import pandas as pd


def split_postcode(df: pd.DataFrame) -> pd.DataFrame:
    """
    Split the `Postal code area` column in the given DataFrame into separate columns for postcode, name, and municipality.

    Args:
        df (pd.DataFrame): The DataFrame containing the `Postal code area` column.

    Returns:
        df (pd.DataFrame): The DataFrame with the `Postal code area` column split into separate columns.
    """
    df.insert(1, "municipality", df["Postal code area"].str.extract(r"\((.*)\)")[0].str.strip())
    df.insert(1, "name", df["Postal code area"].str[5:].str.extract("(.*)\(")[0].str.strip())
    df.insert(1, "postcode", df["Postal code area"].str[:5])
    df = df.drop(columns=["Postal code area"])
    return df


def normalize_by_population(
    df: pd.DataFrame, population_col: str, skip_cols: list[str] = []
) -> pd.DataFrame:
    """
    Normalize the columns of a DataFrame by dividing each column by the corresponding population value.

    Args:
        df (pd.DataFrame): The DataFrame to be normalized.
        population_col (str): The name of the column containing population values.
        skip_cols (list[str], optional): A list of column names to skip normalization. Defaults to [].

    Returns:
        pd.DataFrame: The normalized DataFrame.
    """
    df = df.copy()
    pop_vec = df[population_col]

    skip_norm_cols = [population_col, *skip_cols]
    norm_cols = df.columns[~df.columns.isin(skip_norm_cols)]

    for col in norm_cols:
        df[col] /= pop_vec

    return df
