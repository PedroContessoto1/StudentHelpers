import dia_estudos
import util
import verificacao


def cadastra_bloco(informacao):
    arquivo = open("banco_dias.txt", "a")
    arquivo.write(str(informacao) + "\n")


def bloco_class_dia_exer(data, n_exer, n_exer_acertados):
    dia = dia_estudos.Dia_estudo(data, None, n_exer, n_exer_acertados)
    cadastra_bloco(dia)


def bloco_class_dia_capi(data, n_capi):
    dia = dia_estudos.Dia_estudo(data, n_capi, None, None)
    cadastra_bloco(dia)


def cadastra_dia_ex():
    data, n_exer, n_exer_acertados = util.input_dia_exer()
    if not verificacao.exer_ja_existe(data):
        bloco_class_dia_exer(data, n_exer, n_exer_acertados)
    else:
        print("Data ja cadastrada")
        ver = input("Gostaria de deletar e por essa por cima ? (y/n)").upper()
        if ver == "Y":
            dia = dia_estudos.Dia_estudo(data, None, n_exer, n_exer_acertados)
            util.subistituir_dia(str(dia))


def cadastra_dia_cap():
    data, n_capi = util.input_dia_capi()
    if not verificacao.capi_ja_existe(data):
        bloco_class_dia_capi(data, n_capi)
    else:
        print("Data ja cadastrada")
        ver = input("Gostaria de deletar e por essa por cima ? (y/n)")
        if ver == "Y":
            dia = dia_estudos.Dia_estudo(data, n_capi, None, None)
            util.subistituir_dia(str(dia))