import threading
import tkinter


root = tkinter.Tk()
tkinter.Frame(root, width=250, height=100).pack()
tkinter.Label(root, text='TEXTO AQUI').place(x=100, y=10)

threading.Timer(1.0, root.destroy).start()

root.mainloop()
exit()

# Papel
elif opt == 2 and comput_opt == 2:
opt2 = str((pyautogui.confirm(f'Você Jogou:\n {papel}\n'
                              f'O computador jogou:\n {papel}\n\n'
                              'Empate !!!!! \n\n'
                              f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                              'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
if opt2.lower() == 'sim':
    menu(pontos, compontos)
else:
    pyautogui.alert('Até mais')
    exit()
elif opt == 2 and comput_opt == 3:
compontos += 1
opt2 = str((pyautogui.confirm(f'Você Jogou:\n {papel}\n'
                              f'O computador jogou:\n {tesoura}\n\n'
                              'Perdeu !!!!! \n\n'
                              f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                              'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
if opt2.lower() == 'sim':
    menu(pontos, compontos)
else:
    pyautogui.alert('Até mais')
    exit()
elif opt == 2 and comput_opt == 1:
pontos += 1
opt2 = str((pyautogui.confirm(f'Você Jogou:\n {papel}\n'
                              f'O computador jogou:\n {pedra}\n\n'
                              'GANHOU !!!!! \n\n'
                              f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                              'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
if opt2.lower() == 'sim':
    menu(pontos, compontos)
else:
    pyautogui.alert('Até mais')
    exit()

# Tesoura
if opt == 3 and comput_opt == 3:
    opt2 = str((pyautogui.confirm(f'Você Jogou:\n {tesoura}\n'
                                  f'O computador jogou:\n {tesoura}\n\n'
                                  'Empate !!!!! \n\n'
                                  f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                                  'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
    if opt2.lower() == 'sim':
        menu(pontos, compontos)
    else:
        pyautogui.alert('Até mais')
        exit()
elif opt == 3 and comput_opt == 1:
    compontos += 1
    opt2 = str((pyautogui.confirm(f'Você Jogou:\n {tesoura}\n'
                                  f'O computador jogou:\n {pedra}\n\n'
                                  'Perdeu !!!!! \n\n'
                                  f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                                  'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
    if opt2.lower() == 'sim':
        menu(pontos, compontos)
    else:
        pyautogui.alert('Até mais')
        exit()
elif opt == 3 and comput_opt == 2:
    pontos += 1
    opt2 = str((pyautogui.confirm(f'Você Jogou:\n {tesoura}\n'
                                  f'O computador jogou:\n {papel}\n\n'
                                  'GANHOU !!!!! \n\n'
                                  f'Pontuação: Jogador: {pontos}, Computador: {compontos}\n\n'
                                  'Deseja continuar jogando?: ', buttons=['Sim', 'Não'])))
    if opt2.lower() == 'sim':
        menu(pontos, compontos)
    else:
        pyautogui.alert('Até mais')
        exit()

