import datetime
import pandas as pd


def filter_dataframe_by_dates(df, start_date, end_date, date_column_name):
    """
    Filter a Dataframe, df, by the start and end dates, based on the date_column_name.

    :param df a Pandas Dataframe.
    :param start_date the start date of the filter. (Inclusive)
    :param end_date the end date of the filter. (Inclusive)

    Example:
        start_date = datetime.datetime(year=2021, month=1,day=1)
        end_date = datetime.datetime(year=2021, month=12, day=31)
    """
    mask = (df[date_column_name] > start_date) & (df[date_column_name] <= end_date)
    return df.loc[mask]


def train_test_base_on_date(df: pd.Dataframe, train_start_date: datetime.datetime, train_end_date: datetime.datetime,
                            test_start_date: datetime.datetime, test_end_date: datetime.datetime, date_column_name: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    The original input Dataframe is separated into two separate dataframes.
    A training and testing dataframe, based on the input dates. Training first, testing second.

    :param df: input dataframe of original data.
    :type pd.Dataframe
    :param train_start_date: start date of the training data.
    :type datetime.datetime
    :param train_end_date: End date of the training data.
    :type datetime.datetime
    :param test_start_date: Start date of the test data.
    :type datetime.datetime
    :param test_end_date: End date of the test data.
    :type datetime.datetime
    :param date_column_name: the name of column which holds the date data.
    :type str
    :return: df_train and df_test.
    """
    df_train = filter_dataframe_by_dates(df, train_start_date, train_end_date, date_column_name)
    df_test = filter_dataframe_by_dates(df, test_start_date, test_end_date, date_column_name)
    return df_train, df_test
