# program to create a single list

# algorithm:
# class node:
# create a class node which has two attributes data and next. next is a pointer to the next node in the list
# 1) create another class which has two attributes
# that is head and tail

# 3) create a addNote()  will add a new node in the list
# a)create a new node
# b) it checks, whether the head is equal to null which means the list is empty
# c) if the list is empty both head and tail will point to the newly added node
# d) if the lisyt is not empty the new node will be added to end of the list such that tails next will pointer to a
# newly addded node. this new node will become the new tail of the list

# 4)  countNodes() will count the nodes present in the list:
# Define a node current which will initially point to the head of the list.
# Declare and initialize a variable count to 0.
# Traverse through the list till current point to null.
# Increment the value of count by 1 for each node encountered in the list.
# 5) display() will display the nodes present in the list:
# Define a node current which will initially point to the head of the list.
# Traverse through the list till current points to null.
# Display each node by making current to point to node next to it in each iteration.


# class Node:
#     def __init__(self, data):
#         self.data = data;
#         self.next = None
#
# class CountNodes:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def addNode(self, data):
#         newNode = Node(data)
#
#         if (self.head == None):
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#
#     def CountNodes(self):
#
#         count = 0
#
#         current = self.head
#
#         while(current != None):
#             count +=1
#             current = current.next
#
#     def display(self):
#         current = self.head
#
#         if(self.head == None):
#             print("list is empty")
#             return
#         while(current != None):
#             print(current.data)
#             current = current.next
#
# slist = CountNodes()
# data= [1,2,3,4]
# slist.addNode(data)
# slist.addNode(2)
#
# slist.addNode(3)
#
# slist.display()
#
# print("Count of nodes present in the list: " + str(slist.countNodes()));

# Represent a node of the singly linked list
# class Node:
#     def __init__(self, data):
#         self.data = data;
#         self.next = None;
#
#
# class CountNodes:
#     # Represent the head and tail of the singly linked list
#     def __init__(self):
#         self.head = None;
#         self.tail = None;
#
#         # addNode() will add a new node to the list
#
#     def addNode(self, data):
#         # Create a new node
#         newNode = Node(data);
#
#         # Checks if the list is empty
#         if (self.head == None):
#             # If list is empty, both head and tail will point to new node
#             self.head = newNode;
#             self.tail = newNode;
#         else:
#             # newNode will be added after tail such that tail's next will point to newNode
#             self.tail.next = newNode;
#             # newNode will become new tail of the list
#             self.tail = newNode;
#
#             # countNodes() will count the nodes present in the list
#
#     def countNodes(self):
#         count = 0;
#         # Node current will point to head
#         current = self.head;
#
#         while (current != None):
#             # Increment the count by 1 for each node
#             count = count + 1;
#             current = current.next;
#         return count;
#
#         # display() will display all the nodes present in the list
#
#     def display(self):
#         # Node current will point to head
#         current = self.head;
#
#         if (self.head == None):
#             print("List is empty");
#             return;
#         print("Nodes of singly linked list: ");
#         while (current != None):
#             # Prints each node by incrementing pointer
#             print(current.data),
#             current = current.next;
#
#
# sList = CountNodes();
#
# # Add nodes to the list
# sList.addNode(1);
# sList.addNode(2);
# sList.addNode(3);
# sList.addNode(4);
#
# # Displays the nodes present in the list
# sList.display();
#
# # Counts the nodes present in the given list
# print("Count of nodes present in the list: " + str(sList.countNodes()));

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class CountNodes:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def addNode(self,data):
#         newNode = Node(data)
#         if(self.head == None):
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#
#     def countNodes(self):
#         count = 0
#         current = self.head
#
#         while(current != None):
#             count +=1
#             current= current.next
#         return count
#
#     def display(self):
#
#         current = self.head
#
#         if(self.head == None):
#             print("list is empty")
#             return
#         while(current != None):
#             print(current.data)
#             current = current.next
#
# list = CountNodes()
# list.addNode(1)
# list.addNode(3)
# list.addNode(4)
# list.addNode(4)
# list.display()
#
# print("countnodes:", list.countNodes())

# print middle Number of the element for eampe 1->2->3->4->5  middle: 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CountNode:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):
        newNode = Node(data)

        if (self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def countNodes(self):
        count = 0

        current = self.head
        if (self.head == None):
            return

        while (current != None):
            count += 1
            current = current.next
        return count

    @property
    def middleNumber(data):
        size = len(data)

        middle_number = size // 2

        return middle_number

    def display(self):

        current = self.head

        if (self.head == None):
            print("List is empty")
            return

        print("Linkedlist is there")
        while (current != None):
            print(current.data)

            current = current.next


list = CountNode()

list.addNode(1)
list.addNode(2)
list.addNode(3)
list.addNode(4)

list.display()
# data = [1,2,3,4,5]
list.middleNumber


