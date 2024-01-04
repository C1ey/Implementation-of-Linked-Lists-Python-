import math

class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Lined list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr+=str(itr.data) + '-->'
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

    def insert_values_at_end(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def insert_values_at_begining(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_begining(data)

    def get_length(self):
        count =0
        itr= self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception ("Index Out Of Range")

        if index==0:
            self.head = self.head.next
            return

        count = 0 #In linked lists you have to manually maintain the count to get to the needed index
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break 
            itr = itr.next
            count+=1

    def print_prev(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception ("Index Out Of Range")
        count = self.get_length()
        llstr=''
        itr = self.head
        while itr:
            if count== index-1:
                llstr+=str(itr.data)+'<-- Previous'
                count -=1
        print(llstr)
        

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception ("Index Out Of Range")

        if index==0:
            self.insert_at_begining(data)
            return


        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count+=1


        
if __name__ == '__main__':
    link=LinkedList()
##    link.insert_at_begining(7)
##    link.insert_at_end(100)
##    link.insert_values_at_end([1,2,3,4,5,6,7,8,9])
    link.insert_values_at_begining([1,2,3,4,5,6,7,8,9,9,9])
##    link.remove_at(5)
##    link.insert_at(5,9000)
    #link.print_prev(2)
    link.print()
    print("length: ",link.get_length())
