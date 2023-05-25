import time
import tkinter as tk
from tkinter import messagebox, simpledialog

# Inicia a criação de um pop-up
root = tk.Tk()
root.title('Contagem de Tempo')
root.geometry('300x200')
root.attributes('-topmost', True)  # Define a janela como topmost, por cima de todas as janelas abertas

# Inicia o pop-up de contagem
countdown_label = tk.Label(root, text='')
countdown_label.pack(pady=20)

while True:
    # Recebe os mintos desejados exibindo-os no pop-up e calcula o tempo de descanso
    m = simpledialog.askinteger('Minutos', 'Digite os minutos desejados:')
    s = 0
    rest = int((0.20 * m) * 60)
    countdown_label.config(text=f'Tempo para descanso: {rest} segundos')
    
    while m != 0:
        m -= 1
        for s in range(60):
            countdown_label.config(text=f'Tempo restante de trabalho: \n{m} minutos, {60-s} segundos')
            time.sleep(1)
            root.update()

    # Exibe o pop-up indicando é hora do descanso
    messagebox.showinfo('Take a rest!', 'Hora do descanso! :)')


    # Exibe o pop-up com tempo de descanso restante
    minute = rest//60
    while rest != 0:
        for s in range(60):
            take_rest = countdown_label.config(text=f'Descanso restante:\n {minute} minutes, {60-s} segundos')
            time.sleep(1)
            root.update()
        minute -= 1

    
    messagebox.showinfo('It´s Over!!', 'Descanso acabou vagabundo!')

    # Recebe a entrada de continuar com outro valor ou sair da aplicação
    loop = messagebox.askyesno('Again?', 'Se desejar reiniciar a contagem, clique em "Sim". Caso contrário, clique em "Não".')
    if not loop:
        messagebox.showinfo('Nice work', 'Muito bem, até mais tarde :)')
        root.quit()
        break
