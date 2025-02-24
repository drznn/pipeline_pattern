from src.pipeline import Pipeline
from src.stages.auth_stage import AuthStage
from src.stages.processing_stage import ProcessingStage
from src.stages.notification_stage import NotificationStage

def authentication_pipeline():
    print("Executando Pipeline de Autenticação...")
    pipeline = Pipeline()
    pipeline.add_stage(AuthStage())
    pipeline.add_stage(ProcessingStage())
    pipeline.add_stage(NotificationStage())

    input_data = {"user": "admin", "password": "1234"}
    result = pipeline.execute(input_data)
    
    # Adicionando print para visualizar os resultados
    print("Resultado Final do Pipeline de Autenticação:", result)
    return result


# Garante que o código roda apenas se for chamado diretamente
if __name__ == "__main__":
    authentication_pipeline()
