from exo2 import extract_string_details


def test_extract_string_details():
    phrase = "Python est un langage de programmation puissant et facile à apprendre"
    expected_results = {
        'first_6': "Python",
        'last_9': "apprendre",
        'slice_13_38': " langage de programmation",
        'reversed': "erdnerppa à elicaf te tnassiup noitammargorp ed egagnal nu tse nohtyP",
    }

    results = extract_string_details(phrase)

    for key in expected_results:
        assert results[key] == expected_results[key], f"Erreur dans {key}"
