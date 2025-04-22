
# Queue Implementation Using Python

class Queue:

    def __init__(self):
        # Initialize a Queue Data Structure
        self.queue = []

    def add_element(self, data):
        # Add the Element
        self.queue.append(data)

    def remove_element(self):
        # Remove Element
        if self.is_empty():
            return None  # Return None if the queue is empty
        else:
            return self.queue.pop(0)  # Remove from the front of the queue

    def is_empty(self):
        # To Check Empty 
        return len(self.queue) == 0

    def size(self):
        # Find the Length of the Queue
        return len(self.queue)

    def display(self):
        # Show the elements of the queue
        print("Aditya")
        return self.queue
    


