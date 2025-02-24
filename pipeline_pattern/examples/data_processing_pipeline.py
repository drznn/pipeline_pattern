from pipeline_pattern.src.stages.stage_base import StageBase
from pipeline_pattern.src.pipeline import Pipeline
from pipeline_pattern.src.stages.notification_stage import NotificationStage

class DataExtractionStage(StageBase):
    def execute(self, data):
        """Simula a extração de dados de uma fonte externa."""
        data["extracted"] = True
        return data


class DataTransformationStage(StageBase):
    def execute(self, data):
        """Simula a transformação dos dados extraídos."""
        if data.get("extracted"):
            data["transformed"] = True
        return data


def data_processing_pipeline():
    pipeline = Pipeline()
    pipeline.add_stage(DataExtractionStage())
    pipeline.add_stage(DataTransformationStage())
    pipeline.add_stage(NotificationStage())

    input_data = {"source": "database"}
    result = pipeline.execute(input_data)
    return result
