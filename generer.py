"""Programme principal : fabrique tout le site."""
from donnees import articles_prets, statistiques
from rendu import charger_gabarit, remplir, ecrire_page, page_complete
from exercices import slugifier, formater_date, temps_de_lecture, tronquer

CSV = "articles.csv"
DOSSIER = "site/"
def generer_pages_articles(articles):
    """Ecrit une page HTML par article dans site/articles/."""
    gabarit = charger_gabarit("articles.html")
    for article in articles:
        # 1. Construction du dictionnaire des valeurs à injecter dans le gabarit
        valeurs = {
            "titre": article["titre"],
            "categorie": article["categorie"],
            "chapo": article["chapo"],
            "contenu": article["contenu"],
            "image": article["image"],
            "date": formater_date(article["date"]),
            "minutes": temps_de_lecture(article["contenu"]),
            "prefixe": "../", # Permet aux liens de remonter d'un dossier
        }
        # 2. Remplissage du corps de l'article avec ses données spécifiques
        corps_article = remplir(gabarit, valeurs)
        
        # 3. Génération de la page HTML complète (avec la structure globale du site)
        page = page_complete(article["titre"], corps_article, "../")
        
        # 4. Création d'un nom de fichier propre à partir du titre (ex: "mon-titre.html")
        nom = slugifier(article["titre"]) + ".html"
        
        # 5. Écriture physique du fichier HTML sur votre disque dur
        ecrire_page(DOSSIER + "articles/" + nom, page)
# TODO : construire le dictionnaire des valeurs a injecter :
# titre, categorie, chapo, contenu et image viennent de l'article
# date doit passer par formater_date()
# minutes doit passer par temps_de_lecture(article["contenu"])
# prefixe vaut "../" car la page est dans un sous-dossier
# puis : contenu = remplir(gabarit, valeurs)
# page = page_complete(article["titre"], contenu, "../")
# nom = slugifier(article["titre"]) + ".html"
# ecrire_page(DOSSIER + "articles/" + nom, page)

ETAPES = [
("Pages d'articles", generer_pages_articles),
]

def main():
    """Lance toutes les etapes de generation, dans l'ordre."""
    articles = articles_prets(CSV)
    print(str(len(articles)) + " articles charges")
    for nom, fonction in ETAPES:
        print("--- " + nom)
        fonction(articles)
    print("Termine. Ouvre site/index.html dans ton navigateur.")
main()