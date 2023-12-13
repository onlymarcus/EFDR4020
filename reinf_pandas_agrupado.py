import tagui as t
import rpa as r
import pandas as pd
import time
import pyautogui

# Inicializa o navegador RPA
r.init(visual_automation=True)
r.url('https://cav.receita.fazenda.gov.br/autenticacao/')

# Carrega o arquivo CSV
df = pd.read_csv('efdr4000nov23.csv', encoding='cp1252', delimiter=';')

# Renomear as colunas
df.columns = ['CNPJ_EMIT', 'NOME_EMIT', 'CNPJ_REC', 'NOME_REC', 'NP', 'DH_DIA', 'DH_DOCORIG', 'OBSERVACAO',
              'PROCESSO', 'DH_VLR_DOCORIG', 'COMPROM', 'DH_VALOR', 'DARF_BC', 'DARF_VT', 'DARF_COD', 'DARF_DESC', 'REALIZADO']
# Criar uma nova coluna com o código da receita
df['NAT_REND'] = df['OBSERVACAO'].str.extract(r'\\(\d{5})')
# Se não quiser que apareça NaN digita preenche com espaço em branco
# df['NAT_REND'].fillna('', inplace=True)

# Defina uma função para converter corretamente o formato da string para float


def convert_to_float(value):
    if isinstance(value, str):  # Checa se o valor é uma string
        value = value.replace('.', '').replace(',', '.')
    return float(value)


# 55 Aplica a função convert_to_float e depois arredonda para duas casas decimais
df['DARF_BC'] = df['DARF_BC'].apply(
    convert_to_float).round(2).apply(lambda x: f"{x:.2f}")
df['DARF_VT'] = df['DARF_VT'].apply(
    convert_to_float).round(2).apply(lambda x: f"{x:.2f}")
df['REALIZADO'] = df['REALIZADO'].apply(
    convert_to_float).round(2).apply(lambda x: f"{x:.2f}")

# Corrige o CNPJ errado da EBC
df['CNPJ_EMIT'] = df['CNPJ_EMIT'].replace(115406, '09168704000142')
df['CNPJ_REC'] = df['CNPJ_REC'].replace(115406, '09168704000142')

# Agora ajusta todos os CNPJs para terem 14 dígitos
df['CNPJ_EMIT'] = df['CNPJ_EMIT'].astype(str).str.zfill(14)
df['CNPJ_REC'] = df['CNPJ_REC'].astype(str).str.zfill(14)
# Converte DARF COD E CNPJ EMIT para string
df['CNPJ_EMIT'] = df['CNPJ_EMIT'].astype(str)
df['DARF_COD'] = df['DARF_COD'].astype(str)


