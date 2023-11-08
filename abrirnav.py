from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import openpyxl
import time
import pyautogui

# Inicializa o navegador Selenium
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 60 )


# Abre o arquivo Excel
workbook = openpyxl.load_workbook('r4000.xlsx')
sheet = workbook['Planilha1']

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

# Itera pelas linhas da planilha
for linha in range(4, numero_maximo_linhas + 4):  # Assumindo que os dados começam na linha 4
    # Preenche os campos da primeira página
    
    driver.get('https://cav.receita.fazenda.gov.br/autenticacao/')
    driver.implicitly_wait(30)
    time.sleep(40)