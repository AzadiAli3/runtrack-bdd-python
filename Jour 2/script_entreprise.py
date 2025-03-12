import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )
        self.cursor = self.conn.cursor()

    def ajouter_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (nom, prenom, salaire, id_service))
        self.conn.commit()
        print("Employé ajouté avec succès !")

    def afficher_employes(self):
        query = """
        SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS service
        FROM employe
        JOIN service ON employe.id_service = service.id;
        """
        self.cursor.execute(query)
        for nom, prenom, salaire, service in self.cursor.fetchall():
            print(f"- {nom} {prenom}, Salaire: {salaire} €, Service: {service}")

    def mettre_a_jour_salaire(self, id_employe, nouveau_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.cursor.execute(query, (nouveau_salaire, id_employe))
        self.conn.commit()
        print("Salaire mis à jour !")

    def supprimer_employe(self, id_employe):
        query = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(query, (id_employe,))
        self.conn.commit()
        print("Employé supprimé avec succès !")

    def fermer_connexion(self):
        self.cursor.close()
        self.conn.close()

# ---- Exemple d'utilisation ----
employe_manager = Employe("localhost", "root", "Azadi23", "entreprise")

# Ajouter un employé
employe_manager.ajouter_employe("Dupont", "Alice", 2800, 1)

# Afficher tous les employés
employe_manager.afficher_employes()

# Modifier le salaire d'un employé
employe_manager.mettre_a_jour_salaire(1, 3200)

# Supprimer un employé
employe_manager.supprimer_employe(1)

# Fermer la connexion
employe_manager.fermer_connexion()