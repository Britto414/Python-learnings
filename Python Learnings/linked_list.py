class node:
    def __init__(self,x):
        self.data=x
        self.next=None
        

class linklist:
    def __init__(self):
        self.head=None
        
    def insert_beg(self,data):
            temp=node(data)
            temp.next=self.head
            self.head=temp

    def insert_end(self,data):
        temp=node(data)
        if self.head is None:
            self.head=temp
        else:    
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=temp
            self.tail=itr.next
    
    def insert_after(self,data_to_insert,after_data):
        itr=self.head
        while itr:
            if itr.data==after_data:
                temp=node(data_to_insert)
                temp.next=itr.next
                itr.next=temp
                break
            itr=itr.next
    
    def remove_index(self,index):
        if index<0 or index >= self.length():
            raise ("invalid index")
            return
        if index==0:
            self.head=self.head.next
        count=0
        itr=self.head
        while itr:
            if index-1==count:
                itr.next=itr.next.next
            itr=itr.next
            count+=1

    def remove_value(self,value):
        itr=self.head
        flag=False
        while itr.next:
            if itr.next.data==value:
                flag=True
                itr.next=itr.next.next
                break
               
            itr=itr.next
        if flag:
            pass
        else:
            raise ValueError("Element doesn't exist")
        


    def insert_list(self,list:list()):
        
        for i in list:
            if self.head is None:
                self.head=node(i)
            else:
                self.insert_end(i)

    def insert_rec(self,value,index):
        if index == 0:
            Node = node(value)
            Node.next = self.head
            self.head = Node
            return
        
        


    def list_value(self,index):
        if index<0 or index>=self.length():
            raise("invalid")
            return
        itr=self.head
        count=0
        while count<index:
            count+=1
            itr=itr.next

        print(itr.data)


    def print_link(self):
        itr=self.head
        while itr:
            print(itr.data,"->",end='')
            itr=itr.next
        print()

    def isPalindrome(self, head) -> bool:
        itr=head
        prev=None
        while itr:
            tmp=itr.next
            itr.next=prev
            prev=itr
            itr=tmp
        return prev==head      
        

    def length(self):

        count = 0
        itr=self.head
        while itr:
            count += 1
            itr=itr.next

        return count
    
    def get_length(self):
        print("length:"+str(self.length()))

def reverseorder(head):
    prev = None
    while head: 
        tmp = head.next
        head.next = prev
        prev = head
        head=tmp   
        

    return prev
def print_link(head):
    # itr=self.head
    # while itr:
    #     print(itr.data,"->",end='')
    #     itr=itr.next
    # print()
    if head==None:
        print("End")
        return
    print(head.data,"->",end=" ")
    print_link(head.next)
# def recur_reverse(head):
#     if head.next==None:
#         return head
#     new=recur_reverse(head.next)
#     head.next.next=head
#     head.next=None
#     return new

def recur(head):
    if head.next==None:
        return head
    new=recur(head.next)
    head.next.next=head
    head.next=None
    return new




if __name__=="__main__":
    a=linklist()
 
    a.insert_list([1,2,1])
    print(a.isPalindrome(a.head))


    # a.head =recur(a.head)
    # b=a.head
    # while b.next:
    #     if b.next.data==1:
    #         b.next=None
    #         break
    #     b=b.next


    # a.print_link()


