import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

# Connexion à la base de données
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Azadi23",
        database="stock_management"
    )

# Fonction pour récupérer les produits
def fetch_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Fonction pour afficher les produits dans le tableau
def display_products():
    for row in tree.get_children():
        tree.delete(row)
    for product in fetch_products():
        tree.insert("", "end", values=product)

# Ajouter un produit
def add_product():
    def save_product():
        name = name_entry.get()
        description = desc_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()
        id_category = category_entry.get()

        if not name or not price or not quantity or not id_category:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
            (name, description, int(price), int(quantity), int(id_category))
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Succès", "Produit ajouté")
        add_window.destroy()
        display_products()

    add_window = tk.Toplevel(root)
    add_window.title("Ajouter un produit")

    tk.Label(add_window, text="Nom :").grid(row=0, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Description :").grid(row=1, column=0)
    desc_entry = tk.Entry(add_window)
    desc_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Prix :").grid(row=2, column=0)
    price_entry = tk.Entry(add_window)
    price_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Quantité :").grid(row=3, column=0)
    quantity_entry = tk.Entry(add_window)
    quantity_entry.grid(row=3, column=1)

    tk.Label(add_window, text="ID Catégorie :").grid(row=4, column=0)
    category_entry = tk.Entry(add_window)
    category_entry.grid(row=4, column=1)

    tk.Button(add_window, text="Ajouter", command=save_product).grid(row=5, columnspan=2)

# Modifier un produit
def update_product():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Erreur", "Sélectionnez un produit à modifier")
        return

    item = tree.item(selected_item)["values"]
    product_id = item[0]

    def save_changes():
        name = name_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE product SET name=%s, price=%s, quantity=%s WHERE id=%s",
            (name, int(price), int(quantity), product_id)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Succès", "Produit modifié")
        update_window.destroy()
        display_products()

    update_window = tk.Toplevel(root)
    update_window.title("Modifier un produit")

    tk.Label(update_window, text="Nom :").grid(row=0, column=0)
    name_entry = tk.Entry(update_window)
    name_entry.insert(0, item[1])
    name_entry.grid(row=0, column=1)

    tk.Label(update_window, text="Prix :").grid(row=1, column=0)
    price_entry = tk.Entry(update_window)
    price_entry.insert(0, item[3])
    price_entry.grid(row=1, column=1)

    tk.Label(update_window, text="Quantité :").grid(row=2, column=0)
    quantity_entry = tk.Entry(update_window)
    quantity_entry.insert(0, item[4])
    quantity_entry.grid(row=2, column=1)

    tk.Button(update_window, text="Sauvegarder", command=save_changes).grid(row=3, columnspan=2)

# Supprimer un produit
def delete_product():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Erreur", "Sélectionnez un produit à supprimer")
        return

    item = tree.item(selected_item)["values"]
    product_id = item[0]

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE id=%s", (product_id,))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Succès", "Produit supprimé")
    display_products()

# Interface principale
root = tk.Tk()
root.title("Gestion de Stock")

# Tableau des produits
columns = ("ID", "Nom", "Description", "Prix", "Quantité", "Catégorie")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack()

# Boutons
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Ajouter", command=add_product).grid(row=0, column=0)
tk.Button(btn_frame, text="Modifier", command=update_product).grid(row=0, column=1)
tk.Button(btn_frame, text="Supprimer", command=delete_product).grid(row=0, column=2)

# Charger les produits
display_products()

root.mainloop()
