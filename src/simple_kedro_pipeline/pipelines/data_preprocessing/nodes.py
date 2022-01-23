import pandas as pd


def convert_target_to_int(train_data: pd.DataFrame) -> pd.DataFrame:
	pd.to_numeric(train_data['target'], downcast='integer')
	return train_data


def drop_null_v1_and_null_rows(train_data: pd.DataFrame) -> pd.DataFrame:
	train_without_v1 = train_data[~train_data["V1"].isna()].copy()
	return train_without_v1[~train_without_v1.drop(columns=["Id", "Week", "V1", "V2", "target"]).isna().all(axis=1)]


def preprocess_train(train_data: pd.DataFrame) -> pd.DataFrame:
	train_data = convert_target_to_int(train_data)
	return drop_null_v1_and_null_rows(train_data)
