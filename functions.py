# import
from datetime import datetime
from dateutil.relativedelta import relativedelta

# fonctions
def calcul_age(date_naissance_string):
    """Calcule la différence précise entre aujourd'hui et une date de naissance.

    Cette fonction prend une date de naissance au format chaîne de caractères
    ("JJ/MM/AAAA"), la convertit en objet datetime, et calcule la différence
    exacte en années, mois et jours par rapport à la date actuelle en utilisant
    relativedelta.

    Args:
        date_naissance_string (str): La date de naissance au format "JJ/MM/AAAA".

    Returns:
        relativedelta: Un objet relativedelta représentant l'âge, avec des
                       attributs comme .years, .months, et .days.
    """
    aujourdhui = datetime.today()
    date_naissance = datetime.strptime(date_naissance_string, "%d/%m/%Y")
    age = relativedelta(aujourdhui, date_naissance)
    return age

def verif_age(age: datetime):
    return age.years < 18