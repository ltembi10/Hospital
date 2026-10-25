
class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side, current_node=None):
        side = side.lower()

        if side not in ("left", "right"):
            print("Error: Side must be 'left' or 'right'.")
            return False

        if self.root is None:
            print("Error: Tree is empty.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == parent_name:
            if side == "left":
                if current_node.left is not None:
                    print("Error: Left side is occupied.")
                    return False
                current_node.left = DoctorNode(doctor_name)
            else:
                if current_node.right is not None:
                    print("Error: Right side is occupied.")
                    return False
                current_node.right = DoctorNode(doctor_name)

            return True

        if current_node.left is not None:
            if self.insert(parent_name, doctor_name, side, current_node.left):
                return True

        if current_node.right is not None:
            if self.insert(parent_name, doctor_name, side, current_node.right):
                return True

        if current_node is self.root:
            print(f"Error: Doctor '{parent_name}' not found.")

        return False

    def preorder(self, node):
        if node is None:
            return []

        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        if node is None:
            return []

        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


# Test your DoctorTree and DoctorNode classes here.
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))
