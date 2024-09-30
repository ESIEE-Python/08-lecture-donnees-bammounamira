"""Ce module contient des fonctions pour lire et manipuler des fichiers"""
FILENAME = "listes.csv"
"""Ce module"""
def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    data =[]
    with open(filename, 'r', encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            line.strip()
            if line:
                data.append(list(map(int,line.split(';'))))
    return data

def get_list_k(data, k):
    """retourne retourne la kième liste

    Args:
        date: la liste de listes d'entiers 
        k: l'indice de la liste à retourner 

    Returns:
        list: la k-ième liste d'entiers
    """
    l = []
    for element in data[k]:
        l.append(element)
    return l

def get_first(l):
    """retourne le premier élément d'une liste"""
    return l[0]

def get_last(l):
    """retourne le dernier élément d'une liste"""
    return l[-1]

def get_max(l):
    """retourne le maximum d'une liste"""
    return max(l)

def get_min(l):
    """retourne le minimum d'une liste"""
    return min(l)

def get_sum(l):
    """retourne la somme d'une liste"""
    return sum(l)


#### Fonction principale

def main():
    """Fonction principale qui teste les autres fonctions en utilisant
    les données lues à partir d'un fichier.
    La fonction lit les données depuis 'listes.csv',
    puis utilise les fonctions secondaires
    pour afficher la k-ième liste, son premier élément,
    dernier élément, maximum, minimum et somme.
    """
    # Lire les données depuis le fichier
    data = read_data(FILENAME)
    # Test des fonctions
    k = 0  # Exemple d'indice pour la liste à récupérer
    print(f"The {k}th list is: {get_list_k(data, k)}")
    l = get_list_k(data, k)
    print(f"First element of the list: {get_first(l)}")
    print(f"Last element of the list: {get_last(l)}")
    print(f"Maximum value of the list: {get_max(l)}")
    print(f"Minimum value of the list: {get_min(l)}")
    print(f"Sum of the list: {get_sum(l)}")

if __name__ == "__main__":
    main()
