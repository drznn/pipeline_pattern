# Estágio de autenticação

from .stage_base import StageBase

class AuthStage(StageBase):
    def execute(self, data):
        """Simula a verificação de credenciais com validação de entrada."""
        if not isinstance(data, dict):
            raise ValueError("Os dados devem ser um dicionário.")
        
        if data.get("user") == "admin" and data.get("password") == "1234":
            data["auth"] = True
            print("Autenticação bem-sucedida.")
        else:
            data["auth"] = False
            print("Falha na autenticação.")
        return data
