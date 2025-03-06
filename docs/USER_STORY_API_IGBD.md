# User Stories - API IGBD

## 1. Récupérer l'access token
**En tant qu'utilisateur,**  
**je veux** pouvoir récupérer un access token,  
**Afin de** pouvoir faire des requêtes à l'API Oauth2 de IGBD.

**Critères d'acceptation :**  
- Retourne un code 200.
- La réponse au format json.
- L'access token au format string.

## 2.0. Récupérer le nom d'un jeux
**En tant qu'utilisateur,**  
**je veux** pouvoir récupérer le nom d'un jeux en fonction de son nom,  
**Afin de** pouvoir l'ajouter à la base de données.

**Critères d'acceptation :**
- Retourne un code 200.
- La réponse au format json.
- le nom du jeux dans la réponse est bien celui demandé.

## 2.1. Récupérer le(s) genre d'un jeux
**En tant qu'utilisateur,**  
**je veux** aussi récupérer le(s) genre quand je récupère son nom,  
**Afin de** pouvoir l'ajouter à la base de données.

**Critères d'acceptation :**
- Retourne un code 200.
- La réponse au format json.
- Le nom du jeux dans la réponse est bien celui demandé.
- Il y a bien la clès genres.
- Genres est une liste.
- La liste de genre dans la réponse est bien celui demandé.