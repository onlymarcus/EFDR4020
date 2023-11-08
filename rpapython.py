import tagui as t
import rpa as r
import openpyxl
import time
import pyautogui


# Inicializa o navegador RPA
r.init(visual_automation=True)
r.url('https://cav.receita.fazenda.gov.br/autenticacao/')
#r.url()



# Abre o arquivo Excel
workbook = openpyxl.load_workbook('r4000.xlsx')
sheet = workbook['Planilha1']
time.sleep(30)

# Define o número máximo de linhas a serem processadas (100 no exemplo)
numero_maximo_linhas = 3

# Define o caminho XPath para cada elemento que você precisa interagir
elementos_xpath = {
    'periodo_apuracao': '//*[@id="periodo_apuracao"]',
    'cnpj_empresa': '//*[@id="num_inscricao_estab"]',
    'cnpj_beneficiario': '//*[@id="cnpj_beneficiario"]',
    'botao_confirmar': 'botao_continuar',
    'botao_incluir_nova': '/html/body/app-root/div/div[3]/app-evento4020-formulario/app-reinf-versao-leiaute/form/fieldset[2]/app-reinf-linha-titulo-inclusao/div/div/div/span',
    'grupo_rendimento': '//*[@id="grupo_rendimento"]',
    'natureza_do_rendimento': '//*[@id="natureza_do_rendimento"]',
    'botao_salvar': '/html/body/app-root/div/div[3]/app-evento4020-formulario/app-evento4020-modal-ide-pgto/app-reinf-versao-leiaute/app-reinf-modal/div/div/div[3]/div/button[1]',
    'botao_incluir_novo': '/html/body/app-root/div/div[3]/app-evento4020-formulario/app-reinf-versao-leiaute/form/fieldset[2]/div/app-reinf-collapse/details/div/app-reinf-linha-titulo-inclusao/div/div/div/span',
    'data_do_fato_gerador': '//*[@id="data_do_fato_gerador"]',
    'valor_bruto': '//*[@id="valor_bruto"]',
    'ind_rendimento_decisao_judicial': '//*[@id="ind_rendimento_decisao_judicial"]',
    'vlr_base_agregada': '//*[@id="vlr_base_agregada"]',
    'valor_agregado': '//*[@id="valor_agregado"]',
    'botao_salvar_modal': '/html/body/app-root/div/div[3]/app-evento4020-formulario/app-evento4020-modal-info-pgto/app-reinf-versao-leiaute/app-reinf-modal/div/div/div[3]/div/button[1]',
    'botao_salvar_rascunho': '/html/body/app-root/div/div[3]/app-evento4020-formulario/app-reinf-versao-leiaute/form/app-reinf-botoes-formulario/div/div/button[1]',
    'menu_rendimentos_pagos': '/html/body/app-root/div/div[2]/div/app-reinf-menu/div/ul/li[3]/a',
    'opcao_menu_rendimentos_pagos': '/html/body/app-root/div/div[2]/div/app-reinf-menu/div/ul/li[3]/ul/li[1]/a',
    'botao_r4020': '/html/body/app-root/div/div[3]/app-periodicos4000-inclusao/fieldset/div/div[2]/p[1]'
}

pyautogui.moveTo(x=644, y=357)
time.sleep(1)
pyautogui.moveTo(x=640, y=382)
pyautogui.click(x=640, y=382)
pyautogui.moveTo(x=732, y=513)
pyautogui.click(x=732, y=513)
time.sleep(2)
r.wait()

#pyautogui.click(166,618)
r.type(166,618,'092023')
r.type(509,617, '24134488000108')
r.click(759,618)
r.wait(1)
r.click(759,618)

# r.init()
# r.url('https://duckduckgo.com/')
# r.type('//*[@id="searchbox_input"]', 'decentralisation[enter]')
# r.wait() # ensure results are fully loaded
# r.snap('page', 'results.png')
# r.close()

