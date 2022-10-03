#!/usr/bin/env python
# coding: utf-8

# ## 최대한 찾아서 해봤는데 두개를 합치진 못했어요

# In[6]:


def add_data(friend):
    katok.append(None)
    kLen=len(katok)
    katok[kLen-1]=friend
    
def insert_data(position,friend):
    if position <0 or position > len(katok):
        print("범위를 벗어났습니다")
        return
    katok.append(None)
    kLen=len(katok)
    
    for i in range(kLen-1,position,-1):
        katok[i]=katok[i-1]
        katok[i-1]=None
        
        katok[position]=friend
        
def delete_data(position):
    if position<0 or position> len(katok):
        print("삭제 범위를 벗어났습니다")
        return
    
    kLen=len(katok)
    katok[position]=None
    
    for i in range(position+1,kLen):
        katok[i-1]=katok[i]
        katok[i]=None
        
    del(katok[kLen-1])
    
katok=[]
select=-1


if __name__=="__main__":
    while(select !=3):
        select = int(input("선택하세요(!:추가,2:삭제,3:종료)-->"))
        
        if(select==1):
            data=input("추가할 데이터: ")
            add_data(data)
            print(katok)
            
        elif(select==2):
            pos=int(input("삭제할 위치: "))
            delete_data(pos)
            print(katok)
        elif(select==3):
            print(katok)
            exit
        else:
            print("1~3 중 하나를 입력하세요")
            continue


# In[7]:


def input_data(friend, count):
  if count <0:
    print("연락 횟수는 0과 같거나 커야합니다.\n다시 입력해주세요.")
    return 
 
  cnt = 0
  lis.append(None) 
  list_len = len(lis)
 

  for i in range(list_len-1,0,-1):
 
    if count >= lis[i-1][1]:
      lis[i]=lis[i-1]
      lis[i-1] = None
      cnt +=1
    else : break
 
  position = list_len-cnt-1
  lis[position]=(friend,count)
 
lis = [('다현',200),('정연',150),("쯔위",90),('사나',30),('지효',15)]
if __name__=="__main__":
  while True:
      print("종료를 원하면 엔터를 눌러주세요")
      name = input("추가할 친구--> ")
 
      
      if name == '':
        break;
      
      cnt = int(input("추가할 데이터--> "))
      input_data(name, cnt)
      print(lis)


# In[ ]:




