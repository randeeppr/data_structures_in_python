#!/usr/bin/python3
# 
# Array implementation using list
#
import sys

class my_array:

  def __init__(self,size,elements=[]):
    self.size = size
    self.items =list()
    if len(elements) > size:
      print("Initializaion failed. More elements than Array size.")
      exit(2)
    if elements:
      for element in elements:
        self.items.append(element)

  def check_empty(self):
    """
    Check if the array is empty or not
    """  
    if len(self.items):
       return False
    else:
       return True

  def insert_element_front(self,new_value):
    """
    Insert element in front of the array
    """  
    if len(self.items) >= self.size:
      print("Array full. Can not insert more items")
    else:
      temp = list()
      temp.insert(0,new_value)
      for index,value in enumerate(self.items):
        temp.insert(index+1,value)
      return my_array(self.size,temp)

  def insert_element_end(self,new_value):
    """
    Insert an element at the end of the array
    """
    if len(self.items) >= self.size:
      print("Array full. Can not insert more items")
    else:
      self.items.insert(len(self.items),new_value)
    return self

  def insert_element_beforeIndex(self,index,value):
    """
    Insert new element before an index n
    """
    if len(self.items) >= self.size:
      print("Array full. Can not insert more items")
    else:
      temp = list()
      for i,v in enumerate(self.items):
        if i >= index:
          if i == index:
             temp.insert(i,value)
             temp.insert(i+1,v)
          else:
             temp.insert(i+1,v)             
        else:
          temp.insert(i,v)
      return my_array(self.size,temp)

  def insert_element_afterIndex(self,index,value):
    """
    Insert new element after an index n
    """
    if len(self.items) >= self.size:
      print("Array full. Can not insert more items")
    else:
      temp = list()
      for i,v in enumerate(self.items):
        if i > index:
          if i == index+1:
           temp.insert(i,value)
           temp.insert(i+1,v)
          else:
             temp.insert(i+1,v)             
        else:
          temp.insert(i,v)
      return my_array(self.size,temp)

  def remove_element_atIndex(self,index):
    """
    Remove new element after an index n
    """
    if self.check_empty() == True:
      print("Error. Array is empty")
    else:
      temp = list()
      for i,v in enumerate(self.items):
        if i >= index:
          if i == index:
            pass
          else:
             temp.insert(i-1,v)             
        else:
          temp.insert(i,v)
      return my_array(self.size,temp)

  def check_length(self):
    """
    Prints the length of the current array
    """
    return len(self.items)

  def search_element(self,element):
    """
    Returns the index of the element in the array
    """
    if element in self.items:
      return self.items.index(element)
    else:
      print("Error. Element not found")

  def print_array(self):
    """
    Returns the current items in the array
    """
    return self.items

print("Array should be 1,2,3")
abc = my_array(10,[1,2,3])
print(abc.print_array())
print("Array is not empty")
print(abc.check_empty())
abc = abc.insert_element_front(6)
print("Array should be 6,1,2,3")
print(abc.print_array())
abc = abc.insert_element_end(7)
print("Array should be 6,1,2,3,7")
print(abc.print_array())
abc = abc.insert_element_beforeIndex(3,8)
print("Array should be 6,1,2,8,3,7")
print(abc.print_array())
abc = abc.insert_element_afterIndex(4,9)
print("Array should be 6,1,2,8,3,9,7")
print(abc.print_array())
abc = abc.remove_element_atIndex(2)
print("Array should be 6,1,8,3,9,7")
print(abc.print_array())
print("Length is : 6")
print(abc.check_length())
print("Index of 9 is 4")
print(abc.search_element(9))
