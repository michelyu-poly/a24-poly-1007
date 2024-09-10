
print('Nous aimerions graver dans le marbre la performance des athlètes participant, nous aurions donc besoin des informations suivantes :')


# Prise des parametres
nationalite=input('''Quelle est la nationalité de l'athlète ? ''')
nom=input('''Comment s'appelle l'athlète ? ''')
date=input('''Il a eu le record a quelle date ? ''')
dicipline=input('''Il pratiquait quelle dicipline ? ''')

print('''Est-ce qu'il etait dans une categorie précise ? \n Choix de reponse: oui ou non ''')
choix1='oui'
choix2='non'
choix=input('Saisir votre reponse : ')
while choix!=choix1 and choix!=choix2:
 print('Faites un choix valide ')
if choix==choix1:
    categorie=input('Laquelle ? ')
elif choix!=choix2:    
    print('''D'accord, c'est noté''')

record=input('''Enfin, il avait eu quel record ?''')

print('''Recapitilatif des elemant a prendre en compte pour la garvure sur le marbre \n ''')
if choix==choix1: 
    print(f'''Nom de l'athlète : {nom} \
      \n Pays représenté : {nationalite} \
      \n Date du record : {date} \
      \n Discipline : {dicipline} \
      \n Catégorie: {categorie} \
      \n Record : {record} ''')
elif choix==choix2:
     print(f'''Nom de l'athlète : {nom} \
      \n Pays représenté : {nationalite} \
      \n Date du record : {date} \
      \n Discipline : {dicipline} \
      \n Catégorie: Aucune  \
      \n Record : {record} ''')