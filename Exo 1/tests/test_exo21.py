# test de # Créer une application Python qui utilise la reconnaissance optique de caractères (OCR) pour lire des énigmes à partir d'images et fournir les réponses correspondantes.
#
# def extract_string_details(phrase):
#     return {
#         'first_6': phrase[:6],
#         'last_9': phrase[-9:],
#         'slice_13_38': phrase[13:38].lstrip(),
#         'reversed': phrase[::-1]
#     }

from exo21 import extract_string_details

def test_extract_string_details():
    phrase = "Python est un langage de programmation puissant et facile à apprendre"
    expected_results = {
        'first_6': "Python",
        'last_9': "apprendre",  # Assurez-vous que ceci correspond à la fin de votre chaîne 'phrase'.
        'slice_13_38': " langage de programmation",  # Supprimez l'espace au début si votre chaîne commence directement par 'langage'
        'reversed': "erdnerppa à elicaf te tnassiup noitammargorp ed egagnal nu tse nohtyP",  # Assurez-vous que cette chaîne est exactement l'inverse de 'phrase'.
    }

    results = extract_string_details(phrase)

    for key in expected_results:
        assert results[key] == expected_results[key], f"Erreur dans {key}"