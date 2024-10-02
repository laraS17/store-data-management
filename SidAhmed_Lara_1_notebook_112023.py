#!/usr/bin/env python
# coding: utf-8

# <div style="text-align:center; background-color:#001F3F; color:white; padding:10px;">
#     <h1>Optimisez la gestion des données d'une boutique avec R ou Python</h1>
# </div>
# 

# <div style="border: 2px solid #001F3F; background-color: #77B5FE; padding: 10px; text-align: center;">
#     <h2 style="font-weight: bold; color: #001F3F;">Etape 1 - Importation des librairies et chargement des fichiers</h2>
# </div>

# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">1.1 - Importation des librairies</h3>
# <hr style="border: 1px solid #0074CC;">

# In[1]:


#Importation de la librairie Pandas
import pandas as pd
import warnings


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">1.2 - Création des fonctions</h3>
# <hr style="border: 1px solid #0074CC;">

# In[2]:


def verifier_unicite(df, colonnes_cles):
    # Vérifie si des doublons sont présents dans la combinaison des colonnes spécifiées
    doublons = df.duplicated(subset=colonnes_cles, keep=False)
    # Compte le nombre de doublons
    nombre_doublons = doublons.sum()
    
    # Affiche le résultat
    if nombre_doublons == 0:
        print(f"La combinaison des clés {colonnes_cles} est unique dans le DataFrame.")
    else:
        print(f"La combinaison des clés {colonnes_cles} n'est pas unique dans le DataFrame et il y a {nombre_doublons} doublons.")


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">1.3 - chargement des fichiers</h3>
# <hr style="border: 1px solid #0074CC;">

# In[3]:


# Ignorer les avertissements de type UserWarning provenant de openpyxl
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")
#Importation des fichiers
erp = pd.read_excel('/Users/Bouboule/Documents/Projet. 5/fichier_erp.xlsx')
liaison = pd.read_excel('/Users/Bouboule/Documents/Projet. 5/fichier_liaison.xlsx')
web = pd.read_excel('/Users/Bouboule/Documents/Projet. 5/Fichier_web.xlsx')


# <div style="border: 2px solid #001F3F; background-color: #77B5FE; padding: 10px; text-align: center;">
#     <h2 style="font-weight: bold; color: #001F3F;">Etape 2 - Analyse du fichier ERP</h2>
# </div>

# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">2.1 - Analyse exploratoire</h3>
# <hr style="border: 1px solid #0074CC;">

# In[4]:


#Afficher les dimensions du dataset
erp.shape


# In[5]:


#Consulter le nombre de colonnes
erp.info()


# In[6]:


#Affichage des 5 premières lignes de la table
erp.head()


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">2.2 - Vérification des incohérences</h3>
# <hr style="border: 1px solid #0074CC;">

# In[7]:


# Trouver les lignes où 'stock_status' est 'outofstock' mais 'stock_quantity' est différent de 0
incoherences = erp[(erp['stock_status'] == 'outofstock') & (erp['stock_quantity'] != 0)]

# Imprimer les incohérences
print(incoherences)


# In[8]:


# Filtrer pour trouver les prix négatifs
prix_negatifs = erp[erp['price'] < 0]

# Vérifier s'il y a des prix négatifs
if not prix_negatifs.empty:
    print("Il y a des prix avec une valeur négative dans la colonne price.")
    print(prix_negatifs)
else:
    print("Il n'y a pas de prix avec une valeur négative dans la colonne price.")


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">2.3 - Vérification de l'unicité de la clé</h3>
# <hr style="border: 1px solid #0074CC;">

# In[9]:


verifier_unicite(erp, 'product_id')


# <div style="border: 2px solid #001F3F; background-color: #77B5FE; padding: 10px; text-align: center;">
#     <h2 style="font-weight: bold; color: #001F3F;">Etape 3 - Analyse du fichier liaison</h2>
# </div>

# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">3.1 - Analyse exploratoire</h3>
# <hr style="border: 1px solid #0074CC;">

# In[10]:


liaison.shape


# In[11]:


#Consulter le nombre de colonnes
liaison.info()


# In[12]:


#Affichage des 5 premières lignes de la table
liaison.head()


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">3.2 - Vérification de l'unicité de la clé</h3>
# <hr style="border: 1px solid #0074CC;">

# In[13]:


verifier_unicite(liaison, ['product_id', 'id_web'])


# <div style="border: 2px solid #001F3F; background-color: #77B5FE; padding: 10px; text-align: center;">
#     <h2 style="font-weight: bold; color: #001F3F;">Etape 4 - Analyse du fichier web</h2>
# </div>

# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">4.1 - Analyse exploratoire</h3>
# <hr style="border: 1px solid #0074CC;">

# In[14]:


web.shape


# In[15]:


