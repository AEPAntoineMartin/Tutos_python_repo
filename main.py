from config import *
from functions import *

def main():
    for index, name in enumerate(clients):
        date_naissance_string = clients[name]
        age = calcul_age(date_naissance_string)

        if verif_age(age):
            print(f"{name} ne peut pas entrer. La personne a {age.years} ans.")
        else:
            print(f"{name} peut entrer. La personne a {age.years} ans.")

if __name__ == "__main__":
    main()