import requests
from bs4 import BeautifulSoup

#fonction permettant de récupérer le code de la page html de greenpeace contenant le calendrier 
def get_html_code(url):
    reponse = requests.get(url)
    page = reponse.content
    soup = BeautifulSoup(page, 'html.parser')
    return soup

#fonction permettant d'extraire du code html le calendrier
def get_calendar(page_element):
    #le calendrier sera contenu dans une liste de dictionnaire (ingrédients, mois)
    Calendar =[]
    #le calendrier dans la page html est organisé par article, nous parcourons chacun de ces articles
    for month_and_ingredient in page_element.find_all('article', class_='list-items'):
        #comme le mois n'est pas inclus dans l'article, nous devons retrouver le mois en consultant le anchor contenant le mois, précédent l'article des ingrédients
        month = month_and_ingredient.find_previous('a', class_='anchor').get('name')
        #nous parcourons chaque ingrédient de l'article pour en extraire le nom
        for ingredient in month_and_ingredient.find_all('li'):
            couple_Month_ingredient = {}
            ingredient_clean = ingredient.string
            #la fonction .string renvoie le nom de l'ingrédient mais pollué de \n et \t que nous devons retirer
            couple_Month_ingredient['Ingrédient']=ingredient_clean.strip('\n\t\t\t\t')
            couple_Month_ingredient['Mois']=(month)
            Calendar.append(couple_Month_ingredient)
    return Calendar

#fonction pour récupérer la liste de tous les ingrédients présents dans le calendrier
def get_ingredient(calendar):
    list_ingredient=[]
    for ingredient in calendar:
        if ingredient['Ingrédient'] not in list_ingredient:
            list_ingredient.append(ingredient['Ingrédient'])
        else:
            continue
    return list_ingredient

#fonction pour afficher la liste de tous les ingrédients présents dans le calendrier
def display_ingredient_list(list_ingredient):
    for ingredient in list_ingredient:
        print(ingredient)