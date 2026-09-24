import os    
from exercices import slugifier, formater_date, compter_par_categorie, trier_par_date, temps_de_lecture
from rendu import charger_gabarit, remplir, page_complete, ecrire_page
from donnees import charger_articles, articles_prets


"""Programme principal : fabrique tout le site."""
#from donnees import statistiques
#from rendu import charger_gabarit, remplir, ecrire_page, page_complete
#from exercices import slugifier, formater_date, tronquer

def generer_accueil(articles):
    """Ecrit site/index.html en utilisant uniquement carte.html et base.html."""
    gabarit_carte = charger_gabarit("carte.html")
    une = articles[0]
    
    # Remplacement du <h1> par un <h2> pour éviter le doublon avec base.html
    html_une = f"""
    <section class="une" style="margin-bottom: 40px; border-bottom: 2px solid #ccc; padding-bottom: 20px;">
        <span class="badge" style="background: #e74c3c; color: white; padding: 5px 10px; font-weight: bold;">À LA UNE</span>
        <h2 style="font-size: 2.5em; margin: 15px 0;">
            <a href="articles/{slugifier(une['titre'])}.html" style="color: #2c3e50; text-decoration: none;">{une['titre']}</a>
        </h2>
        <p style="color: #7f8c8d; font-size: 0.9em;">🏷️ {une['categorie']} — 📅 {formater_date(une['date'])}</p>
        <img src="images/{une['image']}" alt="{une['titre']}" style="max-width: 100%; height: auto; border-radius: 8px; margin: 15px 0;">
        <p class="chapo" style="font-size: 1.2em; line-height: 1.6; color: #34495e;">{une['chapo']}</p>
    </section>
    """
    
    html_cartes = ""
    for art in articles[1:4]:
        valeurs_carte = {
            "titre": art["titre"],
            "chapo": art["chapo"],
            "image": art["image"],
            "date": formater_date(art["date"]),
            "categorie": art["categorie"],
            "fichier": slugifier(art["titre"]) + ".html",
            "prefixe": ""
        }
        html_cartes = html_cartes + remplir(gabarit_carte, valeurs_carte)
        
    contenu_page = f"""
    <main class="conteneur">
        {html_une}
        <h2 style="margin-top: 30px; border-bottom: 1px solid #ddd; padding-bottom: 10px;">Anciens articles</h2>
        <div class="grille-cartes" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 20px;">
            {html_cartes}
        </div>
    </main>
    """
    
    html_final = page_complete("Accueil - L'Intègre", contenu_page, prefixe="")
    ecrire_page("site/index.html", html_final)


def generer_actualites(articles):
    """Ecrit site/actualites.html en utilisant uniquement ligne_liste.html et base.html."""
    gabarit_ligne = charger_gabarit("ligne_liste.html")
    
    stats = compter_par_categorie(articles)
    phrases_stats = []
    for categorie, nombre in stats.items():
        s = "s" if nombre > 1 else ""
        phrases_stats.append(f"{categorie} : {nombre} article{s}")
    phrase_statistiques = ", ".join(phrases_stats)
    
    html_lignes = ""
    for art in articles:
        valeurs_ligne = {
            "titre": art["titre"],
            "chapo": art["chapo"],
            "date": formater_date(art["date"]),
            "categorie": art["categorie"],
            "fichier": slugifier(art["titre"]) + ".html",
            "image": art["image"],  # 💡 CORRECTION : Ajout de la variable attendue par ligne_liste.html
            "prefixe": ""
        }
        html_lignes = html_lignes + remplir(gabarit_ligne, valeurs_ligne)
        
    # Remplacement du <h1> par un <h2> ici aussi
    contenu_page = f"""
    <main class="conteneur" style="padding: 20px 0;">
        <h2 style="color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 10px;">Toutes les actualités</h2>
        <div class="barre-stats" style="background: #ecf0f1; padding: 15px; margin: 20px 0; border-radius: 4px; font-size: 0.95em;">
            📊 <strong>Répartition des articles :</strong> {phrase_statistiques}
        </div>
        <div class="flux-articles" style="margin-top: 20px;">
            {html_lignes}
        </div>
    </main>
    """
    
    html_final = page_complete("Actualités - L'Intègre", contenu_page, prefixe="")
    ecrire_page("site/actualites.html", html_final)

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


# 3. ===== STRUCTURE OFFICIELLE DES ÉTAPES DU TP =====
CSV = "articles.csv"
DOSSIER = "site/"
ETAPES = [
    ("Pages d'articles", generer_pages_articles),
    ("Accueil", generer_accueil),
    ("Page actualites", generer_actualites),
]

if __name__ == "__main__":
    print("🚀 Démarrage de la génération...")
    
    # Lecture et tri du CSV
    articles_liste = charger_articles("articles.csv")
    articles_liste = trier_par_date(articles_liste)
    
    # Exécution de la boucle du TP
    for nom, fonction in ETAPES:
        print(f"Exécution de l'étape : {nom}")
        fonction(articles_liste)
        
    print("✅ Génération terminée avec succès !")


def main():
    """Lance toutes les etapes de generation, dans l'ordre."""
    articles = articles_prets(CSV)
    print(str(len(articles)) + " articles charges")
    for nom, fonction in ETAPES:
        print("--- " + nom)
        fonction(articles)
    print("Termine. Ouvre site/index.html dans ton navigateur.")
main()