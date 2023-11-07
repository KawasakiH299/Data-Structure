# encoding :UTF-8

class Node:
    def __init__(self,element):
        self.element = element
        self.next = None

class SingLinkList:
    def __init__(self,node=None):
        self._OneNode = node


    #判断链表是否为空
    def enpty(self):
        return self._OneNode == None


    #设置一个游标用来循环链表
    def lengs(self):
        cur = self._OneNode
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    #遍历链表
    def travel(self):
        cur:Node = self._OneNode
        while cur != None:
            print(cur.element,end=' ')
            cur = cur.next
        print("")



    #尾部添加
    def append(self,item):
        node = Node(item)
        if self.enpty():
            self._OneNode = node
        else:
            cur = self._OneNode
            while cur.next != None:
                cur = cur.next  #cur.next是下一个node
            cur.next=node

    #头部添加
    def add(self,item):
        node = Node(item)
        node.next = self._OneNode
        self._OneNode = node

    #指定位置添加
    def  insert(self,pos:'插入的位置下标',item:'插入的node'):

        #如果要插入的位置下标为负，则表示是在头部插入
        if pos<0:
            self.add(item)
        # 如果要插入的位置下标为大于链表最大长度，则表示是在尾部插入
        elif pos > (self.lengs()-1):
            self.append(item)
        else:
            node = Node(item)
            pre:Node = self._OneNode
            count = 0
            while count < (pos-1):
                count +=1
                pre = pre.next
            node.next=pre.next
            pre.next = node

    #判断是否存在指定元素
    def search(self,item:'指定元素'):
        pre:Node = self._OneNode
        while pre != None:
            if pre.element == item:
                return '该元素存在！'
            else:
                pre = pre.next
        return "该元素不存在或链表为空!"

    #删除指定元素
    def dele(self,item):
        cur:Node = self._OneNode
        pre:Node = None
        while cur !=None:
            if cur.element == item:
                if cur == self._OneNode:
                    self._OneNode = cur.next
                else:
                    pre.next  =  cur.next
                break
            else:
                pre =cur
                cur = cur.next

if __name__ == '__main__':
    singlist = SingLinkList()
    singlist.append(1)
    singlist.append(2)
    singlist.append(3)
    singlist.append(4)
    #print(singlist.lengs())
    #singlist.travel()
    singlist.add(100)
    #singlist.travel()
    singlist.insert(-10,200)
    singlist.travel()
    print(singlist.search(100))
    singlist.dele(100)
    print(singlist.travel())