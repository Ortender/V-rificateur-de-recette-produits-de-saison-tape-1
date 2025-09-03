import Extraction_Calendrier_et_ingredients
import user_interaction
import Realisation_des_actions

if __name__ == '__main__':
    #Nous fournissons l'url permettant de récupérer la "base de données" du calendrier de saisonalité des ingrédients
    url = "https://www.greenpeace.fr/guetteur/calendrier/"
    page = Extraction_Calendrier_et_ingredients.get_html_code(url)
    #Nous récupérons les données et les rangeons au format désiré
    Calendar = Extraction_Calendrier_et_ingredients.get_calendar(page)
    #On extrait la liste des ingrédients présent dans la BD
    list_ingredient = Extraction_Calendrier_et_ingredients.get_ingredient(Calendar)

    user_interaction.welcome_message()
    #Nous affichons les menu de choix à l'utilisateur
    user_choice=user_interaction.menu()
    #En fonction du choix de l'utilisateur nous réalisons l'action désirée
    Realisation_des_actions.Action_user_choice(user_choice, Calendar, list_ingredient)