#Created By Cleon

import math

#Creation of a python node, this node entails a data and next pointer which points to the memory address of the next value in the linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

#This is the creation of the linked list, this list must have a head which begins the list
class LinkedList:
    def __init__(self):
        self.head = None

#This functions inserts data at the begining of the linked list
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

#This function prints data in the linked list
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

#This function inserts data at the end of the lined list
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

#This function inserts values at the end of the linked list
    def insert_values_at_end(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

#This function inserts values at the end of the linked list
    def insert_values_at_begining(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_begining(data)

#This function gets and returns the number of items in the linked list
    def get_length(self):
        count =0
        itr= self.head
        while itr:
            count+=1
            itr = itr.next
        return count
#This function removes data at a specified index in the lined list
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
#This function prints previous data to a specified index in the linked list
    def print_prev(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception ("Index Out Of Range")
        if index==0:
            print("No previous node located")
            return

        count = 0
        itr = self.head
        while itr:
            if count== index-1:
                print(str(itr.data)+'<-- Previous')
            count +=1
            itr= itr.next
        
#This function inserst data at a specified index in the linked list
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
    link.print_prev(2)
    link.print()
    print("length: ",link.get_length())
