# Test Cases Documentation

This document contains detailed documentation for all automated test cases in the Golden Fork test suite, following the ISTQB template format.

## Table of Contents
- [Authentication Tests (TC001-TC010)](#authentication-tests)
- [Menu Workflow Tests (TC011-TC018)](#menu-workflow-tests)
- [End-to-End Tests (TC019-TC021)](#end-to-end-tests)

---

## Authentication Tests

### TC001: Login with Valid Credentials

| Field | Value |
|-------|-------|
| **ID Cas de test** | TC001 |
| **Titre Cas de test** | Se connecter avec des identifiants valides |
| **Créé par** | Test Automation |
| **Revue par** | QA Team |
| **Version** | 1.0 |
| **Niveau de test** | Système |
| **Type de test** | Fonctionnel |
| **Technique de test** | Partitionnement en classes d'équivalence (Classe valide) |

**Nom du testeur**: Automated  
**Date de test**: À exécuter  
**Statut**: Not Yet Executed

#### Prérequis
1. L'application Golden Fork est accessible
2. Un compte utilisateur existe dans le système
3. Le navigateur est ouvert

#### Jeu de données de test
| # | Donnée | Valeur |
|---|--------|--------|
| 1 | Email | testuser@goldenfork.com |
| 2 | Password | TestPass123! |

#### Scénario de test
Vérifier qu'un utilisateur peut se connecter avec des identifiants valides

#### Étapes de test

| Étape # | Action | Résultat Attendu | Résultat Réel | Pass/Fail |
|---------|--------|------------------|---------------|-----------|
| 1 | Naviguer vers /login | La page de connexion s'affiche | | Not Yet Executed |
| 2 | Saisir l'email valide | Le champ accepte l'email | | Not Yet Executed |
| 3 | Saisir le mot de passe valide | Le champ accepte le mot de passe | | Not Yet Executed |
| 4 | Cliquer sur le bouton "Login" | Redirection vers /menu, aucun message d'erreur | | Not Yet Executed |

---

### TC002: Login with Incorrect Password

| Field | Value |
|-------|-------|
| **ID Cas de test** | TC002 |
| **Titre Cas de test** | Se connecter avec un mot de passe incorrect |
| **Créé par** | Test Automation |
| **Revue par** | QA Team |
| **Version** | 1.0 |
| **Technique de test** | Partitionnement en classes d'équivalence (Classe invalide) |

#### Prérequis
1. L'application est accessible
2. Un compte utilisateur existe

#### Jeu de données de test
| # | Donnée | Valeur |
|---|--------|--------|
| 1 | Email | testuser@goldenfork.com |
| 2 | Password | WrongPassword123! |

#### Scénario de test
Vérifier que le système refuse la connexion avec un mot de passe incorrect

#### Étapes de test

| Étape # | Action | Résultat Attendu | Résultat Réel | Pass/Fail |
|---------|--------|------------------|---------------|-----------|
| 1 | Naviguer vers /login | La page de connexion s'affiche | | Not Yet Executed |
| 2 | Saisir l'email valide | Le champ accepte l'email | | Not Yet Executed |
| 3 | Saisir un mot de passe incorrect | Le champ accepte la saisie | | Not Yet Executed |
| 4 | Cliquer sur "Login" | Message d'erreur "Invalid password" ou "Invalid credentials" affiché | | Not Yet Executed |
| 5 | Vérifier l'URL | L'utilisateur reste sur /login | | Not Yet Executed |

---

### TC003: Login with Invalid Email Format

| Field | Value |
|-------|-------|
| **ID Cas de test** | TC003 |
| **Titre Cas de test** | Se connecter avec un format d'email invalide |
| **Technique de test** | Analyse des valeurs limites, Prédiction d'erreurs |

#### Prérequis
1. L'application est accessible

#### Jeu de données de test (Paramétrisé)
| # | Email (Invalide) | Raison |
|---|------------------|--------|
| 1 | (vide) | Champ vide |
| 2 | notanemail | Pas de symbole @ |
| 3 | @example.com | Pas de partie locale |

#### Scénario de test
Vérifier que le système valide le format de l'email

#### Étapes de test

| Étape # | Action | Résultat Attendu | Résultat Réel | Pass/Fail |
|---------|--------|------------------|---------------|-----------|
| 1 | Naviguer vers /login | Page de connexion affichée | | Not Yet Executed |
| 2 | Saisir un email invalide | Champ accepte la saisie | | Not Yet Executed |
| 3 | Saisir un mot de passe | Champ accepte la saisie | | Not Yet Executed |
| 4 | Cliquer sur "Login" | Validation empêche la soumission OU message d'erreur affiché | | Not Yet Executed |

---

### TC005: Valid User Registration

| Field | Value |
|-------|-------|
| **ID Cas de test** | TC005 |
| **Titre Cas de test** | Enregistrer un nouvel utilisateur avec des données valides |
| **Technique de test** | Test par table de décision |

#### Prérequis
1. L'application est accessible
2. L'email n'est pas déjà enregistré

#### Jeu de données de test
| # | Donnée | Valeur |
|---|--------|--------|
| 1 | Username | testuser{random} |
| 2 | Email | user{random}@example.com |
| 3 | Phone | +216 98 123 456 |
| 4 | Password | TestPass123! |
| 5 | Confirm Password | TestPass123! |

#### Scénario de test
Vérifier qu'un nouvel utilisateur peut s'enregistrer avec succès

#### Étapes de test

| Étape # | Action | Résultat Attendu | Résultat Réel | Pass/Fail |
|---------|--------|------------------|---------------|-----------|
| 1 | Naviguer vers /register | Page d'inscription affichée | | Not Yet Executed |
| 2 | Saisir tous les champs avec des données valides | Tous les champs acceptent les données | | Not Yet Executed |
| 3 | Cliquer sur "Create Account" | Message de succès OU redirection vers /login | | Not Yet Executed |

---

## Menu Workflow Tests

### TC011: View Menu List as Authenticated User

| Field | Value |
|-------|-------|
| **ID Cas de test** | TC011 |
| **Titre Cas de test** | Afficher la liste des menus en tant qu'utilisateur authentifié |
| **Technique de test** | Test de cas d'utilisation |

#### Prérequis
1. L'utilisateur est connecté
2. L'application est accessible

#### Jeu de données de test
| # | Donnée | Valeur |
|---|--------|--------|
| 1 | User Email | testuser@goldenfork.com |
| 2 | User Password | TestPass123! |

#### Scénario de test
Vérifier qu'un utilisateur authentifié peut accéder et voir la liste des menus

#### Étapes de test

| Étape # | Action | Résultat Attendu | Résultat Réel | Pass/Fail |
|---------|--------|------------------|---------------|-----------|
| 1 | Se connecter avec des identifiants valides | Connexion réussie | | Not Yet Executed |
| 2 | Naviguer vers /menu | Page des menus affichée | | Not Yet Executed |
| 3 | Vérifier le titre de la page | "Our Menus" affiché | | Not Yet Executed |
| 4 | Vérifier le contenu | Des menus sont affichés OU message "No menus available" | | Not Yet Executed |

---

### TC012: Admin Add New Menu

| Field | Value |
|-------|-------|
| **ID Cas de test** | TC012 |
| **Titre Cas de test** | Administrateur crée un nouveau menu |
| **Technique de test** | Test par table de décision (Opération CREATE) |

#### Prérequis
1. L'utilisateur est connecté en tant qu'Admin ou Chef
2. L'application est accessible

#### Jeu de données de test
| # | Donnée | Valeur |
|---|--------|--------|
| 1 | Admin Email | admin@goldenfork.com |
| 2 | Admin Password | AdminPass123! |
| 3 | Menu Name | Test Menu {random} |
| 4 | Menu Description | Test description for menu |

#### Scénario de test
Vérifier qu'un administrateur peut créer un nouveau menu

#### Étapes de test

| Étape # | Action | Résultat Attendu | Résultat Réel | Pass/Fail |
|---------|--------|------------------|---------------|-----------|
| 1 | Se connecter en tant qu'Admin | Connexion réussie | | Not Yet Executed |
| 2 | Naviguer vers /menu | Page des menus affichée | | Not Yet Executed |
| 3 | Vérifier la présence du bouton "Add New Menu" | Bouton visible pour admin | | Not Yet Executed |
| 4 | Cliquer sur "Add New Menu" | Modal d'ajout s'ouvre | | Not Yet Executed |
| 5 | Saisir le nom du menu | Champ accepte la saisie | | Not Yet Executed |
| 6 | Saisir la description | Champ accepte la saisie | | Not Yet Executed |
| 7 | Cliquer sur "Save" | Menu créé, modal se ferme | | Not Yet Executed |
| 8 | Actualiser la page | Nouveau menu apparaît dans la liste | | Not Yet Executed |

---

### TC013: Admin Edit Existing Menu

| Field | Value |
|-------|-------|
| **ID Cas de test** | TC013 |
| **Titre Cas de test** | Administrateur modifie un menu existant |
| **Technique de test** | Test par table de décision (Opération UPDATE) |

#### Prérequis
1. Connecté en tant qu'Admin
2. Au moins un menu existe

#### Jeu de données de test
| # | Donnée | Valeur |
|---|--------|--------|
| 1 | Updated Name | Updated Menu {random} |
| 2 | Updated Description | Updated description text |

#### Scénario de test
Vérifier qu'un administrateur peut modifier un menu existant

#### Étapes de test

| Étape # | Action | Résultat Attendu | Résultat Réel | Pass/Fail |
|---------|--------|------------------|---------------|-----------|
| 1 | Naviguer vers /menu | Page des menus affichée | | Not Yet Executed |
| 2 | Cliquer sur le menu déroulant d'options | Options affichées (Edit, Delete) | | Not Yet Executed |
| 3 | Cliquer sur "Edit" | Modal d'édition s'ouvre avec données existantes | | Not Yet Executed |
| 4 | Modifier le nom | Nouveau nom accepté | | Not Yet Executed |
| 5 | Modifier la description | Nouvelle description acceptée | | Not Yet Executed |
| 6 | Cliquer sur "Save" | Modifications enregistrées | | Not Yet Executed |
| 7 | Actualiser la page | Menu mis à jour apparaît avec nouvelles données | | Not Yet Executed |

---

## End-to-End Tests

### TC019: Complete Customer Journey

| Field | Value |
|-------|-------|
| **ID Cas de test** | TC019 |
| **Titre Cas de test** | Parcours complet client: Inscription → Connexion → Navigation |
| **Technique de test** | Test de cas d'utilisation (User Story) |
| **Marqueur** | E2E, Slow |

#### Prérequis
1. L'application est accessible
2. Aucun compte existant pour l'email de test

#### Jeu de données de test
| # | Donnée | Valeur |
|---|--------|--------|
| 1 | Username | newuser{random} |
| 2 | Email | newuser{random}@example.com |
| 3 | Phone | +216 98 {random} |
| 4 | Password | E2ETest123! |

#### Scénario de test
En tant que nouveau client, je veux m'inscrire, me connecter et parcourir les menus

#### Étapes de test

| Étape # | Action | Résultat Attendu | Résultat Réel | Pass/Fail |
|---------|--------|------------------|---------------|-----------|
| 1 | Naviguer vers /register | Page d'inscription affichée | | Not Yet Executed |
| 2 | Remplir le formulaire d'inscription | Tous les champs acceptent les données | | Not Yet Executed |
| 3 | Soumettre le formulaire | Inscription réussie, redirection | | Not Yet Executed |
| 4 | Naviguer vers /login | Page de connexion affichée | | Not Yet Executed |
| 5 | Se connecter avec les nouveaux identifiants | Connexion réussie | | Not Yet Executed |
| 6 | Vérifier la redirection | Redirigé vers /menu | | Not Yet Executed |
| 7 | Vérifier l'affichage des menus | Menus ou message "no menus" affiché | | Not Yet Executed |

---

## Test Techniques Summary

### Techniques Appliquées

| Technique | Tests Concernés | Description |
|-----------|-----------------|-------------|
| **Partitionnement en classes d'équivalence** | TC001, TC002, TC003 | Division des entrées en classes valides/invalides |
| **Analyse des valeurs limites** | TC003, TC007 | Test des limites min/max (longueur password, etc.) |
| **Test par table de décision** | TC005, TC006, TC012, TC013, TC014 | Combinaisons de conditions pour validation |
| **Test de transition d'états** | TC008, TC009, TC016 | Navigation entre pages/états |
| **Test de cas d'utilisation** | TC010, TC011, TC019, TC020 | Scénarios utilisateur complets |
| **Prédiction d'erreurs** | TC004 | Anticipation d'erreurs communes utilisateur |

---

## Execution Guidelines

### How to Execute Tests

1. **Automated Execution**
   ```bash
   pytest tests/test_authentication.py::TestAuthentication::test_TC001_valid_login -v
   ```

2. **Generate Report**
   ```bash
   pytest --html=reports/test_report.html --self-contained-html
   ```

3. **Update Test Results**
   - After execution, update "Résultat Réel" and "Pass/Fail" columns
   - Take screenshots for failed tests (automatically captured)
   - Document any deviations or issues

### Result Interpretation

- **Pass**: Test exécuté avec succès, résultats conformes aux attentes
- **Fail**: Test échoué, résultats non conformes
- **Blocked**: Test ne peut pas être exécuté (dépendances)
- **Not Yet Executed**: Test non encore exécuté

---

**Document Version**: 1.0  
**Last Updated**: January 2026  
**Total Test Cases**: 21+  
**Automation Coverage**: 100%
