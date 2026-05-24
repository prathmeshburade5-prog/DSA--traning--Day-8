import sys
class BST:
    def __init__(self,key):
        self.leftchild=None
        self.rightchild=None
        self.data=key
        
    def insert(self,key):
        if self.data==None:
            self.data=key
            return
        elif self.data==key:
            return
        else:
            if key<self.data:
                if self.leftchild:
                    self.leftchild.insert(key)
                else:
                    self.leftchild=BST(key)
            elif key>self.data:
                if self.rightchild:
                    self.rightchild.insert(key)
                else:
                    self.rightchild=BST(key)  
    def search(self,key):
        if self.data==None:
            print("Tree is empty")
            return
        if self.data==key:
            print(key,"value is found")
           
        
        else:
            if key<self.data:
                if self.leftchild:
                    self.leftchild.search(key)
                    print("")
                else:
                    print(key,"not availble at left side")
            elif key>self.data:
                if self.rightchild:
                    self.rightchild.search(key)
                else:
                    print(key,"not availble at right side")                      
                            
        
    def preorder(self):
        print(self.data,end=" -> ")
        if self.leftchild:   #this check leftchild avail
            self.leftchild.preorder()
        if self.rightchild:
            self.leftchild.preorder()    
    def postorder(self):
        if self.leftchild:   #this check leftchild avail
            self.leftchild.postorder()
          
        if self.rightchild:
            self.leftchild.postorder() 
        print(self.data,end=" ->")     
        
    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        
        print(self.data,end=" ")
        
        if self.rightchild:
            self.rightchild.inorder()
                
            
    
    
if __name__== "__main__":
    
    obj=BST(None)
    while True:
        print("\n1 Insert")
        print("2 Preorder")    
        print("3 Postorder")    
        print("4 Inorder")
        print("5 Search")
        print("0 Exit") 
        
        n=int(input("Enter your choice"))
        if n==1:
            arr=[36,26,46,21,31,11,24,41,56,51,66]
            for i in range(len(arr)):
                obj.insert(arr[i])
        elif n==2:
            obj.preorder()
        elif n==3:
            obj.postorder()
        elif n==4:
            obj.inorder()
        elif n==5:
            obj.search()    
            
        elif n==0:
            sys.exit(0)
        else:
            print("Enter the valid number")                         
            
            
        