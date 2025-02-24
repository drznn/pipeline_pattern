import pytest
from pipeline_pattern.src.stages.auth_stage import AuthStage
from pipeline_pattern.src.stages.processing_stage import ProcessingStage
from pipeline_pattern.src.stages.notification_stage import NotificationStage
from pipeline_pattern.examples.authentication_pipeline import authentication_pipeline
from pipeline_pattern.examples.ecommerce_pipeline import ecommerce_pipeline
from pipeline_pattern.examples.data_processing_pipeline import data_processing_pipeline
import time

def test_pipeline_performance():
    """Testa o tempo de execução do pipeline."""
    start = time.time()
    result = authentication_pipeline()
    end = time.time()

    assert result["auth"] is True
    assert result["processed"] is True
    assert result["notification"] == "Notificação enviada com sucesso!"
    print(f"Teste de desempenho passou! Tempo: {end - start:.4f} segundos.")

def test_auth_stage():
    auth = AuthStage()
    assert auth.execute({"user": "admin", "password": "1234"})["auth"] is True
    assert auth.execute({"user": "user", "password": "wrong"})["auth"] is False

def test_processing_stage():
    processing = ProcessingStage()
    assert processing.execute({"auth": True})["processed"] is True
    assert processing.execute({"auth": False}).get("processed") is None

def test_notification_stage():
    notification = NotificationStage()
    assert notification.execute({"processed": True})["notification"] == "Notificação enviada com sucesso!"
    assert notification.execute({"processed": False}).get("notification") is None


def test_authentication_pipeline():
    result = authentication_pipeline()
    assert result["auth"] is True
    assert result["processed"] is True
    assert result["notification"] == "Notificação enviada com sucesso!"


def test_ecommerce_pipeline():
    result = ecommerce_pipeline()
    assert result["stock_checked"] is True
    assert result["payment_processed"] is True
    assert result["notification"] == "Notificação enviada com sucesso!"


def test_data_processing_pipeline():
    result = data_processing_pipeline()
    assert result["extracted"] is True
    assert result["transformed"] is True
    assert result["notification"] == "Notificação enviada com sucesso!"

if __name__ == "__main__":
    pytest.main()

# Teste dos Pipelines
if __name__ == "__main__":
    print("Autenticação:", authentication_pipeline())
    print("E-commerce:", ecommerce_pipeline())
    print("Processamento de Dados:", data_processing_pipeline())