# Classe principal que gerencia o pipeline

import time

class Pipeline:
    def __init__(self):
        self.stages = []

    def add_stage(self, stage):
        """Adiciona um estágio ao pipeline."""
        self.stages.append(stage)

    def execute(self, data):
        """Executa os estágios em sequência, registrando o tempo de cada um."""
        for stage in self.stages:
            start_time = time.time()
            print(f"Executando: {stage.__class__.__name__} com dados: {data}")
            data = stage.execute(data)
            end_time = time.time()
            print(f"Finalizado: {stage.__class__.__name__} em {end_time - start_time:.4f} segundos.\n")
        return data
