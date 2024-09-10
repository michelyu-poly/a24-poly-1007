
import math

print(''' Nous allons vous aidé a calculer la distance maximale suivant l'axe des abcisses d'une boule lancée par un athlète en fonction de sa vitesse initiale et de l'angle depuis laquelle elle est lancée.''')
print(''' Nous aurons donc besoin de certaines informations ''')

# prise des parametres

# Prise de la valeur_angle initiale
print('''Nous avons besoin premierement de la vitesse initiale, vous devez choisir son unité puis entrer un sa valeur_angle. : ''')
print('''Votre angle a quelle mesure ? \
      \n 1- m/s (metre par seconde) \
      \n 2- Km/s (Kilometre par seconde)\
      \n 3- m/min (mettre par minute)\
      \n 4- Km/min (Kilometre par minutes)\
      \n 5- Km/h (Kilometre par heure)''')

choix1=str(input('Choississez un chiffre '))
a,b,c,d,e='1','2','3','4','5'

while choix1!=a and choix1!=b and choix1!=c and choix1!=d and choix1!=e:
    choix1 = input(str('Entrez un choix valide: '))


vitesse_initiale=(float(input('''Entrez la valeur de la vitesse initiale : ''')))

if choix1==b:
   vitesse_initiale=(vitesse_initiale)*1000
elif choix1==c:
   vitesse_initiale=(vitesse_initiale)/60
elif choix1==d:
   vitesse_initiale=(vitesse_initiale)*1000/60
elif choix1==e:
   vitesse_initiale=vitesse_initiale*(1000/3600)

# Prise de l'angle
print('''Nous avons besoin de l'angle de lancement, vous devez choisir son unité puis entrer un sa valeur_angle.''')
print('''Votre angle a quelle mesure ? \
      \n 1- Dégré \
      \n 2- Radian \
      \n 3- Minutes \
      \n 4- Secondes ''')

choix2=str(input('Choississez un chiffre '))

while choix2!=a and choix2!=b and choix2!=c and choix2!=d:
    choix2=str(input('Entrez un choix valide: '))

valeur_angle=float(input('''Entrez la valeur_angle de l'angle: '''))
if choix2==a:
   valeur_angle=math.radians(valeur_angle)
elif choix2==c:
   valeur_angle=math.radians(valeur_angle/60)
elif choix2==d:
   valeur_angle=math.radians(valeur_angle/3600)
   
# Calcul de la dite distance
print(''' Hypotheses: la boule sera toujours lancée à une hauteur de 2m et ne se déplacera pas dans l'axe des y.\
      \n La valeur de l'intensité de la pesanteur sera de 9,8N/Kg.\
      \n  ''')
D=float(((vitesse_initiale*vitesse_initiale)*(math.sin(2.0*valeur_angle)))/9.8)
 
print(f'''Avec ces hypotheses, la distance maximale est en suivant l'axe des abcisses est {D} metre(s)''')