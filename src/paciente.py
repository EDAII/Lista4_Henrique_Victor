class Paciente:

    __slots__ = ['nome', 'sexo', 'idade', 'gravidade', 'ordemChegada']

    def __init__(self, nome, sexo, idade, gravidade, ordemChegada):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.gravidade = gravidade
        self.ordemChegada = ordemChegada
    
    def __gt__(self, outro):
        # Ordem de Prioridade
        #
        # 1. Maior Gravidade
        # 2. Idosos (65+) (Entre eles, maior idade)
        # 3. Crianças e Adolescentes (0-17) (Entre elas, menor idade)
        # 5. Adultos (18-64) (Entre eles, maior idade)

        if self.gravidade == outro.gravidade:
            if self.idade >= 65 or outro.idade >= 65:
                return self.idade > outro.idade
            elif self.idade <= 17 or outro.idade <= 17:
                return self.idade < outro.idade
            else:
                return self.idade > outro.idade
        
        return self.gravidade > outro.gravidade
    
    def __lt__(self, outro):
        return not(self > outro)