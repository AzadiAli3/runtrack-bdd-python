import mysql.connector

# Fonction pour se connecter à la base de données
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Remplace par ton utilisateur MySQL
        password="Azadi23",  # Remplace par ton mot de passe MySQL
        database="stock_management"
    )

def initialize_db():
    conn = mysql.connector.connect(host="localhost", user="root", password="Azadi23")
    cursor = conn.cursor()
    
    # Création de la base de données
    cursor.execute("CREATE DATABASE IF NOT EXISTS stock_management")
    conn.database = "stock_management"2

    # Création de la table product
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            price INT NOT NULL,
            quantity INT NOT NULL,
            id_category INT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Ajouter un produit
def add_product():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Nom du produit : ")
    description = input("Description : ")
    price = int(input("Prix : "))
    quantity = int(input("Quantité : "))
    id_category = int(input("ID Catégorie : "))

    query = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, description, price, quantity, id_category))

    conn.commit()
    conn.close()
    print("✅ Produit ajouté avec succès !")

# Modifier un produit
def update_product():
    conn = connect_db()
    cursor = conn.cursor()

    product_id = int(input("ID du produit à modifier : "))
    name = input("Nouveau nom : ")
    description = input("Nouvelle description : ")
    price = int(input("Nouveau prix : "))
    quantity = int(input("Nouvelle quantité : "))
    id_category = int(input("Nouvelle ID Catégorie : "))

    query = """
        UPDATE product 
        SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s 
        WHERE id = %s
    """
    cursor.execute(query, (name, description, price, quantity, id_category, product_id))

    conn.commit()
    conn.close()
    print("✅ Produit modifié avec succès !")

# Supprimer un produit
def delete_product():
    conn = connect_db()
    cursor = conn.cursor()

    product_id = int(input("ID du produit à supprimer : "))

    query = "DELETE FROM product WHERE id = %s"
    cursor.execute(query, (product_id,))

    conn.commit()
    conn.close()
    print("❌ Produit supprimé avec succès !")

# Afficher tous les produits
def list_products():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()

    print("\n📦 Liste des produits :")
    for product in products:
        print(f"ID: {product[0]}, Nom: {product[1]}, Prix: {product[3]}€, Quantité: {product[4]}, Catégorie: {product[5]}")

    conn.close()

# Menu principal
def main():
    initialize_db()
    
    while True:
        print("\n📌 MENU DE GESTION DE STOCK")
        print("1️⃣ Ajouter un produit")
        print("2️⃣ Modifier un produit")
        print("3️⃣ Supprimer un produit")
        print("4️⃣ Afficher les produits")
        print("5️⃣ Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            add_product()
        elif choix == "2":
            update_product()
        elif choix == "3":
            delete_product()
        elif choix == "4":
            list_products()
        elif choix == "5":
            print("👋 Au revoir !")
            break
        else:
            print("⚠️ Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
