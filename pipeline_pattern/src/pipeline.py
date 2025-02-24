# Classe principal que gerencia o pipeline

class Pipeline:
    def __init__(self):
        self.stages = []

    def add_stage(self, stage):
        """Adiciona um estágio ao pipeline."""
        self.stages.append(stage)

    def execute(self, data):
        """Executa os estágios em sequência, passando os dados de um para o próximo."""
        for stage in self.stages:
            data = stage.execute(data)
        return data
