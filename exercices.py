"""Les 10 fonctions du dojo. A compléter une par une."""
# ===== 1. MODÈLE, déjà écrit pour toi =====
def compter_mots(texte):
    """Renvoie le nombre de mots contenus dans le texte."""
    mots = texte.split()
    return len(mots)

# ===== 2. Facile =====
def est_palindrome(mot):
    """Renvoie True si le mot se lit pareil dans les deux sens."""
# TODO : mettre le mot en minuscules, puis le comparer
# à lui-même inversé. Astuce : mot[::-1] inverse une chaîne.
    mot = mot.lower()
    return mot == mot[::-1]

# ===== 3. Facile =====
def fizzbuzz(n):
    """Renvoie la liste des nombres de 1 à n, où les multiples de 3
sont remplacés par Fizz, ceux de 5 par Buzz, et ceux des deux
par FizzBuzz.
Exemple : fizzbuzz(5) renvoie [1, 2, 'Fizz', 4, 'Buzz']
    """
# TODO : une boucle for avec range(), des conditions,
# et une liste à remplir avec append()
    resultat = []
    for i in range(1, n+1):
        
        if i % 3 == 0:
            resultat.append("Fizz")
        elif i % 5 == 0:
            resultat.append("Buzz")
        else:
            resultat.append(i)
            
        if resultat[-1] == "Fizz" and i % 5 == 0:
            resultat[-1] = "FizzBuzz"
    return resultat

# ===== 4. Facile =====
def maximum(nombres):
    """Renvoie le plus grand nombre de la liste, SANS utiliser max().
Renvoie None si la liste est vide.
    """
# TODO : garder le premier élément comme champion provisoire,
# puis parcourir la liste et changer de champion si besoin
    if len(nombres) == 0:
        return None
    
    majorant = nombres[0]
    for i in range(len(nombres)):
        if majorant < nombres[i]:
            majorant = nombres[i]
    return majorant

# ===== 5. Moyen-facile (utilisé dans le projet) =====
def tronquer(texte, limite):
    """Coupe le texte à limite caractères maximum, sans couper un mot
en deux, et ajoute trois points à la fin si le texte a été coupé.
Exemple : tronquer("Le marché central rouvre", 12) renvoie "Le marché..."
    """
# TODO : si le texte est plus court que la limite, le renvoyer tel quel.
# Sinon, couper avec texte[:limite], puis retirer le dernier mot
# incomplet en coupant au dernier espace (voir .rfind(" "))
    if len(texte) < limite:
        return texte
    
    texte_limite = texte[:limite]
    texte_liste = texte.split()
    
    x = texte_limite.rfind(" ")
    fin_texte_limite = texte_limite[x+1:]
    
    if fin_texte_limite in texte_liste:
        return texte_limite + "..."
    return texte_limite[:x] + "..."
    
# ===== 6. Moyen-facile (utilisé dans le projet) =====
def temps_de_lecture(texte):
    """Renvoie le temps de lecture en minutes, arrondi à l'entier
supérieur, en comptant 200 mots par minute. Minimum 1 minute.
    """
# TODO : réutilise compter_mots(), puis calcule.
# Astuce : pour arrondir au supérieur sans importer math,
# la division entière // et une condition suffisent.
    nombre_de_mots = len(texte.split())
    temps = nombre_de_mots // 200
    if 200 * temps == nombre_de_mots:
        return temps
    return temps + 1

# ===== 7. Moyen (utilisé dans le projet) =====
def slugifier(titre):
    """Transforme un titre en nom de fichier propre :
minuscules, sans accents, sans ponctuation, espaces en tirets.
Exemple : "Le marché central rouvre !" renvoie "le-marche-central-rouvre"
    """
# TODO : 1) passer en minuscules
# 2) remplacer les lettres accentuées par leur équivalent :
# un dictionnaire {"é": "e", "è": "e", "à": "a", ...} aide beaucoup
# 3) ne garder que les lettres, les chiffres et les espaces
# 4) attention : retirer la ponctuation laisse des espaces
# en double. Utilise .split() qui les ignore, puis recolle
# les morceaux avec "-".join(...) : les tirets doubles
# disparaissent tout seuls.
    titre = titre.lower()
    dictionnaire = {"é": "e",
                    "è": "e",
                    "ê": "e",
                    "à": "a",
                    "â": "a",
                    "î": "i",
                    "ï": "i",
                    "ô": "o",
                    "ü": "u",
                    "û": "u",
                    }
    dictionnaire_2 = {
                        ".": "",
                        ":": "",
                        "!": "",
                        "?": "",
                        ",": "",
                    }
    for accent, normal in dictionnaire.items():
        titre = titre.replace(accent, normal)
    for ponct, vide in dictionnaire_2.items():
        titre = titre.replace(ponct, vide)
    
    liste = titre.split()
    
    return "-".join(liste)
    
# ===== 8. Moyen (utilisé dans le projet) =====
def formater_date(date_iso):
    """Transforme une date 2026-03-05 en 5 mars 2026."""
# TODO : découper la chaîne avec .split("-"), convertir en entiers,
# et utiliser une liste des noms de mois pour retrouver le bon
    liste_date = [int(x) for x in date_iso.split("-")]
    dictionnaire = {    1: "janvier",
                        2: "février",
                        3: "mars",
                        4: "avril",
                        5: "mai",
                        6: "juin",
                        7: "juillet",
                        8: "août",
                        9: "septembre",
                        10: "octobre",
                        11: "novembre",
                        12: "decembre",
                        }
    return f"{liste_date[-1]} {dictionnaire.get(liste_date[1])} {liste_date[0]}"

# ===== 9. Moyen (utilisé dans le projet) =====
def trier_par_date(articles):
    """Renvoie la liste des articles triée du plus récent au plus ancien.
Chaque article est un dictionnaire contenant au moins la clé "date",
au format 2026-03-05.
    """
# TODO : la fonction sorted() accepte un paramètre key.
# Définis d'abord une petite fonction qui renvoie article["date"],
# puis passe-la à sorted(..., key=ta_fonction, reverse=True).
# Les dates au format AAAA-MM-JJ se trient correctement comme du texte.

    def ma_fonction(articles):
        return articles["date"]
    
    return sorted(articles, key=ma_fonction, reverse=True)

# ===== 10. Moyen (utilisé dans le projet) =====
def compter_par_categorie(articles):
    """Renvoie un dictionnaire {categorie: nombre d'articles}.
Exemple : {"Ville": 3, "Transport": 2, "Sport": 1}
    """
# TODO : parcourir les articles, et pour chaque catégorie,
# ajouter 1 si elle est déjà dans le dictionnaire,
# sinon la créer avec la valeur 1
    dictionnaire_compteur = {}
    
    for article in articles:
        categorie = article["categorie"]
        
        if categorie in dictionnaire_compteur:
            dictionnaire_compteur[categorie] += 1
        else:
            dictionnaire_compteur[categorie] = 1
    return dictionnaire_compteur