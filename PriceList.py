from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Criar o navegador
service = Service(GeckoDriverManager().install())
nav = webdriver.Firefox(service=service)

# Entrar no site
nav.get('https://telefonesimportados.netlify.app/')

# Varrer preços e botar em uma lista
lista = []

for j in range(0,5):

    for i in range(1,13):

        name = nav.find_element('xpath', f'/html/body/div[5]/div[2]/div[1]/div[{i}]/div/h2/a').text
        price = nav.find_element('xpath', f'/html/body/div[5]/div[2]/div[1]/div[{i}]/div/div[2]/ins').text
        NameAndPrice = name + "," + price

        lista.append(NameAndPrice)
    
    if (j != 4):
        nav.find_element('xpath', '/html/body/div[5]/div[2]/div[2]/div/div/nav/ul/li[7]/a/span').click()
        time.sleep(2)

# Criar arquivo .csv e inserir a lista
path = "C:\\Users\\Vitor\\Downloads\\Estudo\\Python\\Projetos\\PriceList\\PriceList.csv"

with open(path, "w", encoding="UTF-8") as file:
    for i in range (0, len(lista)):
        file.write(lista[i] + "\n")

# Mostrar lista na tela
print(lista)