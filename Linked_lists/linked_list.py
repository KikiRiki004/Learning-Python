# Define Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

# Define LinkedList
class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    # Representation
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Traversing/Iterating
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Inserting new node

    # Inserting in the Beginning
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # Inserting in the End
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    # Inserting Between 2 Nodes

    # Inserting After an existing node
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    # Inserting Before an existing node
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    # Remove Node
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

# Tests
llist = LinkedList()
print(llist) # None

first_node = Node("a")
llist.head = first_node
print(llist) # a -> None

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist) # a -> b -> c -> None

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist) # a -> b -> c -> d -> e -> None

for node in llist:
    print(node) # a /n b /n c /n d /n e

llist = LinkedList()
print(llist) # None
llist.add_first(Node("b"))
print(llist) # b -> None
llist.add_first(Node("a"))
print(llist) # a -> b -> None


