int_val=4
str_val="bhavani"
flt_val=12.40
print("the interger hash value is :"+ str(hash(int_val)))
print("the string hash value is :" +str(hash(str_val)))
print("the float hash value is :" +str(hash(flt_val)))

 #
def recur_fact(n):
     if n<=0:
         return -1,
     else :
        print(recur_fact (n-1) + recur_fibo(n-2))
nterm=10
if nterm <=0:
              print("please enter positive value")
else :
    print("factorial")
for i in range (nterm):
    print(i)
#
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue (self,item):
          self.items.append(item)
          print(item)
    def dequeue (self):
         return self.items.pop(0)
    def front (self):
        return self.items(len(self.items)-1)
    def size (self):
        return len(self.items)
q=Queue()
print(q.isEmpty(),"-becasuse queue is empty")
print("Enquee")
q.enqueue(17)
q.enqueue(21)
q.enqueue(18)
q.enqueue(19)
print("Front",q.front)
print("Dnquee")
print(q.dequeue())
print(q.dequeue())
print("Size",q.size)
#
Stack = []
Stack.append("a")
Stack.append("b")
Stack.append("c")
Stack.append("d")
print("Intial Stack")
print(Stack)
print("\n  Elements popped from the stack")
print(Stack.pop())
print(Stack.pop())
print(Stack.pop())
print("\n Stack after elemnets popped")
print(Stack)
#
print("List")
list=[1,2,3,"bhavani",4,5,6]
print(list)
print("Set")
set={1,2,3,4,5,6}
print(set)
print("Tuple")
tup=(1,2,3,4,5)
print(tup)
print("Dictionary")
dict={"bhavani":18,"Sureash":20,"Sowndharya":22}
print(dict)
#
a=[1,2,3,3,4,7,8]
print(a)
a.insert(9,11)
print(a)
a.pop(3)
print(a)
i=len(a)
print(i)
#
def LinearSearch(a,key):
    n=len(n)
    for i in range(n):
        if a[i] == key:
            return i;
        return 1
    a=[22,55,77,88,66,99,33]
    k=int(input("Enter the elment :"))
    i = LinearSearch(a,k)
if i == -1:
          print(unsuccesfull)
else:
    print("found:",i+1)
#
def bubbleSort(a):
    n = len(a)
    for i in range(n-2):
        for j in range (n-2-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j] = a[j+1]
                a[j+1]=temp
alist=[22,55,44,33,88,66,77,99]
print("befor sorting:",alist)
bubbleSort(alist)         
print("after sorting:",alist)
#
def SelectionSort(a):
    n = len(a)
    for i in range(n-2):
        min=i
        for j in range (i+1,n-1):
            if a[j]>a[min]:
                temp=a[j]
                a[j] = a[min]
                a[min]=temp
alist=[22,55,44,33,88,66,77,99]
print("befor sorting:",alist)
SelectionSort(alist)         
print("after sorting:",alist)
#
def fibonacci(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]
print(fibonacci(9))
#
def TowerOfHanoi(n,source,destination,auxiliary):
    if n==1:
        print("move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1,source,auxiliary,destination)
    print("move disk " ,n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1,auxiliary,destination,source)
n =4
TowerOfHanoi(n,"A","B","C")
