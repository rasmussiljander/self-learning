# %% %%
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

from utils import (
    get_top_municipalities_from_demopgraphics,
    aggregate_counts,
    aggregate_data,
    convert_to_ts,
    normalize_by_population,
    PlotMaker,
)

# %%
plotter = PlotMaker
CWD = Path.cwd()
DATA_PATH = CWD.parent / "data"
DATA_PATH

# %%
data = pd.read_csv(DATA_PATH / "municipality_demographic_data.csv", sep=";", header=1)
data.head()


# %%
top_10_municipalities = get_top_municipalities_from_demopgraphics(data)
top_10_municipalities.to_csv(DATA_PATH / "populations_top10.csv", index=False)
top_10_municipalities


# %%
migration_2020 = pd.read_csv(DATA_PATH / "mobility_by_year/2020.csv")
migration_2020


# %%
arrival_top10 = aggregate_counts(migration_2020, top_10_municipalities, column="Area of arrival")
arrival_top10.index = arrival_top10.index.str.replace("Arrival - ", "")

arrival_top10

# %%
departure_top10 = aggregate_counts(
    migration_2020, top_10_municipalities, column="Area of departure"
)
departure_top10.index = departure_top10.index.str.replace("Departure - ", "")
departure_top10

df_mapping = {
    "departures_total": departure_top10["Total"],
    "arrivals_total": arrival_top10["Total"],
    "departures_female": departure_top10["Females"],
    "arrivals_female": arrival_top10["Females"],
    "departures_male": departure_top10["Males"],
    "arrivals_male": arrival_top10["Males"],
}

migration_2020_top10 = pd.DataFrame(df_mapping, index=arrival_top10.index.rename("Area"))
groups = ["total", "male", "female"]

for sex_group in groups:
    migration_2020_top10[f"net_migration_{sex_group}"] = (
        migration_2020_top10[[f"departures_{sex_group}", f"arrivals_{sex_group}"]]
        .diff(axis=1)
        .iloc[:, -1]
    )
    migration_2020_top10[f"total_movement_{sex_group}"] = migration_2020_top10[
        [f"departures_{sex_group}", f"arrivals_{sex_group}"]
    ].sum(axis=1)


migration_2020_top10 = migration_2020_top10.reindex(
    top_10_municipalities["municipality"]
)  # reorder
migration_2020_top10.to_csv(DATA_PATH / "migration_aggregated_top10_2020.csv")
migration_2020_top10


# %%
data_bars = migration_2020_top10.drop(index="Rest of Finland")
fig = plt.figure(figsize=(15, 8))
sns.set(font_scale=1.2)
bar = sns.barplot(
    x=data_bars.index,
    y="net_migration_total",
    data=data_bars,
    color="darkred",
)
bar.set_title("Net migration counts (2020), 10 biggest municipalities", fontsize=18)
bar.set_xlabel("Municipality")
bar.set_ylabel("Net migration")
fig.savefig(CWD.parent / "images/net_migration_total_2020.png")


migration_sex_ungrouped = pd.DataFrame(
    data_bars["net_migration_male"].append(data_bars["net_migration_female"]),
    columns=["net_migration"],
)

sex = np.full(migration_sex_ungrouped.shape[0], "female")
sex[:10] = "male"
migration_sex_ungrouped["sex"] = sex
migration_sex_ungrouped

fig = plt.figure(figsize=(15, 8))
sns.set(font_scale=1.2)
bar = sns.barplot(
    x=migration_sex_ungrouped.index, y="net_migration", data=migration_sex_ungrouped, hue="sex"
)
bar.set_title("Net migration counts (2020) per sex, 10 biggest municipalities", fontsize=18)
bar.set_xlabel("Municipality")
bar.set_ylabel("Net migration")
fig.savefig(CWD.parent / "images/net_migration_per_sex_2020.png")
#
# %%
ts_filepaths = sorted((DATA_PATH / "mobility_by_year").glob("*"))
migration_data = aggregate_data(ts_filepaths, municipalities_keep=top_10_municipalities)

# %%
sum_migration_ts = convert_to_ts(migration_data, sex_partition="total", migration_count_type="sum")
sum_migration_ts = normalize_by_population(sum_migration_ts, top_10_municipalities)
sum_migration_ts

net_migration_ts = convert_to_ts(migration_data, sex_partition="total", migration_count_type="net")
net_migration_ts = normalize_by_population(net_migration_ts, top_10_municipalities)
net_rolling_means = net_migration_ts.rolling(5).mean()

# %%
fig = plotter.time_series_plot(sum_migration_ts)
fig.savefig(CWD.parent / "images/sum_migration_timeseries.png")

fig = plotter.time_series_plot(net_rolling_means)
fig.savefig(CWD.parent / "images/net_migration_timeseries.png")

# %%
n_yrs = 15
n_rolling = 4

ranks_sum = sum_migration_ts.iloc[-n_yrs:, :].rolling(n_rolling - 1).mean().rank(axis=1)

net_migration_ts_unnormalized = convert_to_ts(
    migration_data, sex_partition="total", migration_count_type="net"
)
ranks_net = net_migration_ts_unnormalized.iloc[-n_yrs:, :].rolling(n_rolling).mean().rank(axis=1)

# %%
fig = plotter.rank_plot(ranks_sum, n_rolling=n_rolling - 1)
fig.savefig(CWD.parent / "images/rank_sum_migration_timeseries.png")

fig = plotter.rank_plot(ranks_net, n_rolling=n_rolling)
fig.savefig(CWD.parent / "images/rank_net_migration_timeseries.png")
