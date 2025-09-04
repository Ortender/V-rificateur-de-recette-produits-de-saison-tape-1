import requests
from bs4 import BeautifulSoup

class Season:
  def __init__(self, ingredient, month):
    self.ingredient = ingredient
    self.month = month

#fonction permettant de récupérer le code de la page html de greenpeace contenant le calendrier 
def get_html_code(url):
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, 'html.parser')
    return soup

#fonction permettant d'extraire du code html le calendrier
def get_calendar(page_element):
    #le calendrier sera contenu dans une liste de dictionnaire (ingrédients, mois)
    calendar =[]
    #le calendrier dans la page html est organisé par article, nous parcourons chacun de ces articles
    for month_and_ingredient in page_element.find_all('article', class_='list-items'):
        #comme le mois n'est pas inclus dans l'article, nous devons retrouver le mois en consultant le anchor contenant le mois, précédent l'article des ingrédients
        month = month_and_ingredient.find_previous('a', class_='anchor').get('name')
        #nous parcourons chaque ingrédient de l'article pour en extraire le nom
        for ingredient in month_and_ingredient.find_all('li'):
            ingredient_clean = ingredient.string
            #la fonction .string renvoie le nom de l'ingrédient mais pollué de \n et \t que nous devons retirer
            ingredient_string=ingredient_clean.strip('\n\t\t\t\t')
            calendar.append(Season(ingredient_string.casefold(),month))
    return calendar

#fonction pour récupérer la liste de tous les ingrédients présents dans le calendrier
def get_ingredient(calendar):
    list_ingredient=[]
    for ingredient in calendar:
        if ingredient.ingredient not in list_ingredient:
            list_ingredient.append(ingredient.ingredient)
        else:
            continue
    return list_ingredient

#fonction pour afficher la liste de tous les ingrédients présents dans le calendrier
def display_ingredient_list(list_ingredient):
    for ingredient in list_ingredient:
        print(ingredient)

def class_to_dict(calendar, column1, column2):
    calendar_dict=[]
    for ingredient in calendar:
        dictionary={}
        dictionary[column1]=ingredient.ingredient
        dictionary[column2]=ingredient.month
        calendar_dict.append(dictionary)
    return calendar_dict