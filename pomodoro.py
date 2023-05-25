import time
import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.withdraw()  # Esconde a janela principal
root.attributes('-topmost', True)  # Define a janela como topmost

while True:
    m = simpledialog.askinteger('Minutos', 'Digite os minutos desejados:')
    s = 0
    rest = (0.20 * m) * 60
    print(f'tempo para descanso de: {rest} segundos')

    while m != 0:
        s += 1
        time.sleep(1)
        print(s)
        if s == 60:
            s = 0
            m -= 1
        else:
            continue

    # Exibe o pop-up
    messagebox.showinfo('Take a rest', 'Hora do descanso! :)')

    print('Hora do descanso')
    while rest != 0:
        print(rest)
        rest -= 1
        time.sleep(1)

    messagebox.showinfo('Take a rest', 'Descanso acabou vagabundo!')

    loop = messagebox.askyesno('Again?', 'Se desejar reiniciar a contagem, clique em "Sim". Caso contrário, clique em "Não".')
    if not loop:
        messagebox.showinfo('See you!', 'Bom trabalho, até mais tarde :)')
        break
