# Estágio de notificação

from .stage_base import StageBase

class NotificationStage(StageBase):
    def execute(self, data):
        """Simula o envio de uma notificação caso o processamento tenha sido bem-sucedido."""
        if data.get("processed") or data.get("payment_processed") or data.get("transformed"):
            print("Enviando notificação ao usuário...")
            data["notification"] = "Notificação enviada com sucesso!"
        return data
