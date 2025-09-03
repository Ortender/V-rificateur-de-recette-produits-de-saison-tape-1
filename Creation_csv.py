import csv

#Cette fonction permet de créer les fichiers CV des choix 3 et 4 du menu utilisateur
def create_csv_calendar(Calendar, column1, column2):
    fieldnames=[column1, column2]
    with open('Calendrier.csv', 'w', newline='') as calendrier_csv:
        writer = csv.DictWriter(calendrier_csv, fieldnames=fieldnames)
        writer.writeheader()
        for ingredient in Calendar:
            writer.writerow(ingredient)
    print('Votre fichier Calendrier.csv a été créé.')