import pyautogui
from models.model import Jogador, papel, pedra, tesoura, Computador
import random
from time import sleep


def main():
    pontos = 0
    compontos = 0
    menu(pontos, compontos)


def opcao_jog(opt):
    if opt.lower() == 'pedra':
        return pedra
    elif opt.lower() == 'papel':
        return papel
    else:
        return tesoura


def opcao_comput(comput_opt):
    if comput_opt.lower() == 'pedra':
        return pedra
    elif comput_opt.lower() == 'papel':
        return papel
    else:
        return tesoura


def menu(pontos: int, compontos: int) -> None:
    # print(f'1 - {pedra}, 2 - {papel}, 3 - {tesoura}')
    # opt = int(input('Selecione a opção desejada: '))
    opt = str(pyautogui.confirm(f'Clique na opção desejada', buttons=['Pedra', 'Papel', 'Tesoura']))
    comput_opt = random.choice(['Pedra', 'Papel', 'Tesoura'])

    pyautogui.alert('JOOOOOOOOOOOO')
    sleep(1)
    pyautogui.alert('KEEEEEEEEEEEN')
    sleep(1)
    pyautogui.alert('POOOOOOOOOOOO')
    sleep(1)

    if opt == 'Pedra' and comput_opt == 'Pedra' or opt == 'Papel' and comput_opt == 'Papel' or opt == 'Tesoura' and comput_opt == 'Tesoura':
        opt2 = str((pyautogui.confirm(f'Você Jogou:\n{opt}\n {opcao_jog(opt)}\n'
                                      f'O computador jogou:\n{comput_opt}\n {opcao_comput(comput_opt)}\n\n'
                                      'Empate !!!!! \n\n'
                                      f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                                      'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
        if opt2.lower() == 'sim':
            menu(pontos, compontos)
        else:
            pyautogui.alert('Até mais')
            exit()

    elif opt == 'Pedra' and comput_opt == 'Papel' or opt == 'Papel' and comput_opt == 'Tesoura' or opt == 'Tesoura' and comput_opt == 'Pedra':
        compontos += 1
        opt2 = str((pyautogui.confirm(f'Você Jogou:\n{opt}\n {opcao_jog(opt)}\n'
                                      f'O computador jogou:\n{comput_opt}\n {opcao_comput(comput_opt)}\n\n'
                                      'Perdeu !!!!! \n\n'
                                      f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                                      'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
        if opt2.lower() == 'sim':
            menu(pontos, compontos)
        else:
            pyautogui.alert('Até mais')
            exit()
    elif opt == 'Pedra' and comput_opt == 'Tesoura' or opt == 'Papel' and comput_opt == 'Pedra' or opt == 'Tesoura' and comput_opt == 'Papel':
        pontos += 1
        opt2 = str((pyautogui.confirm(f'Você Jogou:\n{opt}\n {opcao_jog(opt)}\n'
                                      f'O computador jogou:\n{comput_opt}\n {opcao_comput(comput_opt)}\n\n'
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
