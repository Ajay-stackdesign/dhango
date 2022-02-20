# # you can use this to sort strings too
# # def bubble_sort(elements):
# #     size = len(elements)
# #
# #     for i in range(size-1):
# #         swapped = False
# #         for j in range(size-1-i):
# #             if elements[j] > elements[j+1]:
# #                 tmp = elements[j]
# #                 elements[j] = elements[j+1]
# #                 elements[j+1] = tmp
# #                 swapped = True
# #
# #         if not swapped:
# #             break
# #
# #
# # if __name__ == '__main__':
# #     elements = [5,9,2,1,67,34,88,34]
# #     elements = [1,2,3,4,2]
# #     elements = ["mona", "dhaval", "aamir", "tina", "chang"]
# #
# #     bubble_sort(elements)
# #     print(elements)
#
# # def bubble_sort(candles):
# #     size = len(candles)
# #
# #     for i in range(size-1):
# #         swapped = False
# #         for j in range(size-1-i):
# #             if candles[j] > candles[j+1]:
# #                 temp = candles[j]
# #                 candles[j] = candles[j + 1]
# #                 candles[j+1] = temp
# #                 swapped = True
# #         if not swapped:
# #             break
# #
# #     print(candles[1])
# #
# # if __name__ == '__main__':
# #     can = [3,2,1,3]
# #     bubble_sort(can)
# #     # print(can)

def bubbleSort(self, arr, n):
    # code here
    size = len(n)

    for i in range(size - 1):
        swapped = False

        for j in range(size - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True
            if not swapped:
                break
#
# # class BinarySearchTreeNode:
# #     def __init__(self, data):
# #         self.data = data
# #         self.left = None
# #         self.right = None
# #
# #     def add_child(self, data):
# #         if data == self.data:
# #             return # node already exist
# #
# #         if data < self.data:
# #             if self.left:
# #                 self.left.add_child(data)
# #             else:
# #                 self.left = BinarySearchTreeNode(data)
# #         else:
# #             if self.right:
# #                 self.right.add_child(data)
# #             else:
# #                 self.right = BinarySearchTreeNode(data)
# #
# #
# #     def search(self, val):
# #         if self.data == val:
# #             return True
# #
# #         if val < self.data:
# #             if self.left:
# #                 return self.left.search(val)
# #             else:
# #                 return False
# #
# #         if val > self.data:
# #             if self.right:
# #                 return self.right.search(val)
# #             else:
# #                 return False
# #
# #     def in_order_traversal(self):
# #         elements = []
# #         if self.left:
# #             elements += self.left.in_order_traversal()
# #
# #         elements.append(self.data)
# #
# #         if self.right:
# #             elements += self.right.in_order_traversal()
# #
# #         return elements
# #
# #
# # def build_tree(elements):
# #     print("Building tree with these elements:",elements)
# #     root = BinarySearchTreeNode(elements[0])
# #
# #     for i in range(1,len(elements)):
# #         root.add_child(elements[i])
# #
# #     return root
# #
# # if __name__ == '__main__':
# #     # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
# #     # country_tree = build_tree(countries)
# #     #
# #     # print("UK is in the list? ", country_tree.search("UK"))
# #     # print("Sweden is in the list? ", country_tree.search("Sweden"))
# #
# #     numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
# #     print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
# #
# class BinarySearchTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def add_child(self, data):
#         if data == self.data:
#             return # node already exist
#
#         if data < self.data:
#             if self.left:
#                 self.left.add_child(data)
#             else:
#                 self.left = BinarySearchTreeNode(data)
#         else:
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.right = BinarySearchTreeNode(data)
#
#
#     def search(self, val):
#         if self.data == val:
#             return True
#
#         if val < self.data:
#             if self.left:
#                 return self.left.search(val)
#             else:
#                 return False
#
#         if val > self.data:
#             if self.right:
#                 return self.right.search(val)
#             else:
#                 return False
#
#     def in_order_traversal(self):
#         elements = []
#         if self.left:
#             elements += self.left.in_order_traversal()
#
#         elements.append(self.data)
#
#         if self.right:
#             elements += self.right.in_order_traversal()
#
#         return elements
#
#     def delete(self, val):
#         if val < self.data:
#             if self.left:
#                 self.left = self.left.delete(val)
#         elif val > self.data:
#             if self.right:
#                 self.right = self.right.delete(val)
#         else:
#             if self.left is None and self.right is None:
#                 return None
#             elif self.left is None:
#                 return self.right
#             elif self.right is None:
#                 return self.left
#
#             min_val = self.right.find_min()
#             self.data = min_val
#             self.right = self.right.delete(min_val)
#
#         return self
#
#     def find_max(self):
#         if self.right is None:
#             return self.data
#         return self.right.find_max()
#
#     def find_min(self):
#         if self.left is None:
#             return self.data
#         return self.left.find_min()
#
#
# def build_tree(elements):
#     print("Building tree with these elements:",elements)
#     root = BinarySearchTreeNode(elements[0])
#
#     for i in range(1,len(elements)):
#         root.add_child(elements[i])
#
#     return root
#
# if __name__ == '__main__':
#     numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
#     numbers_tree.delete(20)
#     print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]
#
#     numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
#     numbers_tree.delete(9)
#     print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]
#
#     numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
#     numbers_tree.delete(17)
#     print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]

# def bubble_sort(data):
#     size = len(data)
#
#     for i in range(size - 1):
#         swapped = False
#         for j in range(size - i - 1):
#             if data[j] > data[j + 1]:
#                 temp = data[j]
#                 data[j] = data[j + 1]
#                 data[j + 1] = temp
#                 swapped = True
#
#         if not swapped:
#             # break

def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break

element = [12, 23, 25, 1, 43, 54, 65]
(bubble_sort(element))
print(element)
