#! python3
'''TESTE PARA ESPERAR O SIAFI'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime
import pyautogui
import pynput
from pynput.mouse import Button, Controller
mouse = Controller()


    
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 60 )
type(browser)
browser.get('https://siafi.tesouro.gov.br/senha/public/pages/security/login.jsf')

def inicio():

    time.sleep(2)
    '''Entra no sistema e dá alguns segundos para login e ug'''
    #concor = browser.find_element_by_id('frmTemplateAcesso:btnConcordar')
    #concor.send_keys(Keys.ENTER)'''Clicar em concordar'''

    #print('Para pagamentos no SIAFI, por favor digite quantos segundos vamos esperar entre uma tela e outra:  ')
    #segundos = input()
    '''while True é usado por mim para pagamentos. Para agendamentos é for in range'''
    print('Favor digite quantos segundos o sistema deve esperar entre as telas: ')
    segundos = input()
    print('Favor digite quantos segundos o sistema deve esperar ao digitar a vinculação 400: ')
    segundosv = input()
    print('A partir de qual página você quer pagar? digite um número: ')
    paginap = input()
    print('Favor digitar o número do Documento de Origem: ')
    docorigem = input(str())
    print('Favor digitar a data inicial dos pagamentos:')
    dataInicial = input(str())
    print('Favor digitar a data final dos pagamentos:')
    dataFinal = input(str())


    def pagar():
        while True:
            rp = wait.until(EC.presence_of_element_located((By.ID, 'formComp:tipoDocHabil_input')))
            rp = browser.find_element_by_id('formComp:tipoDocHabil_input')
            rp.send_keys('RP')#insere o tipo RP

            #mouse.position = (200, 686)#mouse sobre o calendario (de)
            #mouse.click(Button.left, 1)#click no calendario
            #mouse.position = (130, 714)#mouse para voltar um mês
            #mouse.click(Button.left, 1)#click para voltar um mês
            #mouse.position = (150, 783)#mouse sobre o dia 30/05
            #mouse.click(Button.left, 1)#click no 1 dia do mês
            

            #mouse.position = (330, 686)#mouse sobre o calendario (para)
            #mouse.click(Button.left, 1)#click no calendario
            #mouse.position = (360, 714)#mouse para ADIANTAR um mês
            #mouse.click(Button.left, 2)#click dupolo para adiantar dois meses
            #mouse.position = (360, 830)#mouse sobre o dia 30 do mes corrente, Março.
            #mouse.click(Button.left, 1)#click no 1 dia do mês

            
            #insere a data inicial escolhida no começo do script
            dataini = browser.find_element(By.XPATH, '//*[@id="formComp:dataInicialPagamento_calendarInputDate"]')
            dataini.clear()
            dataini.click()
            dataini.send_keys(dataInicial)
            #insere a data final escolhida no começo do script
            datafin = browser.find_element(By.XPATH, '//*[@id="formComp:dataFinalPagamento_calendarInputDate"]')
            datafin.clear()
            datafin.click()
            datafin.send_keys(dataFinal)

            docor = browser.find_element_by_id('formComp:numeroDocOrigem_input')
            docor.send_keys(str(docorigem)) #OPÇÃO DE INCLUIR O NÚMERO DO DOCUMENTO DE ORIGEM \O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/
            
            htmlElem = browser.find_element_by_tag_name('html')
            htmlElem.send_keys(Keys.END)#Dá um scrollroll na página
            
            enterElem = browser.find_element_by_id('formComp:botao_pesquisar')
            enterElem.send_keys(Keys.ENTER)#Procura o botão pesquisar e clica nele
            time.sleep(int(segundos))
            
            """**********ATÉ AQUI FOI PARA INSERIR OS PARÂMETROS DA PESQUISA DO GERCOMP*******"""

            try:
                pagina = wait.until(EC.presence_of_element_located((By.ID, 'formComp:seletorPaginaSuperior_input')))#espera que o elemento apareça (ate 20seg)
                pagina = browser.find_element_by_id('formComp:seletorPaginaSuperior_input')
                pagina.send_keys(int(paginap))#OPÇÃO DE MUDAR O NÚMERO DA PÁGINA \O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/
                pagina.send_keys(Keys.ENTER)
            except:
                time.sleep(6)
                pagina = wait.until(EC.presence_of_element_located((By.ID, 'formComp:seletorPaginaSuperior_input')))#espera que o elemento apareça (ate 20seg)
                pagina = browser.find_element_by_id('formComp:seletorPaginaSuperior_input')
                pagina.send_keys(int(paginap))#OPÇÃO DE MUDAR O NÚMERO DA PÁGINA \O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/\O/
                pagina.send_keys(Keys.ENTER)
                
            
            #elemento11 = wait.until(EC.element_to_be_clickable((By.ID, 'formComp:tabelaPesquisarCompromissos:marcaTodas')))
            try:
                elemento11 = browser.find_element_by_id('formComp:tabelaResultadoPesquisa:marcaTodas').click()
                #mouse.position = (121, 278)#levar o mouse até a posição DEPENDENDO SE A PÁGINA FOR A ÚLTIMA PODE VARIAR
                #mouse.click(Button.left, 1)#clicar em selecionar todas
                elemento12 = wait.until(EC.element_to_be_clickable((By.ID, 'formComp:botao_marcar_opcao_realizacao')))
                time.sleep(int(segundos))
            except:
                time.sleep(6)
                elemento11 = browser.find_element_by_id('formComp:tabelaResultadoPesquisa:marcaTodas').click()
                #mouse.position = (121, 278)#levar o mouse até a posição DEPENDENDO SE A PÁGINA FOR A ÚLTIMA PODE VARIAR
                #mouse.click(Button.left, 1)#clicar em selecionar todas
                elemento12 = wait.until(EC.element_to_be_clickable((By.ID, 'formComp:botao_marcar_opcao_realizacao')))
                time.sleep(int(segundos))
                
            htmlElem = browser.find_element_by_tag_name('html')
            htmlElem.send_keys(Keys.END)#leva a página para o final

            enterElem2 = browser.find_element_by_id('formComp:botao_marcar_opcao_realizacao')
            enterElem2.send_keys(Keys.ENTER)#selecionar a opção de realização de compromisso
                 
            enterElem3 = wait.until(EC.presence_of_element_located((By.ID, 'formComp:opcaoRealizacao')))#espera que o elemento apareça (ate 20seg)
            enterElem3 = browser.find_element_by_id('formComp:opcaoRealizacao')
            enterElem3.send_keys('r')#selecionar o tipo de realização, (que pode ser agendamento, ou realizar totalmente) AGENDANDO<<<<<<
            time.sleep(1)
            
            enterElem3 = browser.find_element_by_id('formComp:buttonConfirmar')
            enterElem3.send_keys(Keys.ENTER)#confirma
            time.sleep(int(segundos))
            htmlElem = browser.find_element_by_tag_name('html')
            htmlElem.send_keys(Keys.END)#levar para o final da página
            
            try:
                enterElem4 = browser.find_element_by_id('formComp:botao_executar')
                enterElem4.send_keys(Keys.ENTER)#executar o pagamento
                vinc = wait.until(EC.presence_of_element_located((By.ID, 'formComp:repeatCompromissoLista:0:tableRealizacao:0:subtableVinculacoes:0:vinculacao_input')))
                vinc = browser.find_element_by_id('formComp:repeatCompromissoLista:0:tableRealizacao:0:subtableVinculacoes:0:vinculacao_input')
            except Exception as e:
                    time.sleep(5)  
                
            
            #a partir de agora vai digitar a vinculação e pagar
            while (browser.find_element_by_id('formComp:repeatCompromissoLista:0:tableRealizacao:0:subtableVinculacoes:0:vinculacao_input')):

                try:
                    vinc = wait.until(EC.presence_of_element_located((By.ID, 'formComp:repeatCompromissoLista:0:tableRealizacao:0:subtableVinculacoes:0:vinculacao_input')))
                    vinc = browser.find_element_by_id('formComp:repeatCompromissoLista:0:tableRealizacao:0:subtableVinculacoes:0:vinculacao_input')
                    vinc.send_keys('400')
                    enterElem5 = wait.until(EC.element_to_be_clickable((By.ID, 'formComp:buttonConfirmar')))
                    enterElem5 = browser.find_element_by_id('formComp:buttonConfirmar')
                    enterElem5.send_keys(Keys.ENTER)
                    time.sleep(int(segundosv))
                    if (len(browser.find_elements_by_id('formComp:buttonRetornar'))>0):
                        break
                    else:
                        continue
                except Exception as e:
                    time.sleep(5)
                
                
            enterElem6 = wait.until(EC.presence_of_element_located((By.ID, 'formComp:buttonRetornar')))
            enterElem6 = wait.until(EC.element_to_be_clickable((By.ID, 'formComp:buttonRetornar')))
            enterElem6 = browser.find_element_by_id('formComp:buttonRetornar')
            enterElem6.send_keys(Keys.ENTER)#Retornar para a página inicial do gercomp
            rp = wait.until(EC.presence_of_element_located((By.ID, 'formComp:tipoDocHabil_input')))#esperar o campo dochabil aparecer para reiniciar o loop
            time.sleep(int(segundos))


            """
            NESTA VERSÃO INCLUÍ A FERRAMENTA DO SELENIUM QUE AGUARDA OS ELEMENTOS SEREM CARREGADOS NA PÁGINA ANTES DE CLICAR.
            NO INÍCIO ESTABELECEMOS O TEMPO MÁXIMO QUE ELE ESPERA O ELEMENTO APARECER, QUE É DE 20 SEGUNDOS.
            Hoje, 04/04/18, incluí try except em alguns cliques e clicar no checkbox "marcar todas".

            """
    pagar()

inicio()
