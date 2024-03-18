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
