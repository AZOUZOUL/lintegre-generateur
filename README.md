## 🌐 Gestion des fichiers générés & Déploiement
## Pour voir le site tape plutôt ça https://azouzoul.github.io/lintegre-generateur/site
### Faut-il committer les pages générées ?

**En règle générale, NON.** Dans un projet de développement classique, on ne versionne jamais les fichiers produits automatiquement par un script (comme le contenu du dossier `site/`, de la même manière que pour `venv/` ou `__pycache__`). Ces fichiers polluent l'historique des modifications (*diffs*), créent des conflits de fusion (merge conflicts) absurdes entre collaborateurs, et peuvent être reconstruits en une seule commande.

### ⚠️ L'exception pour ce projet

Dans le cadre de ce projet, **nous faisons une exception volontaire et assumée : le dossier `site/` EST suivi par Git et committé.**

**Pourquoi ?**
L'hébergement du site est confié à **GitHub Pages**. Cet outil est un serveur de fichiers statiques : il ne dispose pas d'un environnement Python pour exécuter notre script `generer.py`. Il est uniquement capable de lire et de diffuser des fichiers HTML/CSS déjà existants et présents sur le dépôt distant.

### 🛠️ Règle de travail en équipe

Pour éviter les conflits d'historique entre binômes lors de la génération du site :
1. **Communiquez** avant de pousser vos modifications de pages.
2. Assurez-vous de toujours exécuter `git pull` avant de lancer `python generer.py` localement.
3. Si un conflit survient sur le dossier `site/`, la priorité doit toujours être donnée à la logique du code source Python dans `generer.py` plutôt qu'aux fichiers HTML générés.
