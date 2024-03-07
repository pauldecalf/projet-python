# Écrivez un programme qui construit un arbre binaire et imprime ses éléments en ordre préfixé.

def pre_order_traversal(tree):
    if tree:
        print(tree[0], end=' ')
        pre_order_traversal(tree[1])
        pre_order_traversal(tree[2])


