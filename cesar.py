def decaler_lettre(lettre, cle) ->chr :
    if lettre.isupper():
     d=chr(((((ord(lettre) - ord('A')) + cle )%26)) + ord('A'))
     return d
    elif lettre.islower():
       d=chr(((((ord(lettre) - ord('a')) + cle )%26)) + ord('a'))
       return d
    else:
        return lettre
def chiffrer(texte, cle) ->str:
    resultat = ""
    for lettre in texte:
        resultat += decaler_lettre(lettre,cle)
    return resultat
def dechiffrer(texte, cle) ->str:
    original = ""
    original=chiffrer(texte,-cle)
    return original