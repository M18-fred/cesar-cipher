from cesar import dechiffrer

def bruteforce(texte):
    resultat=[]
    for cle in range(26):
        original=dechiffrer(texte,cle)
        resultat.append((cle,original))
    return resultat
def compter_lettres(texte) -> dict:
    compteur = {}
    texte=texte.upper()
    for lettre in texte:
        if lettre.isalpha():
            if lettre in compteur:
                compteur[lettre]+=1
            else:
                compteur.update({ lettre:1 })
    return compteur
def lettre_plus_frequente(compteur):
    meilleure_lettre = None
    meilleur_compte = 0
    for lettre, compte in compteur.items():
        if compte > meilleur_compte:
            meilleur_compte=compte
            meilleure_lettre=lettre
    return meilleure_lettre
def deviner_cle(texte):
    compteur = compter_lettres(texte)
    lettre_freq = lettre_plus_frequente(compteur)
    cle = (ord(lettre_freq) - ord('E'))%26
    return cle


