import tagui as t
import rpa as r
import openpyxl
import time
import pyautogui


# Inicializa o navegador RPA
r.init(visual_automation=True)
r.url('http://google.com')

# Abre o arquivo Excel
workbook = openpyxl.load_workbook('r4000.xlsx')
sheet = workbook['Planilha1']
r.wait()
# Define o número máximo de linhas a serem processadas (100 no exemplo)
numero_maximo_linhas = 3

for linha in range(4, numero_maximo_linhas + 4):  # Assumindo que os dados começam na linha 4
    
    texto = sheet[f'C{linha}'].value
    r.click(855,497)
    pyautogui.typewrite(texto)
    