def preenche_nat_rend(row):
    if pd.isnull(row['NAT_REND']):  # Verifica se 'NAT_REND' está vazio
        if row['CNPJ_EMIT'] == '05340639000130' and row['DARF_COD'] == '8739':
            return '17013'
        elif row['CNPJ_EMIT'] == '05340639000130' and row['DARF_COD'] == '6147':
            return '17009'
        elif row['CNPJ_EMIT'] == '05340639000130' and row['DARF_COD'] == '6190':
            return '17099'
        elif row['CNPJ_EMIT'] == '37979739000105':
            return '17023'
        elif row['CNPJ_EMIT'] == '27729308000129' and row['DARF_COD'] == '6147':
            return '17001'
        elif row['CNPJ_EMIT'] == '16951665000110' and row['DARF_COD'] == '6190':
            return '17099'
        elif row['CNPJ_EMIT'] == '16951665000110' and row['DARF_COD'] == '6147':
            return '17009'
        elif row['CNPJ_EMIT'] == '07774050000175' and row['DARF_COD'] == '6190':
            return '17031'
        elif row['CNPJ_EMIT'] == '41116138000138' and row['DARF_COD'] == '6147':
            return '17099'
        elif row['CNPJ_EMIT'] == '12467682000126' and row['DARF_COD'] == '6147':
            return '17009'
        elif row['CNPJ_EMIT'] == '09168704000142' and row['DARF_COD'] == '6190':
            return '17099'
        elif row['CNPJ_EMIT'] == '09422042000195' and row['DARF_COD'] == '6190':
            return '17033'
        elif row['CNPJ_EMIT'] == '41106188000304' and row['DARF_COD'] == '6147':
            return '17001'
        elif row['CNPJ_EMIT'] == '06088039000199' and row['DARF_COD'] == '6147':
            return '17001'
        elif row['CNPJ_EMIT'] == '17086031000100' and row['DARF_COD'] == '6190':
            return '17032'
        elif row['CNPJ_EMIT'] == '40432544000147' and row['DARF_COD'] == '6190':
            return '17029'
        elif row['CNPJ_EMIT'] == '11533627000124' and row['DARF_COD'] == '6147':
            return '17003'
        elif row['CNPJ_EMIT'] == '27729308000129' and row['DARF_COD'] == '6147':
            return '17001'
        elif row['CNPJ_EMIT'] == '00449936000102' and row['DARF_COD'] == '6147':
            return '17032'
        elif row['CNPJ_EMIT'] == '18301321000191' and row['DARF_COD'] == '6190':
            return '17033'
        elif row['CNPJ_EMIT'] == '09445502000109' and row['DARF_COD'] == '6147':
            return '17032'
        elif row['CNPJ_EMIT'] == '21896864000103' and row['DARF_COD'] == '6147':
            return '17009'
        elif row['CNPJ_EMIT'] == '10835932000108' and row['DARF_COD'] == '6147':
            return '17002'
        elif row['CNPJ_EMIT'] == '01781573000162' and row['DARF_COD'] == '6190':
            return '17032'
        elif row['CNPJ_EMIT'] == '04427309000113' and row['DARF_COD'] == '6190':
            return '17032'
        elif row['CNPJ_EMIT'] == '04900474000140' and row['DARF_COD'] == '6190':
            return '17032'
        elif row['CNPJ_EMIT'] == '09769035000164' and row['DARF_COD'] == '6190':
            return '17028'
        elif row['CNPJ_EMIT'] == '24396327000192' and row['DARF_COD'] == '6147':
            return '17099'
        elif row['CNPJ_EMIT'] == '13653008000107' and row['DARF_COD'] == '6147':
            return '17009'
        elif row['CNPJ_EMIT'] == '12035234000153' and row['DARF_COD'] == '6190':
            return '17001'
        elif row['CNPJ_EMIT'] == '34028316002157' and row['DARF_COD'] == '6190':
            return '17030'
        elif row['CNPJ_EMIT'] == '07999951000165' and row['DARF_COD'] == '6147':
            return '17009'
        elif row['CNPJ_EMIT'] == '02604236000162' and row['DARF_COD'] == '6147':
            return '17009'
        elif row['CNPJ_EMIT'] == '12805036000121' and row['DARF_COD'] == '6147':
            return '17003'
        elif row['CNPJ_EMIT'] == '31731853000127' and row['DARF_COD'] == '6147':
            return '17009'
        elif row['CNPJ_EMIT'] == '65149197000251' and row['DARF_COD'] == '6147':
            return '17009'
        elif row['CNPJ_EMIT'] == '28820255000110' and row['DARF_COD'] == '8767':
            return '17008'
        elif row['CNPJ_EMIT'] == '07674744000130' and row['DARF_COD'] == '6190':
            return '17009'
        elif row['CNPJ_EMIT'] == '13938438000167' and row['DARF_COD'] == '6147':
            return '17099'
        # Você pode adicionar mais condições aqui conforme necessário
    # Retorna o valor atual se não estiver vazio ou se nenhuma condição for correspondida
    return row['NAT_REND']


# Aplica a função a cada linha do DataFrame
df['NAT_REND'] = df.apply(preenche_nat_rend, axis=1)

# Converte DARF_BC e DARF_VT para numérico (float)
df['DARF_BC'] = pd.to_numeric(df['DARF_BC'], errors='coerce')
df['DARF_VT'] = pd.to_numeric(df['DARF_VT'], errors='coerce')

