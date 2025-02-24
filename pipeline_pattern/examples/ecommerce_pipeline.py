# Exemplo 3 - Pipeline de Checkout em E-commerce

from pipeline_pattern.src.stages.stage_base import StageBase
from pipeline_pattern.src.pipeline import Pipeline
from pipeline_pattern.src.stages.notification_stage import NotificationStage

class StockCheckStage(StageBase):
    def execute(self, data):
        """Simula verificação de estoque."""
        data["stock_checked"] = True
        return data


class PaymentProcessingStage(StageBase):
    def execute(self, data):
        """Simula o processamento de pagamento."""
        if data.get("stock_checked"):
            data["payment_processed"] = True
        return data


def ecommerce_pipeline():
    pipeline = Pipeline()
    pipeline.add_stage(StockCheckStage())
    pipeline.add_stage(PaymentProcessingStage())
    pipeline.add_stage(NotificationStage())

    input_data = {"order": "12345"}
    result = pipeline.execute(input_data)
    return result