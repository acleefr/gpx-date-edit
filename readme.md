# 🏃 GPX Date Modifier

Ce script Python permet de **changer uniquement la date** des balises `<time>` dans un fichier `.gpx`, tout en conservant **les heures et les coordonnées GPS** intactes. Idéal pour recaler une trace GPS à un autre jour (ex. pour Strava ou Garmin).

---

## 🔧 Fonctionnalités

- Conserve les heures (`hh:mm:ss`) originales
- Ne modifie ni les coordonnées ni les autres métadonnées
- Nettoie le namespace XML pour garder des balises propres (pas de `ns0:`)
- Génère un nouveau fichier `.gpx` propre et prêt à l'emploi

---

## 📦 Utilisation

### 1. Installer Python (si ce n’est pas déjà fait)
Assure-toi d’avoir Python 3.6+ installé.

### 2. Lancer le script

```bash
python change_gpx_date.py
```

Tu peux aussi l’utiliser en modifiant les dernières lignes du script avec le nom du fichier GPX original, celui de sortie, et la nouvelle date :

```python
change_gpx_date("bzh.gpx", "1804.gpx", "2025-04-18")
```

---

## 📝 Exemple

Si ton fichier d'origine contient :
```xml
<time>2023-07-22T09:30:00Z</time>
```

Et que tu passes `"2025-04-18"` comme nouvelle date, tu obtiendras :
```xml
<time>2025-04-18T09:30:00Z</time>
```

---

## 🧼 Résultat

Le nouveau fichier `.gpx` est propre :
- Pas de balises avec `ns0:` 
- Compatible avec toutes les plateformes GPS

---

## 📁 Fichiers

- `change_gpx_date.py` → Le script Python
- `README.md` → Ce fichier d'explication

---

## 🧔 Auteur

Aclee, runner du dimanche
