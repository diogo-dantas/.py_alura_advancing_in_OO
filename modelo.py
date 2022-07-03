from collections.abc import MutableSequence


class MinhaListinhaMutavel(MutableSequence):
    # ABC Class must implement all abstract methods
    pass


class Modulo:

    def __init__(self, prefixo, viagens, fixomodulo=10000):  # fixed cost value negotiated
        self.__prefixo = prefixo
        self._viagens = viagens
        self.__custofixo = round(fixomodulo / len(viagens))

    # Duck Typing - The class has list behaviors but is not a list.

    def __len__(self):  # magic method that defines something is sized
        return len(self._viagens)

    def __getitem__(self, item):  # magic method that defines something is iterable
        return self._viagens[item]

    # getters
    @property
    def qtd_viagens(self):
        return self._viagens

    @property
    def prefixo(self):
        return self.__prefixo

    @property
    def custofixo(self):
        return self.__custofixo

    def __str__(self):  # textual representation of the module class object
        return f' Módulo {self.prefixo}  - QTD de Viagens: {self.__len__()} \n'


class Linha:
    def __init__(self, prefixo, horario, km):
        self.__prefixo = prefixo  # private attribute, security through encapsulation
        self.horario = horario
        self.__km = km  # private attribute
        self.__usuarios = 0  # private attribute

    @property  # without the need to change the places that use the class, unlike getters and setters
    def prefixo(self):
        return self.__prefixo

    @property
    def km(self):
        return self.__km

    @km.setter
    def km(self, novo_km):
        self.__km = novo_km

    @property
    def usuarios(self):  # getter
        return self.__usuarios

    def add_user(self):
        self.__usuarios += 1

    def __str__(self):
        return f'Prefixo: {self.prefixo} \n Horário: {self.horario} QTD KM: {self.km}  QTD Usuários: {self.usuarios} \n'


class Funcionario:
    def __init__(self, registro, nome, linha):
        self.registro = registro
        self.nome = nome.title()
        self.linha = linha
        linha.add_user()

    def __str__(self):
        return f' Colaborador: {self.nome} \n Registro: {self.registro} \n'


class Motorista (Funcionario):
    def __init__(self, registro, nome, linha):
        super().__init__(registro, nome, linha)  # heritage


class Empregado (Funcionario):
    def __init__(self, registro, nome, linha):
        super().__init__(registro, nome, linha)

    def __str__(self):   # superscript method dunder str
        return f' Empregado: {self.nome} \n Registro: {self.registro}  \n Linha Cadastrada: {self.linha} \n'


class Prestador (Funcionario):

    def __init__(self, registro, nome, linha, empresa):
        super().__init__(registro, nome, linha)
        self.empresa = empresa.title()

    def __str__(self):
        return f'Prestador: {self.nome} \n Registro: {self.registro} - Linha Cadastrada: {self.linha} Empresa: {self.empresa}'


# ----- instantied objects  & tests -----

linha1 = Linha('1', 'Entrada', 25)
linha2 = Linha('1', 'Saída', 33)
linha3 = Linha('2', 'Entrada', 45)

dirceu = Motorista('1', 'dirceu lopes da cunha', linha2)

tadeu = Empregado('10001', 'tadeu lopes machado', linha1)

clayton = Prestador('90001', 'clayton cardoso', linha2, 'agronegocios ltda')

print(linha3)

modulo1 = Modulo('001', [linha1, linha2, linha3])

print(modulo1)

for info in modulo1:
    print(f'Linhas atuais: {info.prefixo} - {info.horario} ')

print(f'Valor Custo Fixo: {modulo1.custofixo} \n')

print(dirceu)
print(clayton)
