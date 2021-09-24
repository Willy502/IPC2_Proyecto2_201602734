from .g_node import *

class GList:

    def __init__(self):
        self.first = None

    def insert(self, content):
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
