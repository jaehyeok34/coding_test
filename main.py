def preorder(key: str):
    if key == ".":
        return

    print(key, end="")
    preorder(tree[key][0])
    preorder(tree[key][1])


def inorder(key):
    if key == ".":
        return

    inorder(tree[key][0])
    print(key, end="")
    inorder(tree[key][1])


def postorder(key):
    if key == ".":
        return

    postorder(tree[key][0])
    postorder(tree[key][1])
    print(key, end="")


if __name__ == '__main__':
    n = int(input())
    tree = dict()
    for _ in range(n):
        inputs = input().split()
        tree[inputs[0]] = inputs[1:]

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
