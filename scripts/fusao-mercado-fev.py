from processamento_dados import Dados

path_json = 'raw-data/dados_empresaA.json'
path_csv = 'raw-data/dados_empresaB.csv'

# Criação dos objetos
dados_empresaA = Dados(path_json, "json") 
dados_empresaB = Dados(path_csv, "csv")
# print(dados_empresaB.colunas)
# print(dados_empresaA.colunas)

# Transformação:
relation_BA = {
    'Nome do Item': 'Nome do Produto', 
    'Classificação do Produto': 'Categoria do Produto', 
    'Valor em Reais (R$)': 'Preço do Produto (R$)', 
    'Quantidade em Estoque': 'Quantidade em Estoque', 
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}
dados_empresaB.renomear_colunas(relation_BA)

dados_fusao = Dados.unir_dados(dados_empresaA, dados_empresaB)


# Carregamento
path_dadosAB = 'processed-data/dadosAB.csv'
dados_fusao.salvar_tabela(path_dadosAB)


