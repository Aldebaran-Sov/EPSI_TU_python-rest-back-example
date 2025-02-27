# User Stories - API IGBD

## 1. Récupérer l'access token
**En tant qu'utilisateur,**  
**je veux** pouvoir récupérer un access token,  
**Afin de** pouvoir faire des requêtes à l'API Oauth2 de IGBD.

**Critères d'acceptation :**  
- Retourne un code 200.
- La réponse au format json.
- L'access token au format string.

## 2. Récupérer les infos d'un jeux
**En tant qu'utilisateur,**  
**je veux** pouvoir récupérer les infos d'un jeux en fonction de son nom,  
**Afin de** pouvoir l'ajouter à la base de données.

**Critères d'acceptation :**
- Retourne un code 200.
- La réponse au format json.
- le nom du jeux dans la réponse est bien celui demandé.