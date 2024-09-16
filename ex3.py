import math
vitesse_initiale=(float(input('''Vitesse initiale (m/s): ''')))
angle=(float(input('''Angle de lancer (en degrés): ''')))

Distance=((vitesse_initiale**2)*(math.sin(2*math.radians(angle))))/9.8
Distance_arrondie=round(Distance, 2)
print(f'''Distance parcourue: {Distance_arrondie}m''')