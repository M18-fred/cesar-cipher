from cesar import chiffrer, dechiffrer
from cryptanalyse import bruteforce, deviner_cle

if __name__ == "__main__":

    print("=== Chiffrement de Cesar === \n1. Chiffrer un texte \n2. Déchiffrer un texte \n3. Bruteforce (essayer toutes les clés)" \
    "\n4. Deviner la clé (analyse fréquentielle)\n5. Quitter")
    while True:
        texte=""
        n=int(input("\nVeuillez choisir une option : "))
        if(n==1):
            texte=input("Entrer le texte clair : ")
            cle=int(input("Entrer la clé : "))
            print("Texte chiffré : ",chiffrer(texte,cle))
        elif(n==2):
            texte=""
            texte=input("Entrer le texte chiffré : ")
            cle=int(input("Entrer la clé : "))
            print("Texte clair : ",dechiffrer(texte,cle))
        elif(n==3):
            liste=[]
            texte=input("Entrer le texte chiffré : ")
            liste=bruteforce(texte)
            for elt in liste:
                c,txt = elt
                print(f"Cle : {c} | texte obtenu : {txt}")
        elif(n==4):
            texte=input("Entrer le texte chiffré : ")
            cle_devinee=deviner_cle(texte)
            print("Clé devinée :", cle_devinee)
            print("Texte clair : ", dechiffrer(texte, cle_devinee))
        elif(n==5):
            break
        else:
            print("Option non valide !")
