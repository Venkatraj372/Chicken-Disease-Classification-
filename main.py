from CNNClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier import logger
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNNClassifier.pipeline.stage_03_train_model import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>> stage{STAGE_NAME}  started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n X====================X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"


try:
    logger.info(f">>>>> stage{STAGE_NAME}  started <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n X====================X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Train Model"

try:
    logger.info(f">>>>> stage{STAGE_NAME}  started <<<<<")
    model_train = ModelTrainingPipeline()
    model_train.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n X====================X")
except Exception as e:
    logger.exception(e)
    raise e


