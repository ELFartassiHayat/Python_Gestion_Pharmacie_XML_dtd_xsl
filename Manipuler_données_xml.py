
import os
import xml.etree.ElementTree as ET

FILENAME = "pharmacie.xml"

# Charger et sauvegarder le fichier XML
def charger_donnees():
    tree = ET.parse(FILENAME)
    return tree, tree.getroot()

def sauvegarder_donnees(tree):
    tree.write(FILENAME, encoding="utf-8", xml_declaration=True)

# === Gestion des Clients ===
def ajouter_client():
    tree, root = charger_donnees()
    id_client = input("Entrez l'ID du client : ")
    nom_client = input("Entrez le nom du client : ")
    telephone = input("Entrez le téléphone (facultatif) : ")
    ET.SubElement(root, "Client", {
        "ID_Client": id_client,
        "Nom_Client": nom_client,
        "Telephone": telephone
    })
    sauvegarder_donnees(tree)
    print("Client ajouté avec succès !")

def afficher_clients():
    _, root = charger_donnees()
    print("\nListe des clients :")
    for client in root.findall("Client"):
        print(f"ID: {client.get('ID_Client')}, Nom: {client.get('Nom_Client')}, Téléphone: {client.get('Telephone')}")

def supprimer_client():
    tree, root = charger_donnees()
    id_client = input("Entrez l'ID du client à supprimer : ")
    for client in root.findall("Client"):
        if client.get("ID_Client") == id_client:
            root.remove(client)
            sauvegarder_donnees(tree)
            print("Client supprimé avec succès !")
            return
    print("Client non trouvé.")

def mettre_a_jour_client():
    tree, root = charger_donnees()
    id_client = input("Entrez l'ID du client à mettre à jour : ")
    for client in root.findall("Client"):
        if client.get("ID_Client") == id_client:
            nom_client = input("Entrez le nouveau nom du client : ")
            telephone = input("Entrez le nouveau téléphone (facultatif) : ")
            client.set("Nom_Client", nom_client)
            client.set("Telephone", telephone)
            sauvegarder_donnees(tree)
            print("Client mis à jour avec succès !")
            return
    print("Client non trouvé.")

# === Gestion des Fournisseurs ===
def ajouter_fournisseur():
    tree, root = charger_donnees()
    id_fournisseur = input("Entrez l'ID du fournisseur : ")
    nom_fournisseur = input("Entrez le nom du fournisseur : ")
    telephone = input("Entrez le téléphone (facultatif) : ")
    ET.SubElement(root, "Fournisseur", {
        "ID_Fournisseur": id_fournisseur,
        "Nom_Fournisseur": nom_fournisseur,
        "Telephone": telephone
    })
    sauvegarder_donnees(tree)
    print("Fournisseur ajouté avec succès !")

def afficher_fournisseurs():
    _, root = charger_donnees()
    print("\nListe des fournisseurs :")
    for fournisseur in root.findall("Fournisseur"):
        print(f"ID: {fournisseur.get('ID_Fournisseur')}, Nom: {fournisseur.get('Nom_Fournisseur')}, Téléphone: {fournisseur.get('Telephone')}")

def supprimer_fournisseur():
    tree, root = charger_donnees()
    id_fournisseur = input("Entrez l'ID du fournisseur à supprimer : ")
    for fournisseur in root.findall("Fournisseur"):
        if fournisseur.get("ID_Fournisseur") == id_fournisseur:
            root.remove(fournisseur)
            sauvegarder_donnees(tree)
            print("Fournisseur supprimé avec succès !")
            return
    print("Fournisseur non trouvé.")

def mettre_a_jour_fournisseur():
    tree, root = charger_donnees()
    id_fournisseur = input("Entrez l'ID du fournisseur à mettre à jour : ")
    for fournisseur in root.findall("Fournisseur"):
        if fournisseur.get("ID_Fournisseur") == id_fournisseur:
            nom_fournisseur = input("Entrez le nouveau nom du fournisseur : ")
            telephone = input("Entrez le nouveau téléphone (facultatif) : ")
            fournisseur.set("Nom_Fournisseur", nom_fournisseur)
            fournisseur.set("Telephone", telephone)
            sauvegarder_donnees(tree)
            print("Fournisseur mis à jour avec succès !")
            return
    print("Fournisseur non trouvé.")

