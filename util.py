import dia_estudos
import math


def input_dia_exer():
    data = input("data : ")
    n_exer = int(input("numero de exercicios feitos hoje : "))
    n_exer_acertados = int(input("numero de exercicios acertados : "))
    return data, n_exer, n_exer_acertados


def input_dia_capi():
    data = input("data : ")
    n_capi = int(input("numero de capitulos lidos hoje : "))
    return data, n_capi


def return_bloco():
    arquivo = open("banco_dias.txt", "r")
    return arquivo


def comparar_dias_ex_total(dia1, dia2):
    if dia1[2] > dia2[2]:
        resultado_ex_total = dia1[2] - dia2[2]
        print(f"Na data {dia1[0]}, voce fez mais {resultado_ex_total} exercícios")
        print(f"Data {dia1[0]} = {dia1[2]}")
        print(f"Data {dia2[0]} = {dia2[2]}")

    elif dia1[2] < dia2[2]:
        resultado_ex_total = dia2[2] - dia1[2]
        print(f"Na data {dia2[0]}, voce fez mais {resultado_ex_total} exercícios")
        print(f"Data {dia2[0]} = {dia2[2]}")
        print(f"Data {dia1[0]} = {dia1[2]}")

    else:
        print(f"Na data {dia2[0]} e {dia1[0]}\n")
        print(f"Foi feito {dia2[2]} exercicios")


def alterar_linha(index_linha, nova_linha):
    with open("banco_dias.txt", 'r') as f:
        texto = f.readlines()
    with open("banco_dias.txt", 'w') as f:
        for i in texto:
            if texto.index(i) == index_linha:
                f.write(str(nova_linha) + '\n')
            else:
                f.write(i)


def subistituir_dia(dia):
    acc = 0
    dia = eval(dia)
    for i in return_bloco():
        acc += 1
        if dia[0] == eval(i)[0]:
            alterar_linha(acc - 1, dia)


def return_valores_dias(data):
    for i in return_bloco():
        if eval(i)[0] == data:
            return eval(i)
