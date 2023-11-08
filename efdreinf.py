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
driver = webdriver.Chrome()
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

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable
    )
    # Use pyautogui para mover o mouse e clicar
    pyautogui.moveTo(x=644, y=411)
    pyautogui.moveTo(x=647, y=439)
    pyautogui.click(x=647, y=439)
    pyautogui.moveTo(x=730, y=570)
    pyautogui.click(x=730, y=570)
    time.sleep(2)
    #driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(2));
    #driver.find_element(By.CLASS_NAME, "w4 required textbox ng-pristine ng-invalid ng-touched").send_keys('092023')
    ng = driver.find_element(By.CLASS_NAME, 'ng-touched').send_keys('092023')
    ng.send_keys(Keys.TAB)
    

    driver.find_element(By.XPATH, '//*[@id="num_inscricao_estab"]').send_keys('24134488000108')
    driver.find_element(By.XPATH, '//*[@id="cnpj_beneficiario"]').send_keys(sheet[f'C{linha}'].value)
    driver.find_element(By.XPATH, '/html/body/app-root/div/div[3]/app-evento4020-formulario/app-reinf-versao-leiaute/app-evento4020-inclusao-chave/form/div[2]/button[1]').click()

    # Aguarde algum tempo (opcional) para a página responder antes de continuar
    time.sleep(5)

    # Clica em 'incluir nova'
    driver.find_element(By.XPATH, elementos_xpath['botao_incluir_nova']).click()

    # Preenche os campos da segunda página
    driver.find_element(By.XPATH, elementos_xpath['grupo_rendimento']).send_keys('17')
    driver.find_element(By.XPATH, elementos_xpath['natureza_do_rendimento']).send_keys(sheet[f'P{linha}'].value)
    driver.find_element(By.XPATH, elementos_xpath['botao_salvar']).click()

    # Aguarde algum tempo (opcional) para a página responder antes de continuar
    time.sleep(3)

    # Clica em 'incluir novo'
    driver.find_element(By.XPATH, elementos_xpath['botao_incluir_novo']).click()

    # Preenche os campos da terceira página
    driver.find_element(By.XPATH, elementos_xpath['data_do_fato_gerador']).send_keys(sheet[f'E{linha}'].value)
    driver.find_element(By.XPATH, elementos_xpath['valor_bruto']).send_keys(sheet[f'J{linha}'].value)
    driver.find_element(By.XPATH, elementos_xpath['ind_rendimento_decisao_judicial']).send_keys('N')
    driver.find_element(By.XPATH, elementos_xpath['vlr_base_agregada']).send_keys(sheet[f'J{linha}'].value)
    driver.find_element(By.XPATH, elementos_xpath['valor_agregado']).send_keys(sheet[f'O{linha}'].value)
    driver.find_element(By.XPATH, elementos_xpath['botao_salvar_modal']).click()
    driver.find_element(By.XPATH, elementos_xpath['botao_salvar_rascunho']).click()

    # Use pyautogui para mover o mouse e clicar
    # pyautogui.moveTo(x=644, y=411)
    # pyautogui.moveTo(x=647, y=439)
    # pyautogui.click(x=647, y=439)
    # pyautogui.moveTo(x=730, y=570)
    # pyautogui.click(x=730, y=570)

    # Ações para a próxima iteração (menu, botão, etc.)
    #driver.find_element(By.CSS_SELECTOR, "#nav > li:nth-child(3) > ul > li:nth-child(1) > a").click()
    #driver.find_element(By.CLASS_NAME, "icone-4020").click()
    

# Fecha o navegador e o arquivo Excel
driver.quit()
workbook.close()
