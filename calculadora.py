import datetime
import json


class GerenciadorDeAnuncios:
    def __init__(self):
        self.VISUALIZACOES_POR_REAL = 30
        self.CLIQUES_POR_VISUALIZACAO = 0.12
        self.COMPARTILHAMENTO_POR_CLIQUE = 0.15
        self.VISUALIZACOES_POR_COMPARTILHAMENTO = 40

    def calc_quantidades(self, dinheiro_investido):
        visualizacoes = dinheiro_investido * self.VISUALIZACOES_POR_REAL

        cliques = visualizacoes * self.CLIQUES_POR_VISUALIZACAO

        compartilhamentos = cliques * self.COMPARTILHAMENTO_POR_CLIQUE * 3

        visualizacoes += compartilhamentos * self.VISUALIZACOES_POR_COMPARTILHAMENTO

        return {"dinheiro_investido": dinheiro_investido, "visualizacoes": visualizacoes, "cliques": cliques, "compartilhamentos": compartilhamentos}

    def opcoes(self):
        print("\nInsira uma das opções abaixo:\n")
        print("1 - Cadastrar anuncio")
        print("2 - Exibir dados dos anuncios cadastrados")
        print("3 - Pesquisa por cliente")
        print("4 - Pesquisar por intervalo de tempo")
        print("\nPressione s para sair")

    def recebe_data(self):
        ano = int(input('Insira um ano:\n'))
        mes = int(input('Insira um mês:\n'))
        dia = int(input('Insira um dia:\n'))
        data = datetime.date(ano, mes, dia)

        return data

    def converte_data_str_obj(self, data_str):
        return datetime.datetime.strftime(data_str, '%y')

    def cadastrar_anuncio(self):
        nome_anuncio = input("Nome do anuncio:\n")
        cliente = input("Cliente:\n")

        print("\nInsira a data de incio:\n")
        data_de_inicio = self.recebe_data()

        print("\nInsira a data de termino:\n")
        data_de_termino = self.recebe_data()

        investimento_diario = float(input("Investimento Diario:\n"))

        diferenca_de_dias = data_de_termino - data_de_inicio
        investimento_total = investimento_diario * diferenca_de_dias.days

        quantidades = self.calc_quantidades(investimento_total)

        data_de_inicio_str = data_de_inicio.ctime()
        data_de_termino_str = data_de_termino.ctime()

        ano_inicio = int(data_de_inicio.strftime('%Y'))
        ano_fim = int(data_de_termino.strftime('%Y'))

        return {"nome_anuncio": nome_anuncio, "cliente": cliente, "investimento_diario": investimento_diario, "investimento_total": investimento_total, "visualizacoes": quantidades["visualizacoes"], "cliques": quantidades["cliques"], "compartilhamentos": quantidades["compartilhamentos"], "data_de_inicio": data_de_inicio_str, "data_de_termino": data_de_termino_str, "ano_inicio": ano_inicio, "ano_fim": ano_fim}

    def ler_database(self):
        with open('db.json') as json_file:
            dados = json.load(json_file)

        for cliente in dados:
           self.mostra_dados(cliente)

    def pesquisar_por_cliente(self, cliente):
        with open('db.json') as json_file:
            dados = json.load(json_file)

        for anuncio in dados:
            if (anuncio['cliente'] == cliente):
                print(
                    "--------------------------------------------------------------------")
                print("Nome do Cliente: " + str(anuncio["cliente"]))
                print("Nome do Anuncio: " + str(anuncio["nome_anuncio"]))
                print("Total de cliques: " + str(anuncio["cliques"]))
                print("Total de compartilhamentos: " + str(anuncio["compartilhamentos"])) 

        print("--------------------------------------------------------------------")

    def filtrar_por_tempo(self, data_inicio, data_final):
        with open('db.json') as json_file:
            dados = json.load(json_file)

        for anuncio in dados:
            if anuncio['ano_inicio'] <= data_final and anuncio['ano_fim'] >= data_inicio:
                self.mostra_dados(anuncio)

    def mostra_dados(self ,anuncio):
        print("-------------------------------------------------")
        print("Nome do Anuncio:" + anuncio['nome_anuncio'])
        print("Cliente: " + anuncio["cliente"])
        print("Quantidade de visualizações: " + str(anuncio["visualizacoes"]))
        print("Quantidade de cliques: " + str(anuncio["cliques"]))
        print("Compartilhamentos: " + str(anuncio["compartilhamentos"]))
        print("Data de inicio: " + anuncio["data_de_inicio"])
        print("Data de termino: " + anuncio["data_de_termino"])
        print("--------------------------------------------------")
        
    def sistema_anuncios(self):

        try:
            with open('db.json', 'r') as simple_database:
                anuncios = json.load(simple_database)
        except:
            anuncios = []


        res = ''
    
        while res != 's'.lower():
            print("\nBem vindo ao sistema de cadastros de anuncios!\n")
            self.opcoes()
            res = input()
            
            if (res == '1'):
                anuncio_cadastrado = self.cadastrar_anuncio()
                anuncios.append(anuncio_cadastrado)
                with open('db.json', 'w') as simple_database:
                    json.dump(anuncios, simple_database)

                self.opcoes()
                res = input()

            if (res == '2'):
                self.ler_database()
                self.opcoes()
                res = input()

            if (res == '3'):
                cliente = input("Insira o nome do cliente: ")
                self.pesquisar_por_cliente(cliente)
                self.opcoes()
                #res = input()

            if (res == '4'):
                data_inicio = int(input('Insira a data de inicio: '))
                data_fim = int(input('Insira a data de fim: '))
                self.filtrar_por_tempo(data_inicio, data_fim)
                self.opcoes()
                res = input()


calculadora = GerenciadorDeAnuncios()
calculadora.sistema_anuncios()

