age = 35.48594923498
# chaine  = "j'ai" + age + "ans"s



chaine = "j'ai "+str(age) +" ans"

print(chaine)
nom="michel"

# formatage --------------

toSTR= "j'ai "+str(age) +" ans"
plus= "j'ai ",age, "ans"

percent=("bonjour %s'" %age)
print (percent)

percent=("bonjour %s %d allo" %(nom,age))
print (percent)

# voir real python 

print("%s a %.2f ans" %(nom, age))


var1=2
var2=4.453

chaine1="reponse: {}, {}".format(var1,var2) 
print(chaine1)

chaine2="reponse: {1}, {0}".format(var1,var2) 
print(chaine2)

chaine3="reponse: {:.2g}, {:.2g}".format(var1,var2) 
print(chaine3)


# ----------------fstring---------------------------
print("fstring\n\n")
nom = "michel"
age = 19.6349394
chaine =  f"{nom} est mon nom, {age:.2f} est mon age l'est go"



print(chaine)




# CH55555555555555555555555555555555555555555555555555555555555555


if "":
    print("True sur " "")
else:
    print("false")

if None:
    print("true")
else: 
    print("false")


a=1
if a==0:
    print("a")
    print("a"+34) # c'est une errreure mais python le lit pas  (lit juste erruer de syntaxe)
print("\n\ncontinue\n\n")




a=1
if a==1:
    print("a")
    # print("a"+34) # quand va dans brnache il y a erreure
print("continue")


# a=1 
# if a==1: { print("allo"),  print("hola") } 

# elif interomp if elif else sont couplé

# switch case match case
# note = int(input("une note sur 100"))
# match note:
#     case n if n >= 90:
#         print("A")
#     case n if n >= 60:
#         print("B C")
#     case other:
#         pass

# chaine = "benjamin"
# match chaine:
#     case "0":
#         print("bonjour")
#         print("test")
#     case "benjamin":
#         print("benjamin")
#     case other:
#         print("autre") 


actions = input("que voulez vous faire: ")
match actions.split():
    case ["quitter"]:
        print("quit")
    case ["continuer"]:
        print("continue")
    case ["avancer", nombre, distance]:
        print(f"j'avance de {nombre} {distance}")
        print(actions.split())
    case ["attaquer",target,attack,damage]:
        print(f"j'attaque {target} avec {attack}")
        if int(damage)>=10:
            print("il meurt")
    case _:
        print("je fais rien")

    # case other:
    #     print("alllllo")
        # permet syntaxe complexe 


a = 1000
while a>10:
            print(a)
            a-=1

a = input("entre un nombre")
while not a.isdigit():
     a = input("entre un nombre")

print (int(a))


print (range(100))
print (list(range(100)))

# fonction generatrice 
print(list(range(100,10,-5)))


