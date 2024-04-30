class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.sum = 0
        self.count = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        if type(data) == int or type(data) == float:
            self.sum += data
        self.count += 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end='\t')
            temp = temp.next

    def merge_lists(self, list2):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = list2.head

    # def summa(self):
    #     temp = self.head
    #     sum = 0
    #     while temp:
    #         if type(temp.data) is int:
    #             sum += temp.data
    #         temp = temp.next
    #     return sum
