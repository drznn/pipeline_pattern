# Classe base para os estágios do pipeline

class StageBase:
    def execute(self, data):
        """Método que cada estágio deve implementar."""
        raise NotImplementedError("Execute method must be implemented")
