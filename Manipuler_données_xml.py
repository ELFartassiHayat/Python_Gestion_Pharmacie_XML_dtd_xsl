import xml.etree.ElementTree as ET
import os

FILENAME = "pharmacie.xml"


def charger_donnees():
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    return tree, root

def sauvegarder_donnees(tree):
    stylesheet = '<?xml-stylesheet type="text/xsl" href="pharmacie.xsl"?>'
    xml_data = ET.tostring(tree.getroot(), encoding='utf-8').decode('utf-8')
    with open(FILENAME, 'w', encoding='utf-8') as file:
        file.write('<?xml version="1.0" encoding="utf-8"?>\n')
        file.write(stylesheet + '\n')
        file.write(xml_data)

def existe_entite(root, tag, attribute, value):
    for entity in root.findall(tag):
        if str(entity.get(attribute)).strip() == str(value).strip():
           return entity
    return None


def init_xml_file(fichier_xml):
    if not os.path.exists(fichier_xml):
        root = ET.Element('pharmacie')
        tree = ET.ElementTree(root)
        tree.write(fichier_xml)
        print(f"Fichier {fichier_xml} créé avec succès.")

# === Gestion des Clients ===
def ajouter_client():
    tree, root = charger_donnees()
    id_client = input("Entrez l'ID du client : ")
    if existe_entite(root, "Client", "ID_Client", id_client) is not None:
        print("Un client avec cet ID existe déjà.")
        return
    nom_client = input("Entrez le nom du client : ")
    telephone = input("Entrez le téléphone (facultatif) : ")
    ET.SubElement(root,"Client", {
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
    client_to_remove = existe_entite(root, "Client", "ID_Client", id_client)
    if client_to_remove is not None:
        # Remove related commandes
        commandes_to_remove = [cmd for cmd in root.findall("Commande") if cmd.get("ID_Client") == id_client]
        for commande in commandes_to_remove:
            root.remove(commande)

        root.remove(client_to_remove)
        sauvegarder_donnees(tree)
        print("Client et ses commandes associées supprimés avec succès !")
    else:
        print("Client non trouvé.")

def mettre_a_jour_client():
    tree, root = charger_donnees()
    id_client = input("Entrez l'ID du client à mettre à jour : ")
    client = existe_entite(root, "Client", "ID_Client", id_client)
    if client is None:
        print("Client non trouvé.")
        return
    nom_client = input("Entrez le nouveau nom du client : ")
    telephone = input("Entrez le nouveau téléphone (facultatif) : ")
    client.set("Nom_Client", nom_client)
    client.set("Telephone", telephone)
    sauvegarder_donnees(tree)
    print("Client mis à jour avec succès !")

# === Gestion des Fournisseurs ===
def ajouter_fournisseur():
    tree, root = charger_donnees()
    id_fournisseur = input("Entrez l'ID du fournisseur : ")
    if existe_entite(root, "Fournisseur", "ID_Fournisseur", id_fournisseur) is not None:
        print("Un fournisseur avec cet ID existe déjà.")
        return
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
    fournisseur_to_remove = existe_entite(root, "Fournisseur", "ID_Fournisseur", id_fournisseur)
    if fournisseur_to_remove is not None:
        # Remove related medicaments
        medicaments_to_remove = [med for med in root.findall("Medicament") if med.get("ID_Fournisseur") == id_fournisseur]
        for medicament in medicaments_to_remove:
            # Also remove commandes linked to these medicaments
            commandes_to_remove = [cmd for cmd in root.findall("Commande") if cmd.get("ID_Medicament") == medicament.get("ID_Medicament")]
            for commande in commandes_to_remove:
                root.remove(commande)
            root.remove(medicament)
        root.remove(fournisseur_to_remove)
        sauvegarder_donnees(tree)
        print("Fournisseur, ses médicaments et commandes associées supprimés avec succès !")
    else:
        print("Fournisseur non trouvé.")

def mettre_a_jour_fournisseur():
    tree, root = charger_donnees()
    id_fournisseur = input("Entrez l'ID du fournisseur à mettre à jour : ")
    fournisseur = existe_entite(root, "Fournisseur", "ID_Fournisseur", id_fournisseur)
    if fournisseur is None:
        print("Fournisseur non trouvé.")
        return
    nom_fournisseur = input("Entrez le nouveau nom du fournisseur : ")
    telephone = input("Entrez le nouveau téléphone (facultatif) : ")
    fournisseur.set("Nom_Fournisseur", nom_fournisseur)
    fournisseur.set("Telephone", telephone)
    sauvegarder_donnees(tree)
    print("Fournisseur mis à jour avec succès !")

# === Gestion des Médicaments ===
def ajouter_medicament():
    tree, root = charger_donnees()
    id_medicament = input("Entrez l'ID du médicament : ")
    if existe_entite(root, "Medicament", "ID_Medicament", id_medicament) is not None:
        print("Un médicament avec cet ID existe déjà.")
        return

    id_fournisseur = input("Entrez l'ID du fournisseur : ").strip()
    if existe_entite(root, "Fournisseur", "ID_Fournisseur", id_fournisseur) is None:
        print("Le fournisseur avec cet ID n'existe pas. Veuillez d'abord l'ajouter.")
        return

    nom_medicament = input("Entrez le nom du médicament : ")
    prix = input("Entrez le prix : ")
    quantite = input("Entrez la quantité : ")
    
    ET.SubElement(root, "Medicament", {
        "ID_Medicament": id_medicament,
        "Nom_Medicament": nom_medicament,
        "Prix": prix,
        "Quantite_Stock": quantite,
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
    medicament_to_remove = existe_entite(root, "Medicament", "ID_Medicament", id_medicament)
    if medicament_to_remove is not None:
        # Remove related commandes
        commandes_to_remove = [cmd for cmd in root.findall("Commande") if cmd.get("ID_Medicament") == id_medicament]
        for commande in commandes_to_remove:
            root.remove(commande)
        root.remove(medicament_to_remove)
        sauvegarder_donnees(tree)
        print("Médicament et ses commandes associées supprimés avec succès !")
    else:
        print("Médicament non trouvé.")

def mettre_a_jour_medicament():
    tree, root = charger_donnees()
    id_medicament = input("Entrez l'ID du médicament à mettre à jour : ")
    medicament = existe_entite(root, "Medicament", "ID_Medicament", id_medicament)
    if medicament is None:
        print("Médicament non trouvé.")
        return
    nom_medicament = input("Entrez le nouveau nom du médicament : ")
    prix = input("Entrez le nouveau prix : ")
    quantite_stock = input("Entrez la nouvelle quantité en stock (facultatif) : ")
    id_fournisseur = input("Entrez le nouvel ID du fournisseur : ")
    if not existe_entite(root, "Fournisseur", "ID_Fournisseur", id_fournisseur):
        print(f"Le fournisseur avec l'ID {id_fournisseur} n'existe pas.")
        return
    medicament.set("Nom_Medicament", nom_medicament)
    medicament.set("Prix", prix)
    medicament.set("Quantite_Stock", quantite_stock)
    medicament.set("ID_Fournisseur", id_fournisseur)
    sauvegarder_donnees(tree)
    print("Médicament mis à jour avec succès !")


# === Gestion des Commandes ===
def ajouter_commande():
    tree, root = charger_donnees()
    id_commande = input("Entrez l'ID de la commande : ")
    if existe_entite(root, "Commande", "ID_Commande", id_commande) is not None:
        print("Une commande avec cet ID existe déjà.")
        return
    date_commande = input("Entrez la date de la commande : ")
    id_client = input("Entrez l'ID du client : ")
    if existe_entite(root, "Client", "ID_Client", id_client) is None:
        print(f"Le client avec l'ID {id_client} n'existe pas.")
        return
    id_medicament = input("Entrez l'ID du médicament : ")
    if existe_entite(root, "Medicament", "ID_Medicament", id_medicament) is None:
        print(f"Le médicament avec l'ID {id_medicament} n'existe pas.")
        return
    ET.SubElement(root, "Commande", {
        "ID_Commande": id_commande,
        "Date": date_commande,
        "ID_Client": id_client,
        "ID_Medicament": id_medicament,
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
    commande_to_remove = None
    for commande in root.findall("Commande"):
        if commande.get("ID_Commande") == id_commande:
            commande_to_remove = commande
            break
    if commande_to_remove is not None:
        root.remove(commande_to_remove)
        sauvegarder_donnees(tree)
        print("Commande supprimée avec succès !")
    else:
        print("Commande non trouvée.")


def mettre_a_jour_commande():
    tree, root = charger_donnees()
    id_commande = input("Entrez l'ID de la commande à mettre à jour : ")
    commande = next((cmd for cmd in root.findall("Commande") if cmd.get("ID_Commande") == id_commande), None)
    if commande is None:
        print("Commande non trouvée.")
        return

    id_client = input("Entrez le nouvel ID du client : ")
    if existe_entite(root, "Client", "ID_Client", id_client) is None:
        print("Le client avec cet ID n'existe pas. Veuillez vérifier l'ID.")
        return

    id_medicament = input("Entrez le nouvel ID du médicament : ")
    if not existe_entite(root, "Medicament", "ID_Medicament", id_medicament):
        print("Le médicament avec cet ID n'existe pas. Veuillez vérifier l'ID.")
        return

    date_commande = input("Entrez la nouvelle date de la commande : ")
    commande.set("Date", date_commande)
    commande.set("ID_Client", id_client)
    commande.set("ID_Medicament", id_medicament)
    sauvegarder_donnees(tree)
    print("Commande mise à jour avec succès !")


# === Menu principal ===
def menu():
    init_xml_file(FILENAME)
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