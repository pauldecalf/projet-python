# test de # Écrivez un programme qui construit un arbre binaire et imprime ses éléments en ordre préfixé.
#
# def pre_order_traversal(tree):
#     if tree:
#         print(tree[0], end=' ')
#         pre_order_traversal(tree[1])
#         pre_order_traversal(tree[2])

from exo21 import pre_order_traversal
def test_pre_order_traversal(capsys):
    tree = ['A', ['B', ['D', [], []], ['E', [], []]], ['C', ['F', [], []], []]]
    pre_order_traversal(tree)
    captured = capsys.readouterr()
    assert captured.out == 'A B D E C F '
    tree = ['A', ['B', [], []], ['C', [], []]]
    pre_order_traversal(tree)
    captured = capsys.readouterr()
    assert captured.out == 'A B C '
    tree = ['A', [], []]
    pre_order_traversal(tree)
    captured = capsys.readouterr()
    assert captured.out == 'A '
    tree = []
    pre_order_traversal(tree)
    captured = capsys.readouterr()
    assert captured.out == ''
    tree = ['A', ['B', [], []], ['C', [], []]]
    pre_order_traversal(tree)
    captured = capsys.readouterr()
    assert captured.out == 'A B C '
    tree = ['A', ['B', ['D', [], []], ['E', [], []]], ['C', ['F', [], []], []]]
    pre_order_traversal(tree)
    captured = capsys.readouterr()
    assert captured.out == 'A B D E C F '
    tree = ['A', ['B', ['D', [], []], ['E', [], []]], ['C', ['F', [], []], []]]
    pre_order_traversal(tree)
    captured = capsys.readouterr()
    assert captured.out == 'A B D E C F '
    tree = ['A', ['B', ['D', [], []], ['E', [], []]], ['C', ['F', [], []], []]]
    pre_order_traversal(tree)
    captured = capsys.readouterr()
    assert captured.out == 'A B D E C F '
    tree = ['A', ['B', ['D', [], []], ['E', [], []]], ['C', ['F', [], []], []]]
    pre_order_traversal(tree)
    captured = capsys.readouterr()
    assert captured.out == 'A B D E C F '
    tree = ['A', ['B', ['D', [], []], ['E', [], []]], ['C', ['F', [], []], []]]
    pre_order_traversal(tree)
