import csv
import json

class Dados:
    def __init__(self, path, tipo_dados):
        self.__path = path
        self.__tipo_dados = tipo_dados
        self.dados = self.__leitura_dados()
        self.colunas = self.obter_nomes_colunas()
        self.qtd_linhas = self.__obter_quantidade_dados()

    def __leitura_json(self):
        dados_A = []
        with open(self.__path, 'r') as file:
            dados_A = json.load(file)
        return dados_A

    def __leitura_csv(self):
        dados_B = []
        with open(self.__path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_B.append(row)
        return dados_B

    def __leitura_dados(self):
        dados = []
        if self.__tipo_dados == "csv":
            dados = self.__leitura_csv()
        elif self.__tipo_dados == "json":
            dados = self.__leitura_json()
        elif self.__tipo_dados == "list":
            dados = self.__path
            self.__path = 'lista em memória'
        return dados

    def obter_nomes_colunas(self):
        return list(self.dados[0].keys())

    def renomear_colunas(self, relation_BA):
        dados_atualizados = []

        for dict in self.dados:
            new_dict = {}
            for key, value in dict.items():
                new_dict[relation_BA[key]] = value
            dados_atualizados.append(new_dict)

        self.dados = dados_atualizados
        self.colunas = self.obter_nomes_colunas()
    
    def __obter_quantidade_dados(self):
        return len(self.dados)
    
    def unir_dados(dados_csv, dados_json):
        dados_AB = []
        dados_AB.extend(dados_json.dados)
        dados_AB.extend(dados_csv.dados) 
        return Dados(dados_AB, "list")
    
    def __transformar_tabela(self):
        dados_AB_tabela = [self.colunas]

        for row in self.dados:
            linha = []
            for coluna in self.colunas:
                linha.append(row.get(coluna, 'Indisponível')) 
            dados_AB_tabela.append(linha)
        return dados_AB_tabela
    
    
    def salvar_tabela(self, path_dadosAB):
        dados_AB_tabela = self.__transformar_tabela()

        with open (path_dadosAB, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_AB_tabela)