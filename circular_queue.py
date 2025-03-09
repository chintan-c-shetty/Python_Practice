class cqueue:#circular queue
    def __init__(self,maxx):
        self.capacity=maxx
        self.queue=[0]*maxx
        self.front=-1
        self.rear=-1
    def is_full(self):
        if (self.rear+1)%self.capacity==self.front:
            return True
        return False
    def is_empty(self):
        if self.front==-1:
            return True
        return False
    def enqueue(self,ele):
        if self.is_full():
            print("queue is full!")
            return
        if self.is_empty():
            self.front+=1
        self.rear=(self.rear+1)%self.capacity
        self.queue[self.rear]=ele

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty !")
            return
        self.queue[self.front]=0
        if self.front==self.rear:
            #last element
            self.front=-1
            self.rear=-1
        else:
            self.front=(self.front+1)%self.capacity
    def display(self):
        if self.is_empty():
            print("Queue is empty !")
        else:
            print(self.queue)
q=cqueue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()

q.enqueue(6)
q.enqueue(7)
q.display()
        


        

