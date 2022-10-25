class treenode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def print_tree(self):
        print(self.data)
        if self.children:
            for i in self.children:
                print("   |_",i.data)
                if i.children:
                    for j in i.children:
                        print("      |_",j.data)
                    print("   ------------")
                

def buildtree():
    root=treenode("electronics")
    
    laptop=treenode("laptop")
    laptop.add_child(treenode("mac"))
    laptop.add_child(treenode("lenova"))

    tv=treenode("Tv")
    tv.add_child(treenode("samsung"))
    tv.add_child(treenode("sony"))

    root.add_child(laptop)
    root.add_child(tv)
    return root
    
if __name__=="__main__":

    root=buildtree()
    root.print_tree()



		

