from CNNClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier import logger

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>> stage{STAGE_NAME}  started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n X====================X")
except Exception as e:
    logger.exception(e)
    raise e