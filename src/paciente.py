class Paciente:

    __slots__ = ['nome', 'sexo', 'idade', 'gravidade', 'ordemChegada']

    def __init__(self, nome, sexo, idade, gravidade, ordemChegada):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.gravidade = gravidade
        self.ordemChegada = ordemChegada
    
    def __gt__(self, outro):
        if self.gravidade == outro.gravidade
            return self.ano > outro.ano
        
        return self.gravidade > outro.gravidade
    
    def __lt__(self, outro):
        return not(self > outro)