# You can remove 'pass' if you written code in the function
# Do NOT use .append() or .pop() inside Enqueue() and Dequeue() - move the pointers yourself.

# Exercise 1
Queue = []
HeadPointer = 0
TailPointer = -1
for i in range(8):
    Queue.append(-1)


def IsEmpty():
    global Queue, HeadPointer, TailPointer
    if HeadPointer > TailPointer:
        return True
    return False

def IsFull():
    global Queue, HeadPointer, TailPointer
    if TailPointer == 7:
        return True
    return False

# Exercise 2
def Enqueue(Item):
    global Queue, HeadPointer, TailPointer
    if IsFull():
        return False
    TailPointer += 1
    Queue[TailPointer] = Item
    return True

# Exercise 3
def Dequeue():
    global Queue, HeadPointer, TailPointer
    if IsEmpty():
        return -1
    x = Queue[HeadPointer]
    HeadPointer += 1
    return x

# Exercise 4
def Peek():
    global Queue, HeadPointer, TailPointer
    if IsEmpty():
        return -1
    return Queue[HeadPointer]

def ShowQueue():
    global Queue, HeadPointer, TailPointer
    if IsEmpty():
        return ""
    s = ""
    for i in range(HeadPointer,TailPointer+1,1):
        s = s + str(Queue[i])
        if i < TailPointer:
            s = s + " "
    return s

# Exercise 5
def Canteen(Commands):
    global Queue, HeadPointer, TailPointer
    HeadPointer = 0
    TailPointer = -1
    lst = []
    for command in Commands:
        if command == "serve":
            y = Dequeue()
            if y != -1:
                lst.append(y)
        else:
            parts = command.split(" ")
            Enqueue(parts[1])
    return lst

