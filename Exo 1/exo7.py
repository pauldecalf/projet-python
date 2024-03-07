# Écrivez un programme qui inverse l'ordre des éléments dans chaque tuple d'une liste de tuples.

def reverse_tuple_elements(list_of_tuples):
    # Inverse l'ordre des éléments dans chaque tuple
    reversed_tuples = [tuple(reversed(t)) for t in list_of_tuples]

    # Retourne la liste de tuples avec les éléments inversés
    return reversed_tuples