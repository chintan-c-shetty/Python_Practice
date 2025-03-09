class Queue:

    def __init__(self):
        self.que=[]
    def enqueue(self,x):
        self.que.append(x)
    def dequeue(self):
        if len(self.que)>0:
            front=self.que[0]
            self.que.remove(front)
            return front
        print("queue is empty")
    def display(self):
        print(self.que)
q1=Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.display()



    
