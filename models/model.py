class Jogador:
    pontos = 0

    def __init__(self, nome, pontos):
        self.__nome = nome
        self.__pontos = pontos

    @property
    def nome(self):
        return self.__nome

    @property
    def pontos(self):
        return self.__pontos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos


class Computador:
    pontos = 0

    def __init__(self, pontos):
        self.__pontos = pontos

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos


pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   _____)
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)
          _________)
       _____________)
      (____)
---.__(___)
'''
