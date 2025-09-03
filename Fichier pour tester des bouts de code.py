#Ce fichier me permet simplement de faire des tests de mes bouts de code pour m'assurer qu'ils se comportent comme je le souhaite

import requests
from bs4 import BeautifulSoup

url = "https://www.greenpeace.fr/guetteur/calendrier/"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, 'html.parser')

Calendar =[]
    #le calendrier dans la page html est organisé par article, nous parcourons chacun de ces articles
for month_and_ingredient in soup.find_all('article', class_='list-items'):
    #comme le mois n'est pas inclus dans l'article, nous devons retrouver le mois en consultant le anchor contenant le mois, précédent l'article des ingrédients
    month = month_and_ingredient.find_previous('a', class_='anchor').get('name')
    #nous parcourons chaque ingrédient de l'article pour en extraire le nom et le stocker dans un dictionnaire avec le mois correspondant
    for ingredient in month_and_ingredient.find_all('li'):
        couple_Month_ingredient = {}
        ingredient_clean = ingredient.string
        couple_Month_ingredient['Ingrédient']=ingredient_clean.strip('\n\t\t\t\t')
        couple_Month_ingredient['Mois']=(month)
        Calendar.append(couple_Month_ingredient)

recipe_clean=['Brocoli','Carotte','Potiron']
List_of_month=[]
for ingredient in recipe_clean:
    ingredient_month=[]
    for couple in Calendar:
        if ingredient == couple["Ingrédient"]:
            ingredient_month.append(couple["Mois"])
    List_of_month.append(ingredient_month)
Valid_month=set(List_of_month[0]).intersection(*List_of_month)
print(Valid_month)
'''fieldnames=['Ingrédient', 'Mois']
with open('Calendrier.csv', 'w', newline='') as calendrier_csv:
    writer = csv.DictWriter(calendrier_csv, fieldnames=fieldnames)
    writer.writeheader()
    for ingredient in Calendar:
        writer.writerow(ingredient)'''

'''list_ingredient = []
for ingredient in Calendar:
    if ingredient['Ingrédient'] not in list_ingredient:
        list_ingredient.append(ingredient['Ingrédient'])
    else:
        continue
user_recipe = input('Veuillez fournir la liste de vos ingrédients séparés par une virgule et sans espace (exemple: Potiron,Carotte,Brocoli) ')
recipe = user_recipe.split(',')
recipe_clean=[]
for ingredient in recipe:
    while ingredient not in list_ingredient:
        print(f"\033[31m{ingredient} n'est pas reconnu comme un ingrédient valide, veuillez l'écrire correctement.\033[0m")
        Display_list=input("Voulez-vous voir la liste des ingrédients valide?\n Tapez 'oui' ou 'non': \n")
        if Display_list == "oui":
            for i in list_ingredient:
                print(i)
            ingredient_not_found=input("Avez-vous trouvé votre ingrédient dans la liste?\n Tapez 'oui' ou 'non': \n")
            if ingredient_not_found == "non":
                print("Votre ingrédient ne fait pas partie des aliments considérés dans le calendrier de GreenPeace.\n Veuillez vous référer au site GreenPeace pour plus d'information.")
                break
        ingredient = input("Votre ingrédient: ")
    if ingredient in list_ingredient:
        recipe_clean.append(ingredient)
print(recipe_clean)
if set(recipe).issubset(list_ingredient):
    print('yes')
else:
    print('no')'''
'''user_recipe = input('Veuillez fournir la liste de vos ingrédients séparés par une virgule (exemple: Potiron, Carotte, Brocoli) ')
recipe = user_recipe.split(',')
while not set(recipe).issubset(list_ingredient):
    for ingredient in recipe:
        if set(ingredient).issubset(list_ingredient):
            continue
        else:
            ingredient = input(f"{ingredient} n'est pas reconnu comme un ingrédient de la liste, veuillez le récrire correctement.")
            break
print(recipe)
en_tete = ["ingrédient"]
with open('liste ingrédient.csv', 'w', newline='') as liste_ingredient_csv:
    writer=csv.writer(liste_ingredient_csv, delimiter=',')
    writer.writerow(en_tete)
    for ingredient in zip(list_ingredient):
        writer.writerow(ingredient)'''

'''url = "https://www.greenpeace.fr/guetteur/calendrier/"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, 'html.parser')

dico = []
for month_ingredient in soup.find_all('article'):
    try:
        month = month_ingredient.find_previous('a', class_='anchor').get('name')
    except:
        month = month_ingredient.find_previous_sibling('a', class_='anchor-item').get('name')
    print(month)
    for ingredient in month_ingredient.find_all('li'):
        ingredient_clean = ingredient.string
        dico.append(ingredient_clean.strip('\n\t\t\t\t'))
    
test = get_calendar(page_element)
print(test)'''


