# inria-aphp
Ce repository rentre dans le cadre de la candidature au poste de Data Scientist en collaboration entre Inria et AH-HP. Les données portent sur des résultats de tests pcr COVID d'Australiens.

L'objectif général est de comprendre les problèmes de qualité de données. 

Le fichier aphp_code.ipynb contient le code permettant de répondre aux différentes questions posées. Ce dernier est divisé en différents chapitres :
- **Analyse de forme :** Evalue la forme générale des données ainsi que la création de dictionnaire qui seront utiles pour l'étude.
- **Données manquantes :** Evalue le taux de données manquantes par variable.
- **Qualité des données :** Evalue la qualité des données avec l'identification des incohérences dans le dataframe df_patient.
- **Gestion des doublons :** Effectue des transformations permettant d'appliquer des fonctions pour la suppression des doublons
- **Jointure entre df_patient et df_pcr :** Pour la jointure entre le dataframe df_patient et df_pcr
- **EDA :** Pour l'analyse exploratoire des données

Le dossier test_code contient l'ensemble des fichiers tests des fonctions qui ont permis de détecter et supprimer les doublons. 

L'environnement de travail est donné dans le dossier env.