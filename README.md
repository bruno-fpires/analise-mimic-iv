# Análise de Dados Clínicos do MIMIC-IV

**Autor:** Bruno Pires  
**Data:** 2025

---

## Mini Guia do Projeto

**Objetivo:**  
Analisar dados clínicos do MIMIC-IV usando Python, gerar estatísticas descritivas, gráficos interativos e relatório PDF opcional.

**Estrutura:**  
- `analise_mimic.py` → script principal  
- `dados/` → subpasta com arquivo `pacientes.csv`  
- `README.md` → este guia

**Execução Rápida:**  
1. Certifique-se que `pacientes.csv` está em `/dados`.  
2. Abra o terminal na pasta do projeto.  
3. Rode:  
   ```bash
   python analise_mimic.py
   ```  
4. Explore tabelas, estatísticas e gráficos.  
5. Ao final, escolha se deseja gerar o relatório PDF e selecione o caminho de salvamento.

---

## Descrição

Este projeto tem como objetivo analisar dados clínicos do banco de dados MIMIC-IV usando Python, gerar estatísticas descritivas, visualizações gráficas e um relatório PDF opcional. Ele permite explorar informações como idade, gênero e correlações entre variáveis numéricas de pacientes.

O código é preparado para ser flexível: os gráficos só são salvos se o usuário desejar, e o caminho de salvamento é selecionado via interface gráfica simples.

---

## Estrutura do Projeto

```
/seu_projeto
│
├── analise_mimic.py        # Script principal para análise dos dados
├── README.md               # Este arquivo
├── dados/                  # Pasta onde os arquivos CSV devem ser armazenados
    └── pacientes.csv       # Arquivo CSV contendo os dados clínicos do MIMIC-IV
```

---

## Bibliotecas Necessárias

- `pandas` → manipulação de dados em tabelas (DataFrames)  
- `numpy` → cálculos e operações numéricas  
- `matplotlib.pyplot` → criação de gráficos básicos  
- `seaborn` → gráficos estatísticos avançados  
- `fpdf` → geração de relatórios PDF  
- `tkinter` → seleção de caminho de salvamento para o PDF  

**Instalação rápida via pip:**  
```bash
pip install pandas numpy matplotlib seaborn fpdf
```

---

## Como Executar

1. Certifique-se de que o arquivo `pacientes.csv` está dentro da pasta `dados/`.  
2. Abra o terminal e navegue até a pasta do projeto.  
3. Execute o script:  
   ```bash
   python analise_mimic.py
   ```  
4. O script exibirá:  
   - Primeiras linhas da tabela  
   - Estatísticas descritivas  
   - Contagem por gênero (se disponível)  
   - Idade média dos pacientes (se disponível)  
   - Gráficos interativos com distribuição de idade, contagem por gênero e mapa de correlação entre variáveis numéricas  
5. Ao final, será perguntado se deseja gerar um relatório PDF. Se sim, você poderá escolher o local e nome do arquivo via interface gráfica.

---

## Funcionalidades Futuras

- Adição de filtros por idade, gênero e condição clínica  
- Exportação de gráficos individualmente  
- Integração com banco de dados SQL do MIMIC-IV  

---

## Observações

- O script remove linhas com valores nulos antes das análises.  
- Todos os gráficos são gerados interativamente; eles só são salvos se o usuário optar.  
- Para acessar os dados MIMIC-IV, é necessário concluir a certificação CITI e obter autorização do PhysioNet.  