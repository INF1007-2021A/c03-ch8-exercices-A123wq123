#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici




# TODO: Définissez vos fonction ici
def comparateur_de_deux_fichiers(fichier_1, fichier_2):
    with open(fichier_1, "r") as f1:
        f1_read = f1.read()

    with open(fichier_2, "r") as f2:
        f2_read = f2.read()

    for i, y in zip(f1_read, f2_read):

        if i != y:
            return (f"Première différence rencontrée: {i} et {y}")

    return("Aucune différence encontrée")

def recopiage(fichier):

    with open(fichier, "r") as f1:
        f1_read = f1.read()

    with open("fichier_copie_espaces", "a") as f2:

        for character in f1_read:

            if character == " ":
                f2.write("   ")
            else:
                f2.write(character)

        return f2







if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
