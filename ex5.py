#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
erreur=0
G,B,S=0,0,0
for medaille in code_medals:
    if medaille !="G" and medaille !="S" and medaille !="B":
        erreur=1
    else:
        if medaille=="G":
            G+=1
        if medaille=="S":
            B+=1        
        if medaille=="B":
            S+=1

if erreur==1:
    print("Ceci est une chaine invalide.")
else:
    print(str(country)+":")
    print(F"- {G} Or")
    print(F"- {B} Argent")
    print(F"- {S} Bronze")


