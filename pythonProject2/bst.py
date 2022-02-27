class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.lett.add_child(data)
            else:
                self.left.BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right.BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_transerval(self):
        elements = []

        if self.left:
            elements += self.left.in_order_transerval()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_transerval()

        return elements
def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))