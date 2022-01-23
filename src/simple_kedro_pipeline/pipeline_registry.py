"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from simple_kedro_pipeline.pipelines import data_preprocessing as dp


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    data_preprocessing_pipeline = dp.create_pipeline()

    return {
        "dp": data_preprocessing_pipeline,
        "__default__": data_preprocessing_pipeline
    }
