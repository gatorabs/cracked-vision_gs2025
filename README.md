# 🏚️ Análise de Rachaduras com Visão Computacional

### Projeto Final – Visão Computacional Aplicada à Robótica de Resgate

**Autores:**
- Gabriel José Spioni Estevão – RM94581  
- Marcos Miglioranci Liberati – RM96291  

---

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


## 📦 Instalação e Execução

### 1. Instalação de pacotes

```bash
pip install flask werkzeug opencv-python
```

## 2. Como Executar


Com IDE própria (pycharm/etc) navegue ao diretório da aplicação e inicialize app.py
ou pelo terminal, navegue até o diretório instalado e utilize: python app.py

- Acesse a interface web.
  No terminal aparecerá algo como:  * Running on http://127.0.0.1:5000
- Envie uma imagem da fachada ou estrutura a ser analisada.
- Aguarde o processamento.

Veja o resultado com:
- 📷 Imagem original
- 🛠️ Imagem com contornos destacados

- 📊 Área e comprimento detectados
- 🟢🟡🔴 Classificação da estrutura

- O histórico das últimas análises fica disponível na mesma página, com opção de limpeza.

## 2.5 Estrutura do Projeto

```php
├── app.py                # Aplicação Flask
├── processamento.py      # Pipeline de visão computacional
├── templates/
│   └── index.html        # Interface HTML com Bootstrap
├── static/
│   └── resultados/       # Imagens originais e processadas
└── README.md             # Este documento
```

## 3. 📜 Licença e Aviso

Este projeto foi desenvolvido exclusivamente para fins **acadêmicos** como parte da disciplina de **Visão Computacional Aplicada à Robótica de Resgate em Desastres Naturais** no curso de Engenharia da Computação.

**Uso comercial não autorizado.**  
Todos os direitos reservados aos autores.

---


