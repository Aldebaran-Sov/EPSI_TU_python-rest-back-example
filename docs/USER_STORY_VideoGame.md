# User Stories - jeux vidéos

## 1. Récupérer la liste des jeux vidéos (GET /)
**En tant qu'utilisateur,**  
**je veux** pouvoir récupérer la liste des jeux vidéos,  
**Afin de** pouvoir consulter les jeux vidéos disponibles.

**Critères d'acceptation :**  
- Le système doit retourner la liste de tous les jeux vidéos dans la base de données.
- La réponse inclut le nom, le genre, la date de sortie de chaque jeu vidéo.
- S'il n'y a aucun jeu vidéo dans la base de données, le système doit retourner une liste vide.

---

## 2. Ajouter un jeu vidéo (POST /)
**En tant qu'utilisateur,**  
**je veux** pouvoir ajouter un nouveau jeu vidéo,  
**Afin de** pouvoir enrichir la liste des jeux disponibles.

**Critères d'acceptation :**  
- Le système doit permettre l’ajout d’un jeu vidéo en fournissant au minimum :
  - Le nom.
  - Le genre.
  - La date de sortie.
- Si une donnée obligatoire est manquante ou incorrecte, le système retourne une erreur avec un message approprié.
- Une fois le jeu vidéo ajouté, le système retourne un statut de succès avec les détails du jeu créé.

---

## 3. Récupérer les détails d’un jeu vidéo spécifique (GET /{id})
**En tant qu'utilisateur,**  
**je veux** pouvoir consulter les détails d’un jeu vidéo spécifique,  
**Afin de** voir ses informations complètes.

**Critères d'acceptation :**  
- Le système doit retourner le nom, le genre, la date de sortie et tout autre détail du jeu vidéo correspondant à l’ID fourni.
- Si aucun jeu vidéo avec cet ID n’existe, le système retourne une erreur avec un message approprié.

---

## 4. Mettre à jour un jeu vidéo (PUT /{id})
**En tant qu'utilisateur,**  
**je veux** pouvoir mettre à jour les informations d’un jeu vidéo existant,  
**Afin de** corriger ou modifier ses détails.

**Critères d'acceptation :**  
- Le système doit permettre la mise à jour des champs suivants :
  - Nom.
  - Genre.
  - Date de sortie.
- Si un champ est omis, sa valeur actuelle reste inchangée.
- Si aucun jeu vidéo avec l’ID fourni n’existe, le système retourne une erreur avec un message approprié.
- Une fois les modifications effectuées, le système retourne les détails du jeu mis à jour.

---

## 5. Supprimer un jeu vidéo (DELETE /{id})
**En tant qu'utilisateur,**  
**je veux** pouvoir supprimer un jeu vidéo,  
**Afin de** retirer un jeu de la liste des jeux disponibles.

**Critères d'acceptation :**  
- Le système doit permettre de supprimer un jeu vidéo en fournissant son ID.
- Si aucun jeu vidéo avec cet ID n’existe, le système retourne une erreur avec un message approprié.
- Une fois le jeu vidéo supprimé, le système retourne un statut de succès confirmant l’opération.

---

## 6. Recherche de jeux vidéos par genre ou nom (GET /search?name=&genre=)
**En tant qu'utilisateur,**  
**je veux** pouvoir rechercher des jeux vidéos par leur nom ou leur genre,  
**Afin de** trouver rapidement un jeu spécifique ou un type de jeu.

**Critères d'acceptation :**  
- Le système doit permettre une recherche basée sur :
  - Le nom (partiel ou complet).
  - Le genre.
- Si aucun résultat ne correspond aux critères, le système retourne une liste vide.
- La réponse doit inclure le nom, le genre, et la date de sortie des jeux trouvés.

---
