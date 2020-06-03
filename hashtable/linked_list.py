class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return f'Node({repr(self.value)})'

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        r = ''
        curr = self.head
        while curr is not None:
            r += ' -> '  

        curr = curr.next
    
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    def find(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    def delete(self, value):
        curr = self.head
        if curr.value == value:
            self.head == self.head.next
            return curr
        prev = curr
        curr = curr.next

        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                return curr
            else:
                prev = prev.next
                curr = curr.next
        return None
        
if __name__ == "__main__":
    ll = LinkedList()
