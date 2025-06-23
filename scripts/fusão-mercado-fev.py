import json
import csv 

path_json = 'raw-data/dados_empresaA.json'
path_csv = 'raw-data/dados_empresaB.csv'

def leitura_json(path_json):
    dados_A = []
    with open(path_json, 'r') as file:
        dados_A = json.load(file)
        return dados_A

def leitura_csv(path_csv):
    dados_B = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_B.append(row)
    return dados_B

def leitura_dados(path, tipo_arquivo):
    dados = []
    if tipo_arquivo == "csv":
        dados = leitura_csv(path)
    elif tipo_arquivo == "json":
        dados = leitura_json(path)
    return dados

def obter_nomes_colunas(dados):
    return list(dados[-1].keys())

def renomear_colunas(dados, relation_BA):
    colunas_renomeadas_csv = []

    for dict in dados:
        new_dict = {}
        for key, value in dict.items():
            new_dict[relation_BA[key]] = value
        colunas_renomeadas_csv.append(new_dict)
    return colunas_renomeadas_csv

def obter_quantidade_dados(dados):
    return len(dados)

def unir_dados(dados_csv, dados_json):
    dados_AB = []
    dados_AB.extend(dados_json)
    dados_AB.extend(dados_csv) 
    return dados_AB

def transformar_tabela(dados, nomes_colunas):
    dados_AB_tabela = [nomes_colunas]

    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponível')) 
        dados_AB_tabela.append(linha)
    return dados_AB_tabela

def salvar_tabela(path_dadosAB, dados_AB_tabela):
    with open (path_dadosAB, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados_AB_tabela)

# Início da leitura
dados_csv = leitura_dados(path_csv, "csv")
dados_json = leitura_dados(path_json, "json")

nomes_colunas_csv = obter_nomes_colunas(dados_csv)
nomes_colunas_json = obter_nomes_colunas(dados_json)

# Tranformação dos dados
relation_BA = {
    'Nome do Item': 'Nome do Produto', 
    'Classificação do Produto': 'Categoria do Produto', 
    'Valor em Reais (R$)': 'Preço do Produto (R$)', 
    'Quantidade em Estoque': 'Quantidade em Estoque', 
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_csv = renomear_colunas(dados_csv, relation_BA)

# União dos dados
dados_AB = unir_dados(dados_csv, dados_json)
nomes_colunas = obter_nomes_colunas(dados_csv)

# Exportação dos dados
dados_AB_tabela = transformar_tabela(dados_AB, nomes_colunas)
path_dadosAB = 'processed-data/dadosAB.csv'
salvar_tabela(path_dadosAB, dados_AB_tabela)