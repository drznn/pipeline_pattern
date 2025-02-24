from pipeline_pattern.src.pipeline import Pipeline
from pipeline_pattern.src.stages.auth_stage import AuthStage
from pipeline_pattern.src.stages.processing_stage import ProcessingStage
from pipeline_pattern.src.stages.notification_stage import NotificationStage

def authentication_pipeline():
    pipeline = Pipeline()
    pipeline.add_stage(AuthStage())
    pipeline.add_stage(ProcessingStage())
    pipeline.add_stage(NotificationStage())

    input_data = {"user": "admin", "password": "1234"}
    result = pipeline.execute(input_data)
    return result