#Consulter le nombre de colonnes
web.info()


# In[16]:


#Affichage des 5 premières lignes de la table
web.head()


# In[44]:


#renommer la colonne sku en id_web
web = web.rename(columns={'sku': 'id_web'})


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">4.2 - Vérification des incohérences</h3>
# <hr style="border: 1px solid #0074CC;">

# In[18]:


# Compter les valeurs NaN dans id_web
nombre_nan = web['id_web'].isna().sum()
print(f"Nombre de valeurs NaN dans id_web: {nombre_nan}")

# Identifier les valeurs non numériques et non NaN
valeurs_non_numeriques_non_nan = web[~web['id_web'].astype(str).str.isnumeric() & web['id_web'].notna()]

# Compter ces valeurs
nombre_non_numeriques_non_nan = valeurs_non_numeriques_non_nan.shape[0]

# Afficher leur nombre et leurs valeurs
print(f"Nombre de valeurs non numériques et non NaN dans id_web: {nombre_non_numeriques_non_nan}")
print("Valeurs non numériques et non NaN :")
print(valeurs_non_numeriques_non_nan['id_web'])


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">4.3 - Vérification de l'unicité</h3>
# <hr style="border: 1px solid #0074CC;">

# In[19]:


verifier_unicite(web, 'id_web')


# <h4 style="border-left: 5px solid #0074CC; font-weight: bold; color: #0060A8; padding-left: 10px;">4.3.1 - Vérification des null</h4>
# <hr style="border: 1px solid #0074CC;">

# In[47]:


# Filtrer les lignes où id_web est null
recherche_null = web[web['id_web'].isna()]
print(recherche_null.shape)
recherche_null.info()
recherche_null.head()


# In[21]:


recherche_null[recherche_null['post_name'].notnull()]


# <h4 style="border-left: 5px solid #0074CC; font-weight: bold; color: #0060A8; padding-left: 10px;">4.3.2 - Vérification des doublons non null</h4>
# <hr style="border: 1px solid #0074CC;">

# In[45]:


web_notnull = web[web['id_web'].notnull()]
web_notnull.shape


# In[23]:


verifier_unicite(web_notnull, 'id_web')


# In[24]:


web_notnull.head()


# In[25]:


attachment_count = web_notnull[web_notnull['post_type'] == 'attachment'].shape[0]

print(f"Nombre de doublons avec 'attachment' dans 'post_type': {attachment_count}")


# <h4 style="border-left: 5px solid #0074CC; font-weight: bold; color: #0060A8; padding-left: 10px;">4.3.3 - Suppression des doublons</h4>
# <hr style="border: 1px solid #0074CC;">

# In[26]:


# Trier le DataFrame pour que les 'product' apparaissent en premier
web_sorted = web.sort_values(by=['id_web', 'post_type'], ascending=[True, False])

# Supprimer les doublons en gardant la première occurrence
web_unique = web_sorted.drop_duplicates(subset='id_web', keep='first')
web_unique = web_unique.dropna(subset=['id_web'])


# In[27]:


verifier_unicite(web_unique, 'id_web')


# In[28]:


web_unique.shape


# In[29]:


# Filtrer pour trouver les lignes où post_type est 'attachment'
lignes_attachment = web_unique[web_unique['post_type'] == 'attachment']

# Compter ces lignes
nombre_lignes_attachment = len(lignes_attachment)

# Afficher le résultat
print(f"Nombre de lignes avec post_type 'attachment': {nombre_lignes_attachment}")


# <div style="border: 2px solid #001F3F; background-color: #77B5FE; padding: 10px; text-align: center;">
#     <h2 style="font-weight: bold; color: #001F3F;">Etape 5 - Merger les données</h2>
# </div>

# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">5.1 - Merge de ERP et liaison </h3>
# <hr style="border: 1px solid #0074CC;">

# <h4 style="border-left: 5px solid #0074CC; font-weight: bold; color: #0060A8; padding-left: 10px;">5.1.1 - Merger les dataframes</h4>
# <hr style="border: 1px solid #0074CC;">

# In[30]:


# Fusion entre erp et liaison 
erp_liaison = erp.merge(liaison, on='product_id', how= 'outer', indicator= 'true')
print(erp_liaison.shape)
erp_liaison.head()


# <h4 style="border-left: 5px solid #0074CC; font-weight: bold; color: #0060A8; padding-left: 10px;">5.1.2 - Vérifier le match des données</h4>
# <hr style="border: 1px solid #0074CC;">

# In[31]:


# Compter le nombre de lignes où la valeur de la colonne 'true' est différente de 'both'
verification_match = erp_liaison[erp_liaison['true'] != 'both']
print(verification_match.shape)
verification_match.head()


