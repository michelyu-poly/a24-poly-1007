# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
"""
formatage des string pris du module test_tp1, via github @polymtl 2024
"""
water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? "))
# print("Voici les matériaux requis pour l'assainissement de ",water_quantity,"L d'eau:\n- ",water_quantity/5," filtres\n- ",water_quantity/5*3," lampes UV\n- ",water_quantity/10,"kg de chlore")
import math
if water_quantity==int(water_quantity):

    water_quantity=int(water_quantity)
n_filter = math.ceil(water_quantity/5)
n_light = math.ceil(water_quantity/5*3)
kg_chlorine = water_quantity/10

# print(water_quantity)

# print("Voici les éléments requis pour assainir "+str(water_quantity)+"L d'eau:\n\n        \t- Filtre(s): ",n_filter,"\n\n \t  \t- Lampe(s) UV : ",n_light,"\n \n \t \t- Chlore :",kg_chlorine,"kg")
# print("Voici les éléments requis pour assainir "+str(water_quantity)+"L d'eau:")
# print("\n               - Filtre(s) :",n_filter)

# print("\n               - Lampe(s) UV :",n_light,)

# print("\n               - Chlore : "+str(kg_chlorine)+"kg")


z=f"""Voici les éléments requis pour assainir {water_quantity}L d'eau:\n
        \t- Filtre(s) : {n_filter}\n
        \t- Lampe(s) UV : {n_light}\n
        \t- Chlore : {kg_chlorine}kg"""

print(z)