# === Gestion des Médicaments ===
def ajouter_medicament():
    tree, root = charger_donnees()
    id_medicament = input("Entrez l'ID du médicament : ")
    nom_medicament = input("Entrez le nom du médicament : ")
    prix = input("Entrez le prix du médicament : ")
    quantite_stock = input("Entrez la quantité en stock (facultatif) : ")
    id_fournisseur = input("Entrez l'ID du fournisseur : ")
    ET.SubElement(root, "Medicament", {
        "ID_Medicament": id_medicament,
        "Nom_Medicament": nom_medicament,
        "Prix": prix,
        "Quantite_Stock": quantite_stock,
        "ID_Fournisseur": id_fournisseur
    })
    sauvegarder_donnees(tree)
    print("Médicament ajouté avec succès !")

def afficher_medicaments():
    _, root = charger_donnees()
    print("\nListe des médicaments :")
    for medicament in root.findall("Medicament"):
        print(f"ID: {medicament.get('ID_Medicament')}, Nom: {medicament.get('Nom_Medicament')}, Prix: {medicament.get('Prix')}, Quantité: {medicament.get('Quantite_Stock')}, ID Fournisseur: {medicament.get('ID_Fournisseur')}")

def supprimer_medicament():
    tree, root = charger_donnees()
    id_medicament = input("Entrez l'ID du médicament à supprimer : ")
    for medicament in root.findall("Medicament"):
        if medicament.get("ID_Medicament") == id_medicament:
            root.remove(medicament)
            sauvegarder_donnees(tree)
            print("Médicament supprimé avec succès !")
            return
    print("Médicament non trouvé.")

def mettre_a_jour_medicament():
    tree, root = charger_donnees()
    id_medicament = input("Entrez l'ID du médicament à mettre à jour : ")
    for medicament in root.findall("Medicament"):
        if medicament.get("ID_Medicament") == id_medicament:
            nom_medicament = input("Entrez le nouveau nom du médicament : ")
            prix = input("Entrez le nouveau prix : ")
            quantite_stock = input("Entrez la nouvelle quantité en stock (facultatif) : ")
            id_fournisseur = input("Entrez le nouvel ID du fournisseur : ")
            medicament.set("Nom_Medicament", nom_medicament)
            medicament.set("Prix", prix)
            medicament.set("Quantite_Stock", quantite_stock)
            medicament.set("ID_Fournisseur", id_fournisseur)
            sauvegarder_donnees(tree)
            print("Médicament mis à jour avec succès !")
            return
    print("Médicament non trouvé.")

# === Gestion des Commandes ===
def ajouter_commande():
    tree, root = charger_donnees()
    id_commande = input("Entrez l'ID de la commande : ")
    date = input("Entrez la date de la commande : ")
    id_client = input("Entrez l'ID du client : ")
    id_medicament = input("Entrez l'ID du médicament : ")
    ET.SubElement(root, "Commande", {
        "ID_Commande": id_commande,
        "Date": date,
        "ID_Client": id_client,
        "ID_Medicament": id_medicament
    })
    sauvegarder_donnees(tree)
    print("Commande ajoutée avec succès !")

def afficher_commandes():
    _, root = charger_donnees()
    print("\nListe des commandes :")
    for commande in root.findall("Commande"):
        print(f"ID: {commande.get('ID_Commande')}, Date: {commande.get('Date')}, ID Client: {commande.get('ID_Client')}, ID Médicament: {commande.get('ID_Medicament')}")

def supprimer_commande():
    tree, root = charger_donnees()
    id_commande = input("Entrez l'ID de la commande à supprimer : ")
    for commande in root.findall("Commande"):
        if commande.get("ID_Commande") == id_commande:
            root.remove(commande)
            sauvegarder_donnees(tree)
            print("Commande supprimée avec succès !")
            return
    print("Commande non trouvée.")

