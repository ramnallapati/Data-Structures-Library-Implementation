

# Implement Stack Functions

class Stack:

    def __init__(self):

        # Initialize a Empty stack
        self.stack = []
    
    def add_element(self,data):
        
        # Add the Element
        self.stack.append(data)
       
    
    def remove_element(self):

        # remove the Element
        if self.is_empty():
            raise IndexError("No Element are Present")
        else:
           
            return self.stack.pop()
    
    def top_element(self):

        # see the top Element
        if self.is_empty():
            raise IndexError("No Elements are present")
        else:
            return self.stack[-1]

    def is_empty(self):

        # To Find the Stack with Empty or not

        return len(self.stack) == 0
    
    def _size(self):

        # To get the Size of the Stack

        return len(self.stack)
    
    def display(self):

        # To display the all elements in the Stack is

        print("The Elements in the Stacks is : \n",self.stack)


