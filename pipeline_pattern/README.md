# Pipeline Pattern - Documentação Oficial

## 📌 Introdução

Este repositório implementa um **Pipeline Pattern** modular para diversas aplicações. Ele permite a construção de fluxos de processamento de dados de maneira organizada, onde cada **estágio** executa uma transformação ou ação específica nos dados antes de passá-los para o próximo estágio.

## 🎯 Motivação

Este projeto foi desenvolvido como parte da disciplina **Reuso de Software**, com o objetivo de explorar a reutilização de padrões arquiteturais no desenvolvimento de software. O **Pipeline Pattern** foi escolhido por sua flexibilidade, organização modular e aplicabilidade em diversos domínios, como autenticação, processamento de dados e e-commerce.

### **Equipe do Projeto**

- **Andre Silva Cavalcanti de Albuquerque** - 378667 - a.albuquerque@alu.ufc.br
- **Antonio Elliton Dias Gomes** - 499843 - ellitond26@gmail.com 
- **Antonio Kaio Elias Portela** - 494707 - kaioportela@alu.ufc.br 
- **Wilhelm de Sousa Steins** - 495961 - wilhelmsteins@gmail.com 
- **Mateus Gonçalves Loiola** - 496797 - mateustaua16@gmail.com

## 📁 Estrutura do Projeto

A organização do repositório segue uma estrutura modular, garantindo a **separação de responsabilidades** e a **facilidade de manutenção**:

```
/pipeline_pattern
│── /examples                # Exemplos de uso do pipeline
│   ├── authentication_pipeline.py   # Pipeline de Autenticação
│   ├── data_processing_pipeline.py  # Pipeline de Processamento de Dados (ETL)
│   ├── ecommerce_pipeline.py        # Pipeline de Checkout de E-commerce
│
│── /src                     # Implementação do Pipeline Pattern
│   ├── pipeline.py           # Classe principal do pipeline
│   ├── /stages               # Estágios do pipeline
│   │   ├── __init__.py       # Indica que esta pasta é um pacote
│   │   ├── auth_stage.py     # Estágio de Autenticação
│   │   ├── processing_stage.py  # Estágio de Processamento
│   │   ├── notification_stage.py # Estágio de Notificação
│   │   ├── stage_base.py     # Classe Base para os Estágios
│
│── /tests                   # Testes automatizados
│   ├── test_pipeline.py      # Testes do pipeline
│
│── README.md                # Documentação do projeto
│── requirements.txt          # Dependências do projeto
│── LICENSE                   # Licença de uso
```

## 🚀 Como Executar

### 1️⃣ **Clonar o Repositório**
```bash
git clone https://github.com/drznn/pipeline_pattern.git
cd pipeline_pattern
```

### 2️⃣ **Instalar Dependências**
Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ **Executar os Pipelines de Exemplo**
#### **🔐 Pipeline de Autenticação**
```bash
python examples/authentication_pipeline.py
```

#### **📊 Pipeline de Processamento de Dados**
```bash
python examples/data_processing_pipeline.py
```

#### **🛒 Pipeline de Checkout de E-commerce**
```bash
python examples/ecommerce_pipeline.py
```

## ✅ Rodando os Testes
Se houver problemas de importação ao rodar os testes, **execute o seguinte comando primeiro**:
```powershell
$env:PYTHONPATH = ".;src"
```
Agora, rode os testes:
```bash
pytest tests/test_pipeline.py -s
```
Se todos os testes passarem, você verá a saída:
```
======= 7 passed in X.XXs =======
```

## 🔍 Explicação Técnica

O **Pipeline Pattern** permite organizar um fluxo de execução sequencial e modular. Cada **estágio** do pipeline é uma classe separada, e novos estágios podem ser adicionados sem impactar o funcionamento geral.

### 🔹 **Diferencial do Padrão de Projeto**
O **Pipeline Pattern** foi escolhido por oferecer:
- 🔄 **Modularidade:** Cada etapa do processamento é independente.
- 🚀 **Reuso de Código:** Novos pipelines podem ser construídos reaproveitando estágios existentes.
- ⚡ **Facilidade de Testes:** Cada estágio pode ser testado isoladamente.
- 🔧 **Extensibilidade:** Novos estágios podem ser adicionados sem alterar o pipeline principal.

### 🔹 **Componentes Principais:**
- **`Pipeline` (src/pipeline.py)** → Gerencia a sequência de execução dos estágios.
- **`StageBase` (src/stages/stage_base.py)** → Classe base para todos os estágios.
- **Estágios Implementados:**
  - **Autenticação (`auth_stage.py`)** → Valida credenciais do usuário.
  - **Processamento (`processing_stage.py`)** → Executa ações com base nos dados recebidos.
  - **Notificação (`notification_stage.py`)** → Envia notificações ao final do processo.

## ❓ O Que Fazer em Caso de Dúvidas?
Se encontrar dificuldades ao executar o projeto:
1. Verifique se todas as dependências estão instaladas com `pip list`.
2. Certifique-se de estar executando os comandos **da raiz do projeto**.
3. Se ocorrer erro de importação, tente rodar:
   ```powershell
   $env:PYTHONPATH = ".;src"
   ```
4. Consulte os arquivos de exemplo para entender como rodar os pipelines corretamente.

Caso ainda tenha problemas, entre em contato com um dos integrantes do projeto pelo e-mail listado acima.

## 📜 Licença
Este projeto está licenciado sob a **MIT License** – veja o arquivo `LICENSE` para mais detalhes.

---
### 🚀 **Dúvidas ou Sugestões?**
Fique à vontade para abrir uma **issue** no repositório oficial:  
🔗 [GitHub Repository](https://github.com/drznn/pipeline_pattern.git)