def mettre_a_jour_commande():
    tree, root = charger_donnees()
    id_commande = input("Entrez l'ID de la commande à mettre à jour : ")
    for commande in root.findall("Commande"):
        if commande.get("ID_Commande") == id_commande:
            date = input("Entrez la nouvelle date de la commande : ")
            id_client = input("Entrez le nouvel ID du client : ")
            id_medicament = input("Entrez le nouvel ID du médicament : ")
            commande.set("Date", date)
            commande.set("ID_Client", id_client)
            commande.set("ID_Medicament", id_medicament)
            sauvegarder_donnees(tree)
            print("Commande mise à jour avec succès !")
            return
    print("Commande non trouvée.")

# === Menu principal ===
def menu():
    while True:
        print("\n=== Menu Gestion de Pharmacie ===")
        print("1. Gérer les clients")
        print("2. Gérer les fournisseurs")
        print("3. Gérer les médicaments")
        print("4. Gérer les commandes")
        print("5. Quitter")
        choix = input("Entrez votre choix : ")
        if choix == "1":
            sous_menu_clients()
        elif choix == "2":
            sous_menu_fournisseurs()
        elif choix == "3":
            sous_menu_medicaments()
        elif choix == "4":
            sous_menu_commandes()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")

# === Sous-menus ===
def sous_menu_clients():
    while True:
        print("\n=== Gestion des Clients ===")
        print("1. Ajouter un client")
        print("2. Afficher les clients")
        print("3. Supprimer un client")
        print("4. Mettre à jour un client")
        print("5. Retour au menu principal")
        choix = input("Entrez votre choix : ")
        if choix == "1":
            ajouter_client()
        elif choix == "2":
            afficher_clients()
        elif choix == "3":
            supprimer_client()
        elif choix == "4":
            mettre_a_jour_client()
        elif choix == "5":
            break
        else:
            print("Choix invalide, réessayez.")

def sous_menu_fournisseurs():
    while True:
        print("\n=== Gestion des Fournisseurs ===")
        print("1. Ajouter un fournisseur")
        print("2. Afficher les fournisseurs")
        print("3. Supprimer un fournisseur")
        print("4. Mettre à jour un fournisseur")
        print("5. Retour au menu principal")
        choix = input("Entrez votre choix : ")
        if choix == "1":
            ajouter_fournisseur()
        elif choix == "2":
            afficher_fournisseurs()
        elif choix == "3":
            supprimer_fournisseur()
        elif choix == "4":
            mettre_a_jour_fournisseur()
        elif choix == "5":
            break
        else:
            print("Choix invalide, réessayez.")

def sous_menu_medicaments():
    while True:
        print("\n=== Gestion des Médicaments ===")
        print("1. Ajouter un médicament")
        print("2. Afficher les médicaments")
        print("3. Supprimer un médicament")
        print("4. Mettre à jour un médicament")
        print("5. Retour au menu principal")
        choix = input("Entrez votre choix : ")
        if choix == "1":
            ajouter_medicament()
        elif choix == "2":
            afficher_medicaments()
        elif choix == "3":
            supprimer_medicament()
        elif choix == "4":
            mettre_a_jour_medicament()
        elif choix == "5":
            break
        else:
            print("Choix invalide, réessayez.")

def sous_menu_commandes():
    while True:
        print("\n=== Gestion des Commandes ===")
        print("1. Ajouter une commande")
        print("2. Afficher les commandes")
        print("3. Supprimer une commande")
        print("4. Mettre à jour une commande")
        print("5. Retour au menu principal")
        choix = input("Entrez votre choix : ")
        if choix == "1":
            ajouter_commande()
        elif choix == "2":
            afficher_commandes()
        elif choix == "3":
            supprimer_commande()
        elif choix == "4":
            mettre_a_jour_commande()
        elif choix == "5":
            break
        else:
            print("Choix invalide, réessayez.")

menu()

#pour démarer un serveur http locale en utilise la commande python -m http.server 8000 dans notre cmd
# pour accéder au fichier dans un navigateur http://localhost:8000/pharmacie.xml


