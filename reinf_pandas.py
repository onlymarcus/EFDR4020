import tagui as t
import rpa as r
import pandas as pd
import time
import pyautogui

# Inicializa o navegador RPA
r.init(visual_automation=True)
r.url('https://cav.receita.fazenda.gov.br/autenticacao/')

# Carrega o arquivo CSV
df = pd.read_csv('R4000OUT23.csv', encoding='cp1252', delimiter=';')

# Renomear as colunas
df.columns = ['CNPJ_EMIT', 'NOME_EMIT', 'CNPJ_REC', 'NOME_REC', 'NP', 'DH_DIA', 'DH_DOCORIG', 'OBSERVACAO',
              'PROCESSO', 'DH_VLR_DOCORIG', 'COMPROM', 'DH_VALOR', 'DARF_BC', 'DARF_VT', 'DARF_COD', 'DARF_DESC', 'REALIZADO']
# Criar uma nova coluna com o código da receita
df['CODIGO_REC'] = df['OBSERVACAO'].str.extract(r'\\(\d{5})')
df['CODIGO_REC'].fillna('', inplace=True)

# Defina uma função para converter corretamente o formato da string para float


def convert_to_float(value):
    if isinstance(value, str):  # Checa se o valor é uma string
        value = value.replace('.', '').replace(',', '.')
    return float(value)


# Aplica a função convert_to_float e depois formata para duas casas decimais
df['DARF_BC'] = df['DARF_BC'].apply(
    convert_to_float).apply(lambda x: f"{x:.2f}")
df['DARF_VT'] = df['DARF_VT'].apply(
    convert_to_float).apply(lambda x: f"{x:.2f}")
df['REALIZADO'] = df['REALIZADO'].apply(
    convert_to_float).apply(lambda x: f"{x:.2f}")

time.sleep(30)

# Itera pelas linhas do DataFrame
for index, row in df.iterrows():
    # Preenche os campos da primeira página
    # Use pyautogui para mover o mouse e clicar no menu suspenso para iniciar o r4000
    r.click(1634, 939)
    pyautogui.press('home')
    r.click('primeiroclick.png')
    r.wait(1)
    r.click('segundoclick.png')
    r.click('casinha.png')
    time.sleep(2)
    r.wait()

    # primeira página com informações gerais
    r.click('periododeapuracao.png')
    pyautogui.write('102023')
    pyautogui.press('tab')
    pyautogui.write('24134488000108', interval=0.1)
    pyautogui.press('tab')
    texto = str(row['CNPJ_REC'])  # CNPJ do recolhedor converter em string
    pyautogui.write(texto, interval=0.1)
    pyautogui.press('tab')
    texto = str(index + 1)  # converter em string
    pyautogui.write(texto, interval=0.1)
    r.click('continuar.png')
    # segunda página, natureza do rendimento pago, clicar em incluir nova
    r.wait(1)
    r.click('incluirnova.png')
    r.wait(1)
    r.click(444, 581)
    pyautogui.press('down', presses=7)
    pyautogui.press('enter')
    pyautogui.press('tab')
    texto = str(row['R'])  # COLUNA R COM A NATUREZA DO RENDIMENTO
    pyautogui.typewrite(texto, interval=0.1)
    pyautogui.press(['tab', 'tab', 'enter'])
    # Terceira página: Detalhamento dos pagamentos ou créditos, clicar incluir novo
    r.click('incluirnovo.png')
    r.wait(1)
    r.click('datadofatogerador.png')
    pyautogui.write('31102023')
    pyautogui.press('tab')
    basedecalc = row['basedecalc']  # VALOR DA BASE DE CÁLCULO
    pyautogui.write(basedecalc)
    pyautogui.press('tab')
    pyautogui.write('n')
    pyautogui.press(['tab', 'tab', 'tab'])
    obser = str(row['I'])  # VALOR DA OBSERVAÇÃO
    pyautogui.write(obser)
    pyautogui.press(['tab', 'tab', 'tab'])
    pyautogui.write(basedecalc)
    pyautogui.press('tab')
    vlrdarf = row['vlrdarf']  # VALOR DO DARF
    pyautogui.write(vlrdarf)
    pyautogui.press(['tab', 'enter'])
    # Pagina de finalização - salvar rascunho
    r.click(1470, 776)
    pyautogui.press('end')
    r.click('salvarrascunho.png')

r.close()  # Fecha a sessão RPA
