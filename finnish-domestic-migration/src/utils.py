import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_top_municipalities_from_demopgraphics(
    data: pd.DataFrame, number_of_municipalities: int = 10
) -> pd.DataFrame:
    """Get top `X` number of municipalities by population.

    Args:
        data (pd.DataFrame): Demographic data
        number_of_municipalities (int): Number of top municipalities to return. Defaults to 10.

    Returns:
        pd.DataFrame: Municipality-population mapping
    """
    data_2019 = data[["Alue 2020", "Tiedot", "2019"]]

    populations_index = data_2019["Tiedot"] == "Väkiluku"  # Fetch rows that contain population
    populations = data_2019[populations_index]

    populations = populations.drop(columns="Tiedot")  # Cleaning and renaming cols
    populations = populations.rename(columns={"Alue 2020": "municipality", "2019": "population"})

    populations["population"] = populations["population"].astype(int)  # type casting for sorting
    populations_sorted = populations.sort_values(
        by="population", ascending=False, ignore_index=True
    )

    # Drop region populations
    is_district = populations_sorted["municipality"].str.contains("(kunta|region)")
    populations_sorted = populations_sorted[~is_district]

    # Choose top municipalities
    top_populations = populations_sorted[1 : number_of_municipalities + 1]

    top_populations["municipality"] = top_populations["municipality"].str.replace(
        pat="�", repl="ä"
    )  # Cleaning 'ä'

    rest_of_finland = populations_sorted[number_of_municipalities + 1 :]

    rest_of_finland = pd.DataFrame({"population": [rest_of_finland.population.sum()]})
    rest_of_finland["municipality"] = "Rest of Finland"
    rest_of_finland.population.sum()

    top_populations = pd.concat([top_populations, rest_of_finland]).reset_index(drop=True)

    return top_populations


def aggregate_counts(
    data: pd.DataFrame, municipalities_keep: pd.DataFrame, column: str
) -> pd.DataFrame:
    """Groups migrations counts for given `column` type.

    Args:
        data (pd.DataFrame): Migration data
        municipalities_keep (pd.DataFrame): Municipalities to aggregate for.
        column (str): Column name (arrival/departure) to aggregate.

    Returns:
        top10_grouped (pd.DataFrame): Total migration counts for `column` in `municipalities_keep`
    """
    regex_key_top10 = f"({'|'.join(list(municipalities_keep['municipality']))})"
    top10_index = pd.Series(data[column]).str.contains(regex_key_top10)
    top10 = data[top10_index]

    top10_grouped = top10.groupby(column).sum()
    top10_grouped.columns = ["Total", "Males", "Females"]

    other = data[~top10_index]
    other_grouped = other.groupby(column).sum()
    other_grouped.columns = ["Total", "Males", "Females"]

    other_grouped = pd.DataFrame(other_grouped.sum(axis=0)).T
    other_grouped.index = ["Rest of Finland"]

    top10_grouped = top10_grouped.append(other_grouped)

    return top10_grouped


def aggregate_data(file_paths: list, municipalities_keep: pd.DataFrame):
    """
    Aggregate migration data from multiple files.
    Municipalities_keep shows the number of muns to keep in the data.

    Args:
        file_paths (list): List of file paths to read the migration data from.
        municipalities_keep (pd.DataFrame): DataFrame containing the municipalities to keep.

    Returns:
        pd.DataFrame: Aggregated migration data.
    """
    migration_data = pd.DataFrame()
    for file in file_paths:
        filename = str(file).split("/")[-1]
        yr = filename.split(".")[0]
        if int(yr) % 5 == 0:  # print progress
            print(yr)

        data = pd.read_csv(file, sep=",", header=0)
        arrival = aggregate_counts(data, municipalities_keep, column="Area of arrival")
        arrival.index = arrival.index.str.replace("Arrival - ", "")

        departure = aggregate_counts(data, municipalities_keep, column="Area of departure")
        departure.index = arrival.index.str.replace("Departure - ", "")

        df_mapping = {
            "departures_total": departure["Total"],
            "arrivals_total": arrival["Total"],
            "departures_female": departure["Females"],
            "arrivals_female": arrival["Females"],
            "departures_male": departure["Males"],
            "arrivals_male": arrival["Males"],
        }

        migration_yr = pd.DataFrame(df_mapping, index=arrival.index.rename("Area"))

        groups = ["total", "male", "female"]

        for sex_group in groups:
            migration_data[f"net_migration_{sex_group}_{yr}"] = (
                migration_yr[[f"departures_{sex_group}", f"arrivals_{sex_group}"]]
                .diff(axis=1)
                .iloc[:, -1]
            )

            migration_data[f"sum_migration_{sex_group}_{yr}"] = migration_yr[
                [f"departures_{sex_group}", f"arrivals_{sex_group}"]
            ].sum(axis=1)
    return migration_data


