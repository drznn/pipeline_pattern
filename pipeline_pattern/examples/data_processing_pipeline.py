# Exemplo 2 - Pipeline de Processamento de dados

from src.pipeline import Pipeline
from src.stages.stage_base import StageBase
from src.stages.notification_stage import NotificationStage

class DataExtractionStage(StageBase):
    def execute(self, data):
        """Simula a extração de dados de uma fonte externa."""
        print("Extraindo dados da fonte externa...")
        data["extracted"] = True
        return data

class DataTransformationStage(StageBase):
    def execute(self, data):
        """Simula a transformação dos dados extraídos."""
        if data.get("extracted"):
            print("Transformando os dados extraídos...")
            data["transformed"] = True
        return data

def data_processing_pipeline():
    """Executa o pipeline de processamento de dados (ETL)."""
    print("Iniciando o Pipeline de Processamento de Dados...")

    pipeline = Pipeline()
    pipeline.add_stage(DataExtractionStage())
    pipeline.add_stage(DataTransformationStage())
    pipeline.add_stage(NotificationStage())

    input_data = {"source": "database"}
    result = pipeline.execute(input_data)

    print("Resultado Final do Pipeline de Processamento de Dados:", result)
    return result

# Garante que o código roda apenas se for chamado diretamente
if __name__ == "__main__":
    data_processing_pipeline()
