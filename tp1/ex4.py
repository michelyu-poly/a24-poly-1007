# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).
# - Demander le pourcentage de batterie du bateau
# - Calculer la distance possible en suivant les règles suivantes: 
#   - Entre 50% et 100% de batterie, chaque pourcentage équivaut à 2km
#   - Entre 25% et 50% de batterie, chaque pourcentage équivaut à 0,5km
#   - Entre 10% et 25% de batterie, chaque pourcentage équivaut à 1km
#   - Entre 5% et 10% de batterie, chaque pourcentage équivaut à 2.5km
#   - Entre 0% et 5% de batterie, chaque pourcentage équivaut à 6km  
# *La borne inférieure n'est pas incluse.
# - L'affichage la distance doit être arrondi au km près.  

battery_level = float(input("Pourcentage de batterie ? "))
distance=0
# while battery_level>50:
#     battery_level-=1
#     distance+=2

# while battery_level>25:
#     battery_level-=1
#     distance+=0.5

# while battery_level>10:
#     battery_level-=1
#     distance+=1

# while battery_level>5:
#     battery_level-=1
#     distance+=2.5

# while battery_level>0:
#     battery_level-=1
#     distance+=6
if battery_level == 0 or battery_level>100:
    print("La batterie est vide")

else:
    if battery_level>50:
        distance+=(battery_level-50)*2
        battery_level=50
        # print("1",distance)

    if battery_level>25:
        distance+=(battery_level-25)*0.5
        battery_level=25
        # print("2",distance)

    if battery_level>10:
        distance+=(battery_level-10)*1
        battery_level=10
        # print("3",distance)

    if battery_level>5:
        distance+=(battery_level-5)*2.5
        battery_level=5
        # print("4",distance)

    if battery_level>0:
        distance+=(battery_level)*6
        battery_level=0
        # print("5",distance)

    print(distance,"km")

# 49 - 69.5 
# 74 - 118
# 22.5 - 55