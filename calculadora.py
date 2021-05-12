import datetime
import json

# Colocar tudo dentro de uma classe
# teste vanilla, cada componente seria uma função
# mudar pra snake_case
# criar base de dados em JSON


def calculadora_anuncios(dinheiroInvestido):

    VISUALIZACOES_POR_REAL = 30
    CLIQUES_POR_VISUALIZACAO = 0.12
    COMPARTILHAMENTO_POR_CLIQUE = 0.15
    VISUALIZACOES_POR_COMPARTILHAMENTO = 40

    visualizacoes = dinheiroInvestido * VISUALIZACOES_POR_REAL

    cliques = visualizacoes * CLIQUES_POR_VISUALIZACAO

    compartilhamentos = cliques * COMPARTILHAMENTO_POR_CLIQUE * 4

    visualizacoes += compartilhamentos * VISUALIZACOES_POR_COMPARTILHAMENTO

    return {"dinheiroInvestido": dinheiroInvestido, "visualizacoes": visualizacoes, "cliques": cliques, "compartilhamentos": compartilhamentos}


def opcoes():
    print("\nInsira uma das opções abaixo:\n")

    print("1 - cadastrar anuncio\n")

    print("Pressione s para sair\n")


def recebeData():
    ano = int(input('Insira um ano:\n'))
    mes = int(input('Insira um mês:\n'))
    dia = int(input('Insira um dia:\n'))
    data = datetime.date(ano, mes, dia)

    return data


def cadastrar_anuncio():
    nomeAnuncio = input("Nome do anuncio:\n")
    cliente = input("Cliente:\n")

    print("\nInsira a data de incio:\n")
    dataDeInicio = recebeData()

    print("\nInsira a data de termino:\n")
    dataDeTermino = recebeData()

    investimentoDiario = float(input("Investimento Diario:\n"))

    diferenca_de_dias = dataDeTermino - dataDeInicio
    investimento_total = investimentoDiario * diferenca_de_dias.days

    quantidades = calculadora_anuncios(investimento_total)

    # Modularizar a entrega de quantidades talvez, deixar o retorno do cadastro de anuncio mais limpo
    # De fato vai ficar to retornando só pra ver mesmo kkk

    # Implementar a persistência com JSON.
    # Filtra por intervalo de tempo e cliente
    # Fazer testes
    
    return {"nomeAnuncio": nomeAnuncio, "cliente": cliente, "investimentoDiario": investimentoDiario, "investimento_total": investimento_total, "visualizacoes": quantidades["visualizacoes"], "cliques": quantidades["cliques"], "compartilhamentos": quantidades["compartilhamentos"]}


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
            # retornar logo as quatro condições
            """  valor total investido

             quantidade máxima de visualizações

             quantidade máxima de cliques

             quantidade máxima de compartilhamentos """

        if (res == '3'):
            pass
        
        print(anuncios)


sistema_anuncios()
