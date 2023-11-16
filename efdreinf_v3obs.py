import tagui as t
import rpa as r
import openpyxl
import time
import pyautogui

# Inicializa o navegador RPA
r.init(visual_automation=True)
r.url('https://cav.receita.fazenda.gov.br/autenticacao/')

# Abre o arquivo Excel
workbook = openpyxl.load_workbook('r4000novo.xlsx') 
sheet = workbook['Planilha1']
time.sleep(30)
# Define o número máximo de linhas a serem processadas (100 no exemplo)
numero_maximo_linhas = 30

# Itera pelas linhas da planilha
for linha in range(79, numero_maximo_linhas + 79):  # Assumindo que os dados começam na linha 4
    # Preenche os campos da primeira página
    # Use pyautogui para mover o mouse e clicar no menu suspenso para iniciar o r4000
    r.click(1634,939)
    pyautogui.press('home')
    r.click('primeiroclick.png')
    r.wait(1)
    r.click('segundoclick.png')
    r.click('casinha.png')
    time.sleep(2)
    r.wait()

    #primeira página com informações gerais
    r.click('periododeapuracao.png')
    pyautogui.write('092023')
    pyautogui.press('tab')
    pyautogui.write('24134488000108', interval=0.1)
    pyautogui.press('tab')
    texto = str(sheet[f'C{linha}'].value)# CNPJ converter em string
    pyautogui.write(texto, interval=0.1)
    pyautogui.press('tab')
    texto = str(linha)#converter em string
    pyautogui.write(texto, interval=0.1)
    r.click('continuar.png')
    #segunda página, natureza do rendimento pago, clicar em incluir nova
    r.wait(1)
    r.click('incluirnova.png')
    r.wait(1)
    r.click(444,581)
    pyautogui.press('down', presses=7)
    pyautogui.press('enter')
    pyautogui.press('tab')
    texto = str(sheet[f'R{linha}'].value)# COLUNA R COM A NATUREZA DO RENDIMENTO
    pyautogui.typewrite(texto, interval=0.1)
    pyautogui.press(['tab', 'tab', 'enter'])
    #Terceira página: Detalhamento dos pagamentos ou créditos, clicar incluir novo
    r.click('incluirnovo.png')
    r.wait(1)
    r.click('datadofatogerador.png')
    pyautogui.write('31102023')
    pyautogui.press('tab')
    basedecalc = str(sheet[f'S{linha}'].value) # VALOR DA BASE DE CÁLCULO (MULTIPLICAR POR CEM NO EXCEL)
    pyautogui.write(basedecalc)
    pyautogui.press('tab')
    pyautogui.write('n')
    pyautogui.press(['tab', 'tab', 'tab'])
    obser = str(sheet[f'I{linha}'].value) # VALOR DA OBSERVAÇÃO
    pyautogui.write(obser)
    pyautogui.press(['tab', 'tab', 'tab'])
    pyautogui.write(basedecalc)
    pyautogui.press('tab')
    vlrdarf = str(sheet[f'T{linha}'].value)# VALOR DO DARF
    pyautogui.write(vlrdarf)
    pyautogui.press(['tab', 'enter'])
    #Pagina de finalização - salvar rascunho
    r.click(1470,776)
    pyautogui.press('end')
    r.click('salvarrascunho.png')
workbook.close()
r.click('salvarrascunho.png')