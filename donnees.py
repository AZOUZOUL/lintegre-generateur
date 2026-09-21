"""Lecture et preparation des donnees du journal."""
import csv
from exercices import trier_par_date, compter_par_categorie

CHAMPS_OBLIGATOIRES = ["titre", "date", "categorie", "image", "chapo", "contenu"]
# ===== MODÈLE : la lecture du CSV vous est donnee =====
def charger_articles(chemin):
    """ Lit le fichier CSV et renvoie une liste de dictionnaires.
        Leve une erreur claire si le fichier est introuvable.
    """
    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            lecteur = csv.DictReader(fichier)
            return list(lecteur)
    except FileNotFoundError:
        print("Fichier introuvable : " + chemin)
        return []
    
def verifier_articles(articles):
    """Renvoie la liste des problemes trouves dans les articles.
Un probleme est une phrase decrivant ce qui manque, par exemple :
"Article 3 : le champ chapo est vide".
Renvoie une liste vide si tout va bien.
    """
# TODO : parcourir les articles avec enumerate() pour avoir le numero,
# puis pour chaque champ de CHAMPS_OBLIGATOIRES, verifier qu'il existe
# dans le dictionnaire et qu'il n'est pas vide.
    problemes = []
    for index, article in enumerate(articles, start=1):
        for champ in CHAMPS_OBLIGATOIRES:
            if champ not in article:
                problemes.append(f"Article {index} : le champ {champ} n'existe pas.")
            elif not article[champ].strip():
                problemes.append(f"Article {index} : le champ {champ} est vide.")
    return problemes

def articles_prets(chemin):
    """Charge, verifie et trie les articles du plus recent au plus ancien.
Affiche les problemes eventuels avant de renvoyer la liste triee.
    """
# TODO : appeler charger_articles(), puis verifier_articles(),
# afficher chaque probleme avec print(), puis renvoyer
# les articles tries avec trier_par_date()
    articles =  charger_articles(chemin="articles.csv")
    problemes = verifier_articles(articles)
    for probleme in problemes:
        print(probleme)
    return trier_par_date(articles)
    
    
    

def statistiques(articles):
    """Renvoie un dictionnaire {categorie: nombre}, via la fonction du dojo."""
# TODO : une seule ligne, en reutilisant compter_par_categorie()
    return compter_par_categorie(articles)