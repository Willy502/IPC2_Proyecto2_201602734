from .g_node import *

class GList:

    def __init__(self):
        self.first = None

    def add(self, content):
        if self.first is None:
            self.first = GNode(content = content)
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = GNode(content = content)

    def size(self):
        length = 0
        current = self.first
        while current != None:
            length += 1
            current = current.next
        return length

    def get(self, position):
        length = 0
        current = self.first
        while current != None:
            length += 1
            if position == length - 1:
                return current.content
            current = current.next
        raise Exception('GList out of range exception')

    def delete(self, position):
        length = 0
        current = self.first
        previous = None

        while current != None:
                
            if position == length:
                if previous is None:
                    self.first = current.next
                    current.next = None
                elif current:
                    previous.next = current.next
                    current.next = None
                return

            length += 1

            previous = current
            current = current.next

        raise Exception('GList out of range exception')

    def update(self, position, content):
        length = 0
        current = self.first
        while current != None:
            length += 1
            if position == length - 1:
                current.content = content
                return
            current = current.next
        raise Exception('GList out of range exception')