def convert_to_ts(data: pd.DataFrame, sex_partition: str, migration_count_type: str):
    """
    Convert the given DataFrame into a time series format.

    Args:
        data (pd.DataFrame): The input DataFrame.
        sex_partition (str): The partition based on sex.
        migration_count_type (str): The type of migration count.

    Returns:
        pd.DataFrame: The converted time series DataFrame.
    """
    cols_keep_mask = data.columns.str.contains(
        f"{migration_count_type}.*{sex_partition}", regex=True
    )
    cols_keep = list(data.columns[cols_keep_mask].values)
    data_filtered = data[cols_keep]
    data_ts = data_filtered.T

    yrs = np.arange(1990, 2021, 1)
    data_ts.index = pd.Index(yrs, name="Year")

    return data_ts


def normalize_by_population(data: pd.DataFrame, populations: pd.DataFrame):
    """
    Normalize the data by population.

    Args:
        data (pd.DataFrame): The data to be normalized.
        populations (pd.DataFrame): The population data.

    Returns:
        pd.DataFrame: The normalized data.
    """
    data_normalized = data.copy()
    for _, row in populations.iterrows():
        municip, pop = row
        data_normalized.loc[:, municip] = (data[municip] / pop) * 100

    return data_normalized


class PlotMaker:
    """Helper class for creating plots"""

    def rank_plot(ranks: pd.DataFrame, n_rolling):
        """Create a rank plot for the given `rank` data with `n_rolling` years rolling mean."""
        first_yr = ranks.iloc[n_rolling]
        first_yr.sort_values(ascending=False)
        y_labels = first_yr.sort_values(ascending=True).index

        fig = plt.figure(figsize=(15, 8))
        ax = plt.gca()
        sns.set(font_scale=1.4)
        sns.lineplot(
            data=ranks,
            legend=False,
            ax=ax,
            linewidth=5,
            palette=sns.color_palette("tab10", 11),
        )

        for line in ax.lines:
            line.set_linestyle("-")

        ax.set_yticks(np.arange(1, 12))
        ax.set_yticklabels(y_labels)
        ax.set_ylabel("Net migration rank (1-10)")
        ax.set_xlabel("Year")
        ax.set_title(f"Rank of {n_rolling}-year Rolling Average Net Migration")

        plt.show()

        return fig

    def time_series_plot(data):
        """Create a time series plot."""
        fig = plt.figure(figsize=(15, 8))
        sns.set(font_scale=1.2)

        lines = sns.lineplot(
            data=data.drop(columns="Rest of Finland"),
            palette=sns.color_palette("tab10", 10),
        )
        lines.set_xlabel("Year")
        lines.set_ylabel("Total migration (%)")
        lines.set_title("Time-series of sum migration data normalized by population")

        col_l2 = "firebrick"
        lines2 = sns.lineplot(data=data["Rest of Finland"], linewidth=2, color=col_l2)
        lines2.text(2020 + 0.2, data.iloc[-1, -1], "Rest of Finland", color=col_l2)
        plt.show()

        return fig
