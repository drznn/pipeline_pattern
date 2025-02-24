# Estágio de processamento de dados

from .stage_base import StageBase

class ProcessingStage(StageBase):
    def execute(self, data):
        """Simula um processamento adicional se a autenticação for bem-sucedida."""
        if data.get("auth"):
            data["processed"] = True
        return data