# <h4 style="border-left: 5px solid #0074CC; font-weight: bold; color: #0060A8; padding-left: 10px;">5.1.3 - Suppression de la colonne drop</h4>
# <hr style="border: 1px solid #0074CC;">

# In[32]:


erp_liaison_drop = erp_liaison.drop(['true'],axis=1)
erp_liaison_drop.head()


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">5.2 - Merge avec web</h3>
# <hr style="border: 1px solid #0074CC;">

# <h4 style="border-left: 5px solid #0074CC; font-weight: bold; color: #0060A8; padding-left: 10px;">5.2.2 - Merger les dataframes</h4>
# <hr style="border: 1px solid #0074CC;">

# In[33]:


# Fusion entre erp et liaison 
product = erp_liaison_drop.merge(web_unique, on='id_web', how='outer', indicator= 'true')
print(product.shape)
product.head()


# <h4 style="border-left: 5px solid #0074CC; font-weight: bold; color: #0060A8; padding-left: 10px;">5.2.2 - Vérifier le match des données</h4>
# <hr style="border: 1px solid #0074CC;">

# In[34]:


# Compter le nombre de lignes où la valeur de la colonne 'true' est différente de 'both'
product_test = product[product['true'] != 'both']
print(product_test.shape)
product_test.head()


# <h4 style="border-left: 5px solid #0074CC; font-weight: bold; color: #0060A8; padding-left: 10px;">5.2.3 - Vérifier les valeurs différentes de "both"</h4>
# <hr style="border: 1px solid #0074CC;">

# In[35]:


product_test = product[product['true'] == 'left_only']
print(product_test.shape)
product_test.head()


# In[36]:


null_count = product_test[product_test['id_web'].isnull()]
print(null_count.shape)
null_count.head()


# In[37]:


web_notnull = product_test[product_test['id_web'].notnull()]
print(web_notnull.shape)
web_notnull.head()


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">5.3 - Nettoyage des données</h3>
# <hr style="border: 1px solid #0074CC;">

# In[38]:


product = product[product['true'] == 'both']
print(product.shape)
product.head()


# <div style="border: 2px solid #001F3F; background-color: #77B5FE; padding: 10px; text-align: center;">
#     <h2 style="font-weight: bold; color: #001F3F;">Etape 6 - Chiffre d'affaire par produit et total </h2>
# </div>

# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">6.1 - Chiffre d'affaire par produit</h3>
# <hr style="border: 1px solid #0074CC;">

# In[39]:


# Calculer le chiffre d'affaires par produit
product['chiffre_affaires'] = product['total_sales'] * product['price']

# Afficher le chiffre d'affaires par produit
print(product[['product_id', 'chiffre_affaires']])


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">6.2 - Chiffre d'affaire total</h3>
# <hr style="border: 1px solid #0074CC;">

# In[40]:


# Calculer le chiffre d'affaires total réalisé en ligne
chiffre_affaires_total = product['chiffre_affaires'].sum()

# Afficher le chiffre d'affaires total en euros
print(f"Le chiffre d'affaires total réalisé en ligne est de : {chiffre_affaires_total} euros")


# <div style="border: 2px solid #001F3F; background-color: #77B5FE; padding: 10px; text-align: center;">
#     <h2 style="font-weight: bold; color: #001F3F;">Etape 7 - Detection d’éventuelles valeurs aberrantes sur les prix produit </h2>
# </div>

# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">7.1 - Détection des outliers</h3>
# <hr style="border: 1px solid #0074CC;">

# In[41]:


import matplotlib.pyplot as plt
import numpy as np

# Détection des outliers avec la règle de l'IQR
Q1 = product['price'].quantile(0.25)
Q3 = product['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 -(1.5 * IQR)
upper_bound = Q3 +(1.5 * IQR)
outliers = product[(product['price'] < lower_bound) | (product['price'] > upper_bound)]

# Lister les outliers
print("Outliers détectés :")
print(outliers['price'])


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">7.2 - Boxplot des prix des produits</h3>
# <hr style="border: 1px solid #0074CC;">

# In[42]:


# Représentation graphique
plt.figure(figsize=(10, 6))
product['price'].plot(kind='box')
plt.title("Boxplot des Prix des Produits")
plt.ylabel("Prix")
plt.show()


# <h3 style="border-left: 5px solid #0074CC; font-weight: bold; color: #ED0010; padding-left: 10px;">7.2 - Scatter plot des prix des produits</h3>
# <hr style="border: 1px solid #0074CC;">

# In[43]:


only = product[(product['price'] < upper_bound) & (product['price'] > lower_bound)]
# Ajoutez les outliers au scatter plot en utilisant une couleur différente
plt.scatter(only['price'].index, only['price'].values, c='blue')
plt.scatter(outliers['price'].index, outliers['price'].values,c='red')
plt.show()


# In[ ]:




