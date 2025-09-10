# analise_mimic_relatorio.py
# Análise de dados clínicos do MIMIC-IV usando Python
# Bruno Pires - Artigo

# ------------------------------
# 1. Importando bibliotecas necessárias
# ------------------------------
import pandas as pd # Manipulação de tabelas, leitura de CSV
import numpy as np # Cálculos numéricos
import matplotlib.pyplot as plt # Gráficos
import seaborn as sns # Gráficos avançados
from fpdf import FPDF # Geração de PDF
from tkinter import Tk # Interface gráfica de salvamento
from tkinter.filedialog import asksaveasfilename

# ------------------------------
# 2. Conectando ao MIMIC-IV (exemplo com CSV)
# ------------------------------
caminho_dados = "dados/pacientes.csv"
try:
    df = pd.read_csv(caminho_dados)
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    print(f"Arquivo {caminho_dados} não encontrado. Verifique o caminho.")
    exit()  # Para evitar erros se o CSV não existir

# ------------------------------
# 3. Visualizando os dados
# ------------------------------
print("\nPrimeiras linhas do dataset:")
print(df.head())
print("\nInformações gerais do dataset:")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe(include='all'))

# ------------------------------
# 4. Limpeza de dados
# ------------------------------
df = df.dropna()
print(f"\nDataset após remoção de nulos: {df.shape[0]} linhas restantes")

# ------------------------------
# 5. Análise básica
# ------------------------------
analise_genero = None
if 'gender' in df.columns:
    analise_genero = df['gender'].value_counts()
    print("\nContagem de pacientes por gênero:")
    print(analise_genero)

analise_idade = None
if 'age' in df.columns:
    analise_idade = df['age'].mean()
    print(f"\nIdade média dos pacientes: {analise_idade:.2f} anos")

# ------------------------------
# 6. Visualizações
# ------------------------------
def salvar_grafico(fig, titulo):
    """Pergunta ao usuário se deseja salvar o gráfico e salva se ele confirmar."""
    root = Tk()
    root.withdraw()  # Esconde a janela principal
    caminho = asksaveasfilename(
        title=f"Salvar gráfico - {titulo}",
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )
    root.destroy()
    if caminho:
        fig.savefig(caminho)
        print(f"Gráfico salvo em: {caminho}")
    else:
        print("Gráfico não foi salvo.")

# Histograma de idade
if 'age' in df.columns:
    plt.figure(figsize=(8,5))
    fig = sns.histplot(df['age'], bins=20, kde=True, color='skyblue').get_figure()
    plt.title("Distribuição de Idade dos Pacientes")
    plt.xlabel("Idade")
    plt.ylabel("Frequência")
    plt.show()
    salvar_grafico(fig, "Distribuição de Idade")

# Contagem por gênero
if 'gender' in df.columns:
    plt.figure(figsize=(6,4))
    fig = sns.countplot(x='gender', data=df, palette='Set2').get_figure()
    plt.title("Número de Pacientes por Gênero")
    plt.show()
    salvar_grafico(fig, "Contagem por Gênero")

# ------------------------------
# 7. Correlação entre colunas numéricas
# ------------------------------
numericas = df.select_dtypes(include=np.number)
if not numericas.empty:
    plt.figure(figsize=(10,8))
    fig = sns.heatmap(numericas.corr(), annot=True, cmap='coolwarm').get_figure()
    plt.title("Mapa de Correlação entre Variáveis Numéricas")
    plt.show()
    salvar_grafico(fig, "Mapa de Correlação")

# ------------------------------
# 8. Geração do relatório PDF
# ------------------------------
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Relatório de Análise MIMIC-IV", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)

# Contagem por gênero
if analise_genero is not None:
    pdf.cell(0, 10, "Contagem de Pacientes por Gênero:", ln=True)
    for genero, qtd in analise_genero.items():
        pdf.cell(0, 8, f"{genero}: {qtd}", ln=True)

# Idade média
if analise_idade is not None:
    pdf.ln(5)
    pdf.cell(0, 10, f"Idade média dos pacientes: {analise_idade:.2f} anos", ln=True)

# Estatísticas descritivas
pdf.ln(10)
pdf.cell(0, 10, "Estatísticas descritivas:", ln=True)
desc = df.describe(include='all').round(2)
for col in desc.columns:
    pdf.ln(5)
    pdf.cell(0, 8, f"{col}:", ln=True)
    for stat in desc.index:
        pdf.cell(0, 6, f"  {stat}: {desc.at[stat, col]}", ln=True)

# Salvar PDF
root = Tk()
root.withdraw()
caminho_pdf = asksaveasfilename(
    title="Salvar Relatório PDF",
    defaultextension=".pdf",
    filetypes=[("PDF files", "*.pdf")]
)
root.destroy()
if caminho_pdf:
    pdf.output(caminho_pdf)
    print(f"Relatório PDF salvo em: {caminho_pdf}")
else:
    print("Relatório PDF não foi salvo.")