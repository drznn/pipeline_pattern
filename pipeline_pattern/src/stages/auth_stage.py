# Estágio de autenticação

from .stage_base import StageBase

class AuthStage(StageBase):
    def execute(self, data):
        """Simula a verificação de credenciais."""
        if data.get("user") == "admin" and data.get("password") == "1234":
            data["auth"] = True
        else:
            data["auth"] = False
        return data