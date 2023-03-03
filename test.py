import random


def names(message):
    name_list = message.split(' и ')
    mes = name_list[0] + ' и ' + name_list[1] + ' любят друг друга на ' + str(calc(name_list[0], name_list[1])) + '%'
    return mes

def calc(name1, name2):
    calc = random.randint(1,100)
    return calc
