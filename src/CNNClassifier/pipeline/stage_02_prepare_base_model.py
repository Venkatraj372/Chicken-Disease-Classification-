from CNNClassifier.config.configuration import ConfigManager
from CNNClassifier import logger
from CNNClassifier.entity.config_entity import PrepareBaseModelConfig
from CNNClassifier.components.preparebasemodel import PrepareBaseModel



STAGE_NAME = "Prepare Base Model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage{STAGE_NAME}  started <<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n X====================X")
    except Exception as e:
        logger.exception(e)
        raise e
