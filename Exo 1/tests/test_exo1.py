from exo1 import count_upper_lower_case

def test_count_upper_lower_case():
    source = "Ceci est un Test de la Chaîne de Caractères!"
    upper, lower = count_upper_lower_case(source)
    assert upper == 4, f"Expected 4 uppercase letters, got {upper}"
    assert lower == 31, f"Expected 31 lowercase letters, got {lower}"
