class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class linkedlist():
    def __init__(self):
        self.head = None
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) +'-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def length(self):
        count =0
        itr = self.head
        while itr:
            count+= 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index<0 or index>=self.length():
            raise Exception("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index<0 or index>=self.length():
            raise Exception("Index out of range")
        if index == 0:
            self.insert_at_begining(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next=node
            itr = itr.next
            count += 1
if __name__ == '__main__':
    my_list = linkedlist()
    my_list.insert_at_begining(1)
    my_list.insert_at_begining(2)
    my_list.insert_at_begining(3)
    my_list.insert_at_begining(4)
    my_list.insert_at_begining(5)
    my_list.insert_at_end(6)
    my_list.insert_at_end(7)
    my_list.insert_at_end(8)
    my_list.insert_at_end(9)
    my_list.insert_at_end(10)
    my_list.print()
    my_list.insert_at(5,14)
    my_list.print()

        
    

