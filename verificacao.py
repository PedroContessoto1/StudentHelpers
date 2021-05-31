import util


def dia_ja_existe(data):
    for i in util.return_bloco():
        if data == i[0]:
            return True


def exer_ja_existe(data):
    for i in util.return_bloco():
        i = eval(i)
        if data == i[0] and i[2] is not None:
            return True


def capi_ja_existe(data):
    for i in util.return_bloco():
        i = eval(i)
        if data == i[0] and i[1] is not None:
            return True

