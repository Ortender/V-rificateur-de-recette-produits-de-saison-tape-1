import csv

#Cette fonction permet de créer les fichiers CV des choix 3 et 4 du menu utilisateur
def create_csv_calendar(calendar, column1, column2):
    fieldnames=[column1, column2]
    with open('Calendrier.csv', 'w', newline='') as calendar_csv:
        writer = csv.DictWriter(calendar_csv, fieldnames=fieldnames)
        writer.writeheader()
        for ingredient in calendar:
            writer.writerow(ingredient)
    print('Votre fichier Calendrier.csv a été créé.')