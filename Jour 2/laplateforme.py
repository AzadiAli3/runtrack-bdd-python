import mysql.connector

conn = mysql.connector.connect(
    host="localhost",      
    user="root",           
    password="Azadi23", 
    database="LaPlateforme"  
)

# Création d'un curseur pour exécuter la requête SQL
cursor = conn.cursor()

# Requête pour récupérer les noms et capacités des salles
query = "SELECT nom, capacite FROM salle;"
cursor.execute(query)

# Récupération et affichage des résultats
print("Liste des salles et leurs capacités :")
for nom, capacite in cursor.fetchall():
    print(f"- {nom}: {capacite} personnes")

# Fermeture de la connexion
cursor.close()
conn.close()
