import csv
import pyperclip as pc
import os

path_csv = os.path.abspath('seu_arquivo_csv.csv')
with open(path_csv, mode='r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    x = 0
    for linha in leitor_csv: break
    for h in linha:
        pc.copy(h)
        cond = input("Digite algo para continuar: ")
        if cond == 'pare': break
        else: continue
        x += 1
        