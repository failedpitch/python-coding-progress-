class Node:
    def __init__(self, pNodeData):
        self.NodeData = pNodeData
        self.LeftNode = None
        self.RightNode = None

    def GetLeft(self):
        return self.LeftNode

    def GetRight(self):
        return self.RightNode

    def GetData(self):
        return self.NodeData

    def SetLeft(self, NewNode):
        self.LeftNode = NewNode

    def SetRight(self, NewNode):
        self.RightNode = NewNode


class Tree:
    def __init__(self, FirstNode):
        self.FirstNode = FirstNode

    def GetRootNode(self):
        return self.FirstNode

    def Insert(self, NewNode):
        CurrentNode = self.FirstNode
        while True:
            if NewNode.GetData() < CurrentNode.GetData():
                if CurrentNode.GetLeft() == None:
                    CurrentNode.SetLeft(NewNode)
                    return True
                else:
                    CurrentNode = CurrentNode.GetLeft()
            else:
                if CurrentNode.GetRight() == None:
                    CurrentNode.SetRight(NewNode)
                    return True
                else:
                    CurrentNode = CurrentNode.GetRight()


def OutputInOrder(RootNode):
    if RootNode.GetLeft() != None:
        OutputInOrder(RootNode.GetLeft())
    print(RootNode.GetData())
    if RootNode.GetRight() != None:
        OutputInOrder(RootNode.GetRight())


# Create nodes
FirstNode = Node(10)
SecondNode = Node(20)
ThirdNode = Node(5)
FourthNode = Node(15)
FifthNode = Node(7)


MyTree = Tree(FirstNode)
MyTree.Insert(SecondNode)
MyTree.Insert(ThirdNode)
MyTree.Insert(FourthNode)
MyTree.Insert(FifthNode)

OutputInOrder(MyTree.GetRootNode())

