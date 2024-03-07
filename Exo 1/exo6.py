def tuple_with_most_elements(list_of_tuples):
    # Trouve le tuple avec le plus d'éléments
    max_tuple = max(list_of_tuples, key=len)

    # Retourne le tuple avec le plus d'éléments
    return max_tuple