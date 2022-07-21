from selenium import webdriver

#Inicio
def before_all(context):       #Antes de Tudo

    #Declarar o Selenium, iniciar como navegador e apontar driver
    context.driver = webdriver.Chrome('C:/Users/emili/PycharmProjects/fts132_blazedemo/drivers/chrome/chromedriver.exe')

    #Maximizar a janela do navegador
    context.driver.maximize_window()

    print('Passo A - Antes de Tudo')

#Fim
def after_all(context):        #Depois de Tudo

    #Desligar / Destruir o objeto do Selenium
    context.driver.quit()

    print('Passo Z - Depois de Tudo')