"""Chargement des gabarits et ecriture des pages HTML."""

import os


# ===== MODÈLE : le remplissage d'un gabarit vous est donne =====
def remplir(gabarit, valeurs):
    """Remplace chaque marqueur du gabarit par sa valeur. valeurs est un dictionnaire, par exemple {"titre": "Bonjour"} : chaque {{titre}} du gabarit sera remplace par Bonjour."""
    resultat = gabarit
    for cle in valeurs:
        marqueur = "{{" + cle + "}}"
        resultat = resultat.replace(marqueur, str(valeurs[cle]))
        return resultat


def charger_gabarit(nom):
    """Lit un fichier du dossier gabarits et renvoie son contenu en texte. Exemple : charger_gabarit("carte.html")"""
    chemin_fichier = "gabarits/" + nom

    with open(chemin_fichier, mode="r", encoding="utf-8") as fichier:
        return fichier.read()
import os

def ecrire_page(chemin, contenu_html):
    """Ecrit le contenu dans le fichier, en creant le dossier si besoin,
    puis affiche une ligne de confirmation.
    """
    dossier_parent = os.path.dirname(chemin)
    
    if dossier_parent:
        os.makedirs(dossier_parent, exist_ok=True)
        
    with open(chemin, mode="w", encoding="utf-8") as fichier:
        fichier.write(contenu_html)
        
    print("Page ecrite : " + chemin)
    
    
def page_complete(titre_page, contenu, prefixe=""):
    """Assemble une page entiere : insere le contenu dans base.html.
    prefixe vaut "" pour une page a la racine, "../" pour une page rangee dans le dossier articles.
    """

    gabarit_base = charger_gabarit("base.html")
    donnees_remplissage = {
        "titre_page": titre_page,
        "contenu": contenu,
        "prefixe": prefixe
    }
    
    html_final = remplir(gabarit_base, donnees_remplissage)
    
    return html_final

