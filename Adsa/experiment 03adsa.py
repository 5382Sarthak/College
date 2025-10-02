class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Insertion
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

# Searching
def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Traversals
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

# Find minimum node
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Deletion
def delete_node(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # Node with one or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # Node with two children
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)
    return root

# Main program with user input
def main():
    root = None
    while True:
        print("\nBinary Search Tree Operations:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Inorder Traversal")
        print("5. Preorder Traversal")
        print("6. Postorder Traversal")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            n = int(input("How many keys do you want to insert? "))
            for _ in range(n):
                key = int(input("Enter key to insert: "))
                root = insert(root, key)
        elif choice == 2:
            key = int(input("Enter key to search: "))
            found = search(root, key)
            print("Found!" if found else "Not Found!")
        elif choice == 3:
            key = int(input("Enter key to delete: "))
            root = delete_node(root, key)
        elif choice == 4:
            print("Inorder Traversal: ", end="")
            inorder(root)
            print()
        elif choice == 5:
            print("Preorder Traversal: ", end="")
            preorder(root)
            print()
        elif choice == 6:
            print("Postorder Traversal: ", end="")
            postorder(root)
            print()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
