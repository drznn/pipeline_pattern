## SE ESTIVER COM ERROS DE EXECUÇÃO NO TESTE DE NÃO ECONTRAR O MODULO /SRC. RODAR O COMANDO ABAIXO NO TERMINAL
## $env:PYTHONPATH = ".;src"


import pytest
import time
from src.stages.auth_stage import AuthStage
from src.stages.processing_stage import ProcessingStage
from src.stages.notification_stage import NotificationStage
from examples.authentication_pipeline import authentication_pipeline
from examples.ecommerce_pipeline import ecommerce_pipeline
from examples.data_processing_pipeline import data_processing_pipeline

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
