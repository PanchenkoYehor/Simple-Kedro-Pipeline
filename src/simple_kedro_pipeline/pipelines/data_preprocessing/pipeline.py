from kedro.pipeline import Pipeline, node

from .nodes import preprocess_train

def create_pipeline(**kwargs):
	return Pipeline(
		[
			node(
				func = preprocess_train,
				inputs = "train_data",
				outputs = "preprocessed_train",
				name = "proprocess_train_node"
			)
		]
	)
