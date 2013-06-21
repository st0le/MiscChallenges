import random
class LinkedList:
    
    def __init__(self):
        self.head = self.tail = None
        
    def add(self, item ):
        new_node = [item,None]
        if self.tail == None:
            self.head = self.tail = new_node
        else:
            self.tail[1] = new_node
            self.tail = new_node
            
    def __str__(self):
        return str(self.head)

    def middle(self):
        slow = fast = self.head
        if fast: fast = fast[1]
        while fast:
            slow = slow[1]
            fast = fast[1]
            if fast:
                fast = fast[1]
            
        return slow[0]
    

LL = LinkedList()
lst = []
for i in xrange(11):
    r = random.randint(10,99)
    LL.add(r)
    lst.append(r)
print LL
print "Middle Element : ",LL.middle()
print "Verify : ",lst[len(lst)/2]