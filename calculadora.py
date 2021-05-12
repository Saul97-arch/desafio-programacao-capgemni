import datetime
import json

# Colocar tudo dentro de uma classe
# teste vanilla, cada componente seria uma função


def calculadora_anuncios(dinheiro_investido):

    VISUALIZACOES_POR_REAL = 30
    CLIQUES_POR_VISUALIZACAO = 0.12
    COMPARTILHAMENTO_POR_CLIQUE = 0.15
    VISUALIZACOES_POR_COMPARTILHAMENTO = 40

    visualizacoes = dinheiro_investido * VISUALIZACOES_POR_REAL

    cliques = visualizacoes * CLIQUES_POR_VISUALIZACAO

    compartilhamentos = cliques * COMPARTILHAMENTO_POR_CLIQUE * 4

    visualizacoes += compartilhamentos * VISUALIZACOES_POR_COMPARTILHAMENTO

    return {"dinheiro_investido": dinheiro_investido, "visualizacoes": visualizacoes, "cliques": cliques, "compartilhamentos": compartilhamentos}


def opcoes():
    print("\nInsira uma das opções abaixo:\n")

    print("1 - Cadastrar anuncio\n")
    print("2 - Exibir dados dos anuncios cadastrados")
    print("Pressione s para sair\n")


def recebe_data():
    ano = int(input('Insira um ano:\n'))
    mes = int(input('Insira um mês:\n'))
    dia = int(input('Insira um dia:\n'))
    data = datetime.date(ano, mes, dia)

    return data

# testar se funfa


def converte_data_str_obj(data_str):
    return datetime.datetime.strftime(data_str, '%y')


def cadastrar_anuncio():
    nome_anuncio = input("Nome do anuncio:\n")
    cliente = input("Cliente:\n")

    print("\nInsira a data de incio:\n")
    data_de_inicio = recebe_data()

    print("\nInsira a data de termino:\n")
    data_de_termino = recebe_data()

    investimento_diario = float(input("Investimento Diario:\n"))

    diferenca_de_dias = data_de_termino - data_de_inicio
    investimento_total = investimento_diario * diferenca_de_dias.days

    quantidades = calculadora_anuncios(investimento_total)

    data_de_inicio_str = data_de_inicio.ctime()
    data_de_termino_str = data_de_termino.ctime()

    ano_inicio = int(data_de_inicio.strftime('%Y'))
    ano_fim = int(data_de_termino.strftime('%Y'))

    return {"nome_anuncio": nome_anuncio, "cliente": cliente, "investimento_diario": investimento_diario, "investimento_total": investimento_total, "visualizacoes": quantidades["visualizacoes"], "cliques": quantidades["cliques"], "compartilhamentos": quantidades["compartilhamentos"], "data_de_inicio": data_de_inicio_str, "data_de_termino": data_de_termino_str, "ano_inicio": ano_inicio, "ano_fim": ano_fim}


def ler_database():
    with open('data.json') as json_file:
        dados = json.load(json_file)

    for cliente in dados:
        print("--------------------------------------------------------------------")
        print("Nome do Cliente: " + str(cliente["cliente"]))
        print("Nome do Anuncio: " + str(cliente["nome_anuncio"]))
        print("Total de cliques: " + str(cliente["cliques"]))
        print("Total de compartilhamentos: " + str(cliente["compartilhamentos"]))

    print("--------------------------------------------------------------------")   


def sistema_anuncios():

    try:
        with open('data.json', 'r') as simple_database:
            anuncios = json.load(simple_database)
    except:
        anuncios = []

    res = ""

    print("Bem vindo ao sistema de cadastros de anuncios!\n")
    opcoes()

    while res != 's'.lower():
        res = input()
        opcoes()

        if (res == '1'):
            anuncio_cadastrado = cadastrar_anuncio()
            anuncios.append(anuncio_cadastrado)
            with open('data.json', 'w') as simple_database:
                json.dump(anuncios, simple_database)

            opcoes()
            res = input()

        if (res == '2'):
            ler_database()
            opcoes()
            res = input()

        if (res == '3'):
            pass

        # print(anuncios)


sistema_anuncios()
