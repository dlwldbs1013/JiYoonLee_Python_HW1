#!/usr/bin/env python
# coding: utf-8

# # 단순연결리스트

# In[4]:


import  random

def getNumber():
    return random.randrange(1,46) #1~45

lotto=[]
num=0

print("로또 추첨을 시작합니다.\n");
while True :
    num=getNumber()

    if lotto.count(num) ==0 :
        lotto.append(num)

    if len(lotto)>=6 :
        break

print("추첨된 로또 번호 : " ,end="")
for i in range(0,6) :
    print("%d " % lotto[i], end="")


# # 원형연결리스트

# In[7]:


import random
import math

class Node():
    def __init__(self) :
        self.data =None
        self.link =None
        
def printStores(start) :
    current=start
    if current ==None :
        return
    
    while current.link !=head :
        current = current.link
        x,y = current.data[1:]
        print(current.data[0],'편의점 거리:',math.sqrt(x*x+y*y))
    print()
    
def makeStoreList(store) :
    global memory, head, current, pre
    
    node = Node()
    node.data=store
    memory.append(node)
    
    if head == None:
        node.link = head
        return
    
    nodeX,nodeY=node.data[1:]
    nodeDist=math.sqrt(nodeX*nodeX+nodeY*nodeY)
    headX,headY=head.data[1:]
    headDist=math.sqrt(headX*headX+headY*headY)
    
    if headDist>nodeDist :
        node.link=head
        last=head
        while last.link !=head :
            last=last.link
        last.link=node
        head=node
        return
    
    current=head
    while current.link !=head:
        pre=current
        current=current.link
        currX,currY=current.data[1:]
        currDist=math.sqrt(currX*currX+currY*currY)
        if currDist>nodeDist :
            pre.link=node
            node.link=current
            return
        
    current.link=node
    node.link=head
    
memory=[]
head,current,pre=None,None,None

if __name__ == "__main__":
    
    storeArray=[]
    storeName='A'
    for _in range(10):
        store =(storeName,random.randint(1,100),random.randint(1,100))
        storeArray.append(store)
        storeName=chr(ord(storeName)+1)
        
        for store in storeArray:
            makeStoreList(store)
            
            printStores(head)


# # 스택

# In[ ]:


##함수 선언 부분 #
def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else:
        return False

def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        return
    top += 1
    stack[top] = data

def pop() :
    global SIZE, stack, top
    if (isStackEmpty()) :
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :
    global SIZE, stack, top
    if (isStackEmpty()):
        return None
    return stack[top]

SIZE = 100
stack = [None for in range (SIZE)]
top = -1


if __name__=="__main__"


    with open("진달래꽃.txt", 'r', encoding='UTF8') as rfp:
        lineAry = rfp.readlines ()
    print("----- 원본 -----")
    for line in lineAry :
        push(line)
        print(line, end =' ')
    print()
    
    print("---거꾸로 처리된 결과---")
    while True:
        line = pop()
        if line == None :
            break
            
    miniStack = [None for _ in range (len(line))]
    miniTop = -1
    
    for ch in line :
        miniTop += 1
        miniStack[miniTop] = ch
        
        while True:
            if miniTop == -1 :
                break
            ch = miniStack[miniTop]
            miniTop -= 1
            print(ch, end = ' ')


# # 큐

# In[ ]:


def isQueueFull() :
    global SIZE, queue, front, rear 
    if ((rear+1) % SIZE == front):
        return True 
    else :
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear 
    if (front == rear):
        return True 
    else :
        return False

def enQueue (data):
    global SIZE, queue, front, rear 
    if (isQueueFull()) :
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear+1) % SIZE
    queue[rear] = data
    
def deQueue () :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print(”큐가 비었습니다.")
        return None
    return queue[(front+1) % SIZE]
              
def calcTime ()
    global SIZE, queue, front, rear
    timeSum = 0
    for i in range((front+1) % SIZE, (rear+1) % SIZE)
        timeSum += queue[i][1]
            return timeSum
              
              
SIZE = 6
queue = [None for _ in range(SIZE)]
front = rear = 0
              
if __name__=="__main__":
            waitCall=[('사용',9),('고장',3),('환불',4),('환불',4),('고장',3)]
              
            for call in waitCall :
                print("귀하의 대기 예상시간은 ", calcTime (), "분입니다.")
                print("현재 대기 콜-> ", queue)
                enQueue (call)
                print()
              
        print("최종 대기 콜 -> ", queue)
        print("프로그램 종료!")


# In[ ]:




