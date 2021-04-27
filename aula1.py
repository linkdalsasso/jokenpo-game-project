import pyautogui
from models.model import Jogador, papel, pedra, tesoura, Computador
from random import randint
from time import sleep


def main():
    pontos = 0
    compontos = 0
    menu(pontos, compontos)


def menu(pontos: int, compontos: int) -> None:
    # print(f'1 - {pedra}, 2 - {papel}, 3 - {tesoura}')
    # opt = int(input('Selecione a opção desejada: '))
    opt = int(pyautogui.confirm(f'1 - Pedra , 2 - Papel , 3 - Tesoura ', buttons=['1', '2', '3']))
    comput_opt = randint(1, 3)

    pyautogui.alert('JOOOOOOOOOOOO')
    sleep(1)
    pyautogui.alert('KEEEEEEEEEEEN')
    sleep(1)
    pyautogui.alert('POOOOOOOOOOOO')
    sleep(1)

    # Pedra
    if opt == 1 and comput_opt == 1 or opt == 2 and comput_opt == 2 or opt == 3 and comput_opt == 3:
        opt2 = str((pyautogui.confirm(f'Você Jogou:\n {pedra}\n'
                                      f'O computador jogou:\n {pedra}\n\n'
                                      'Empate !!!!! \n\n'
                                      f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                                      'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
        if opt2.lower() == 'sim':
            menu(pontos, compontos)
        else:
            pyautogui.alert('Até mais')
            exit()
    elif opt == 1 and comput_opt == 2 or opt == 2 and comput_opt == 3 or opt == 3 and comput_opt == 1:
        compontos += 1
        opt2 = str((pyautogui.confirm(f'Você Jogou:\n {pedra}\n'
                                      f'O computador jogou:\n {papel}\n\n'
                                      'Perdeu !!!!! \n\n'
                                      f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                                      'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
        if opt2.lower() == 'sim':
            menu(pontos, compontos)
        else:
            pyautogui.alert('Até mais')
            exit()
    elif opt == 1 and comput_opt == 3 or opt == 2 and comput_opt == 1 or opt == 3 and comput_opt == 2:
        pontos += 1
        opt2 = str((pyautogui.confirm(f'Você Jogou:\n {pedra}\n'
                                      f'O computador jogou:\n {tesoura}\n\n'
                                      'GANHOU !!!!! \n\n'
                                      f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                                      'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
        if opt2.lower() == 'sim':
            menu(pontos, compontos)
        else:
            pyautogui.alert('Até mais')
            exit()


if __name__ == '__main__':
    main()
