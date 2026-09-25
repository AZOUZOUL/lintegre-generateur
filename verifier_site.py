"""Controle qualite des pages generees."""
import os
from bs4 import BeautifulSoup
import requests

reponse = requests.get("https://github.com/AZOUZOUL/lintegre-generateur/tree/main/site")
soup = BeautifulSoup(reponse.content, "html.parser")
print(soup.title.string)

def analyser_page(chemin):
    """Ouvre une page HTML locale et renvoie l'objet soup correspondant."""
    with open(chemin, "r", encoding="utf-8") as fichier:
        return BeautifulSoup(fichier.read(), "html.parser")

def controler(chemin):
    """Verifie une page et renvoie la liste des problemes trouves."""
    soup = analyser_page(chemin)
    problemes = []
# ===== MODÈLE : le premier controle vous est donne =====
    if soup.title is None or soup.title.string.strip() == "":
        problemes.append(chemin + " : la balise title est vide")
        
# TODO 1 : verifier que la page contient exactement un h1
# (soup.find_all("h1") renvoie une liste)
    liste_h1 = soup.find_all("h1")
    if len(liste_h1) != 1:
        problemes.append(chemin + f" : la page doit contenir exactement un h1 (trouve : {len(liste_h1)})")
    elif liste_h1[0].string is None or liste_h1[0].string.strip() == "":
        problemes.append(chemin + " : la balise h1 est vide")
        
# TODO 2 : verifier que CHAQUE image a un attribut alt non vide.
# Pour une image : image.get("alt")
    for img in soup.find_all("img"):
        alt_texte = img.get("alt")
        if alt_texte is None or alt_texte.strip() == "":
            problemes.append(chemin + " : une balise alt est vide ou manquante")

        
# TODO 3 : verifier qu'il ne reste aucun marqueur non remplace.
# Astuce : chercher la chaine "{{" dans le texte de la page
    texte_complet = soup.get_text()
    if "{{" in texte_complet:
        problemes.append(chemin + " : il reste des marqueurs {{ non remplaces")
        
    return problemes
def main():
    """Controle toutes les pages du dossier site."""
    pages = []
    for dossier, _, fichiers in os.walk("site"):
        for nom in fichiers:
            if nom.endswith(".html"):
                pages.append(os.path.join(dossier, nom))
    total = []
    for page in pages:
        total = total + controler(page)
        
    print(str(len(pages)) + " pages analysees")
    if total == []:
        print("Aucun probleme detecte.")
    else:
        for probleme in total:
            print(probleme)
main()