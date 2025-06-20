# 🏚️ Análise de Rachaduras com Visão Computacional

### Projeto – Visão Computacional Aplicada à Robótica de Resgate

**Autores:**
- Gabriel José Spioni Estevão – RM94581  
- Marcos Miglioranci Liberati – RM96291  

## 🧠 Contexto

Este projeto simula uma aplicação de visão computacional embarcada em um robô autônomo de resgate, projetado para atuar em **zonas afetadas por desastres naturais**.

O objetivo do robô é **detectar rachaduras em fachadas e estruturas**, a fim de identificar edificações com risco de desmoronamento.

A aplicação web desenvolvida permite **enviar imagens**, processá-las automaticamente com OpenCV, e classificar o estado da estrutura como:

- ✅ **Estável**
- ⚠️ **Alerta**
- ❌ **Risco de Desmoronamento**


## 🔍 Pipeline de Processamento

O pipeline de visão computacional implementado segue estas etapas:

1. **Pré-processamento:**
   - Redimensionamento proporcional
   - Conversão para escala de cinza
   - Filtro de suavização (Gaussian Blur)

2. **Detecção de Bordas:**
   - Filtro de Canny

3. **Segmentação e Extração de Características:**
   - Detecção de contornos
   - Cálculo de área e comprimento das rachaduras

4. **Classificação de Severidade**
Baseada nas métricas extraídas:

| Área (px²) | Comprimento (px) | Classificação         | Cor Indicativa |
|------------|------------------|------------------------|----------------|
| > 2000     | ou > 1500        | ❌ Risco de Desmoronamento | Vermelho       |
| > 1000     | ou > 700         | ⚠️ Alerta               | Amarelo        |
| ≤ 1000     | e ≤ 700          | ✅ Estável              | Verde          |             


## 💻 Tecnologias Utilizadas

- Python 3.11+
- Flask (interface web)
- OpenCV (processamento de imagem)
- HTML + Bootstrap 5 (interface responsiva)


## 📦 Instalação
Bibliotecas necessárias para rodar o Projeto:
```bash
pip install flask werkzeug opencv-python
```




## 2. Como Executar

## ⚠️ Atenção: Antes de rodar o app, verifique se as dependências estão instaladas no ambiente atual!
Use o comando abaixo para instalar os requisitos, se necessário:

### ✅ Com IDE (pycharm)
- Navegue ao diretório da aplicação e inicialize app.py
---
### 💻  Sem IDE
- Pelo terminal, navegue até o diretório instalado e utilize: python app.py
---
- Acesse a interface web.
  No terminal(ou IDE) aparecerá algo como:  ```
                                    Running on http://127.0.0.1:5000
                                    ```
- Envie uma das imagens de rachadura disponíveis na pasta "Images".
- Aguarde o processamento.

Veja o resultado com:
---
- 📷 Imagem original
- 🛠️ Imagem com contornos destacados

- 📊 Área e comprimento detectados
- 🟢🟡🔴 Classificação da estrutura

- O histórico das últimas análises fica disponível na mesma página, com opção de limpeza.

## 📂 2.5 Estrutura do Projeto

```php
├── app.py                # Aplicação Flask
├── processamento.py      # Pipeline de visão computacional
├── templates/
│   └── index.html        # Interface HTML com Bootstrap
├── static/
│   └── resultados/       # Imagens originais e processadas
├── images/               # Imagens de exemplo para teste
└── README.md             # Este documento
```

## 3. 📜 Licença e Aviso

Este projeto foi desenvolvido exclusivamente para fins **acadêmicos** como parte da disciplina de **Visão Computacional e Percepção para Robótica** no curso de Engenharia Mecatrônica.




