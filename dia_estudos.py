class Dia_estudo:
    def __init__(self, data, capitulos, n_exer, n_exer_acertados):
        self.data = data
        self.capitulos = capitulos
        self.n_exer = n_exer
        self.n_exer_acertados = n_exer_acertados
        self.n_exer_errado = n_exer - n_exer_acertados

    def __str__(self):
        return f"{self.data,self.capitulos,self.n_exer,self.n_exer_acertados,self.n_exer_errado}"