# Agrupar por CNPJ_REC, DARF_COD, NAT_REND e somar DARF_BC e DARF_VT
df_agrupado = df.groupby(['CNPJ_REC', 'DARF_COD', 'NAT_REND']).agg(
    {'DARF_BC': 'sum', 'DARF_VT': 'sum'}).reset_index()
# 55 Aplica a função convert_to_float e depois arredonda para duas casas decimais
df_agrupado['DARF_BC'] = df_agrupado['DARF_BC'].apply(
    convert_to_float).round(2).apply(lambda x: f"{x:.2f}")
df_agrupado['DARF_VT'] = df_agrupado['DARF_VT'].apply(
    convert_to_float).round(2).apply(lambda x: f"{x:.2f}")
# salva o agrupado em excel
df_agrupado.to_excel('agrupado.xlsx', index=False)
# DataFrame onde a coluna 'NAT_REND' está vazia (é NaN)
df_vazio = df[df['NAT_REND'].isna()]
df_vazio.to_excel('preenchido.xlsx', index=False)
# DataFrame onde a coluna 'NAT_REND' está preenchida:
df = df.dropna(subset=['NAT_REND'])
# Imprime no excel
df.to_excel('preenchido.xlsx', index=False)
time.sleep(30)

# Itera pelas linhas do DataFrame
for index, row in df_agrupado.iloc[9:].iterrows():
    # Preenche os campos da primeira página
    # Use pyautogui para mover o mouse e clicar no menu suspenso para iniciar o r4000
    r.click(1634, 939)
    pyautogui.press('home')
    r.click('primeiroclick.png')
    r.wait(1)
    r.click('segundoclick.png')
    r.click('casinha.png')
    r.wait()

    # primeira página com informações gerais
    r.click('periododeapuracao.png')
    pyautogui.write('112023')
    pyautogui.press('tab')
    pyautogui.write('24134488000108', interval=0.1)
    pyautogui.press('tab')
    cnpj_rec = str(row['CNPJ_REC'])  # CNPJ do recolhedor converter em string
    # digita cnpj do recolhedor devagar
    pyautogui.write(cnpj_rec, interval=0.1)
    # pyautogui.press('tab')
    r.click('identificador.png')
    num_ordem = index + 1  # digitar um número de ordem
    num_ordem = str(num_ordem)
    pyautogui.write(num_ordem, interval=0.1)
    r.click('continuar.png')
    # segunda página, natureza do rendimento pago, clicar em incluir nova
    r.wait(1)
    r.click('incluirnova.png')
    r.wait(1)
    r.click(444, 581)
    pyautogui.press('down', presses=7)
    pyautogui.press('enter')
    pyautogui.press('tab')
    nat_rend = str(row['NAT_REND'])  # COLUNA COM A NATUREZA DO RENDIMENTO
    pyautogui.typewrite(nat_rend, interval=0.1)
    pyautogui.press(['tab', 'tab', 'enter'])
    # Terceira página: Detalhamento dos pagamentos ou créditos, clicar incluir novo
    r.click('incluirnovo.png')
    r.wait(1)
    r.click('datadofatogerador.png')
    pyautogui.write('30112023')
    pyautogui.press('tab')
    darf_bc = str(row['DARF_BC'])  # VALOR DA BASE DE CÁLCULO
    pyautogui.write(darf_bc, interval=0.1)
    pyautogui.press('tab')
    pyautogui.write('n')
    pyautogui.press(['tab', 'tab', 'tab'])
    obser = ' '  # VALOR DA OBSERVAÇÃO
    pyautogui.write(obser)
    pyautogui.press(['tab', 'tab', 'tab'])
    pyautogui.write(darf_bc, interval=0.1)
    pyautogui.press('tab')
    darf_vt = str(row['DARF_VT'])  # VALOR DO DARF
    pyautogui.write(darf_vt, interval=0.1)
    pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'enter'])
    # Pagina de finalização - salvar rascunho
    r.click(1470, 776)
    pyautogui.press('end')
    r.click('concluirenviar.png')
    r.wait(2)
    r.click('assinatura.png')
    r.click('selecionar.png')
    r.wait(5)
    # r.click('senha.png')
    # pyautogui.write('1234', interval=0.05)
    # r.click('oksenha.png')


r.close()  # Fecha a sessão RPA
