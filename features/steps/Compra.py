from behave import given, when, then
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#precisa sempre importar a classe environment (onde estão o Antes e o Depois do Teste)
from features import environment

# Método Executado antes da feature e serve para chamar os passos seguintes
def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(
            # pode ser incluidas outras ações
        )

@given(u'que acesso o site Blazedemo')
def step_impl(context):
    context.driver.get('https://blazedemo.com')
    print('Passo 1 - Acessou o site Blazedemo')

@when(u'seleciono a cidade de origem como "{origem}"')
def step_impl(context, origem):

    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'fromPort')

    # Criar um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(origem)
    # objeto_origem.select_by_value(origem)

    print('Passo 2 - Selecionou a cidade de origem')

@when(u'seleciono a cidade de destino como "{destino}"')
def step_impl(context, destino):

    # Mapeia o combo com as cidades de origem
    combo_origem = context.driver.find_element(By.NAME, 'toPort')

    # Criar um objeto para permitir selecionar as opções do combo
    objeto_origem = Select(combo_origem)

    # Seleciona o elemento no combo
    objeto_origem.select_by_visible_text(destino)
    # objeto_origem.select_by_value(origem)

    print('Passo 3 - Selecionou a cidade de destino')


@when(u'clico no botao Find Flights')
def step_impl(context):

    print('Passo 4 - Clicou no botão Find Flights')


@then(u'sou direcionado para a pagina de selecao de voos')
def step_impl(context):

    print('Passo 5 - Direcionou para a página de seleção de vôos')


@when(u'seleciono o primeiro voo')
def step_impl(context):

    print('Passo 6 - Selecionou o primeiro vôo')


@then(u'sou direcionado para a pagina de pagamento')
def step_impl(context):

    print('Passo 7 - Direcionou para a página de pagamento')


@when(u'preencho os dados para pagamento')
def step_impl(context):

    print('Passo 8 - Preencheu os dados para o pagamento')


@when(u'clico no botao Purchase Flight')
def step_impl(context):

    print('Passo 9 - Clicou no botão Purchase Flights')


@then(u'sou direcionado para a pagina de confirmacao')
def step_impl(context):
    print('Passo 10 - Direcionou para a página de confirmação')


@when(u'seleciono de "São Paolo" para "Rome"')
def step_impl(context):

    print('Passo 2c - Selecionou a cidade de origem e destino')
