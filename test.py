import datetime


def recebe_data():
    ano = int(input('Insira um ano:\n'))
    mes = int(input('Insira um mês:\n'))
    dia = int(input('Insira um dia:\n'))
    data = datetime.date(ano, mes, dia)

    return data

def converte_data_str_obj(data_str):
    return datetime.datetime.strptime(data_str, '%y')


data_str = int(recebe_data().strftime('%Y'))


print(type(data_str))