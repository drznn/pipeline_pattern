# Exemplo 3 - Pipeline de Checkout em E-commerce

from src.stages.stage_base import StageBase
from src.pipeline import Pipeline
from src.stages.notification_stage import NotificationStage

class StockCheckStage(StageBase):
    def execute(self, data):
        """Simula verificação de estoque."""
        print("Verificando estoque do pedido...")
        data["stock_checked"] = True
        return data

class PaymentProcessingStage(StageBase):
    def execute(self, data):
        """Simula o processamento de pagamento."""
        if data.get("stock_checked"):
            print("Processando pagamento...")
            data["payment_processed"] = True
        return data

def ecommerce_pipeline():
    """Executa o pipeline de checkout no e-commerce."""
    print("Iniciando o Pipeline de Checkout no E-commerce...")

    pipeline = Pipeline()
    pipeline.add_stage(StockCheckStage())
    pipeline.add_stage(PaymentProcessingStage())
    pipeline.add_stage(NotificationStage())

    input_data = {"order": "12345"}
    result = pipeline.execute(input_data)

    print("Resultado Final do Pipeline de E-commerce:", result)
    return result

# Executando o pipeline quando o script for chamado diretamente
if __name__ == "__main__":
    ecommerce_pipeline()
