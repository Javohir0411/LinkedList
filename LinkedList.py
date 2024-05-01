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

    def count_elements(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def separate_elements(self, elements):
        separated_lists = {}
        for element in elements:
            data_type = type(element)
            if data_type in separated_lists:
                separated_lists[data_type].append(element)
            else:
                separated_lists[data_type] = LinkedList()
                separated_lists[data_type].append(element)
        return separated_lists

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end='\t')
            temp = temp.next

    # def merge_lists(self, list2):
    #     temp = self.head
    #     while temp.next:
    #         temp = temp.next
    #     temp.next = list2.head

    def delete(self, data):
        print('All Nodes: ')
        self.print_list()
        x = self.head
        while x.next:
            if x.next.data == data:
                x.next = x.next.next
                self.print_list()
                return 'Successfully deleted'
            x = x.next
        return 'No Node Found'

    def index_of_element_in_linked_list(head, target):
        index = 0
        current = head

        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1

        return -1

    def linked_list_to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
