import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Azadi23",
    database="entreprise"
)

cursor = conn.cursor()

# Exécuter la requête pour récupérer les employés avec leur service
query = """
SELECT employe.nom, employe.prenom, employe.salaire, service.nom AS service
FROM employe
JOIN service ON employe.id_service = service.id;
"""
cursor.execute(query)

# Affichage du résultat en console
print("Liste des employés avec leur service :")
for nom, prenom, salaire, service in cursor.fetchall():
    print(f"- {nom} {prenom}, Salaire: {salaire} €, Service: {service}")

# Fermeture de la connexion
cursor.close()
conn.close()
