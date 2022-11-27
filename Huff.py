class Node:
    def _init_(self,symbol, frequency,left = None, right = None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right
        self.huff = '' 
        


def print_nodes(root, val = ""):
    val = val + str(root.huff)
    if root.left:
        print_nodes(root.left,val)
    if root.right:
        print_nodes(root.right,val)
    if not root.left and not root.right:
        print(root.symbol, "----", val)

string = input()
dict = {}

for i in string:
    if i in dict:
        dict[i] += 1 
    else:
        dict[i] = 1 
        
nodes = [Node(i,dict[i]) for i in dict]
print(dict.keys())
print(dict.values())

while(len(nodes) > 1):
    nodes = sorted(nodes,key = lambda x : x.frequency)

    
    left = nodes[0]
    right = nodes[1]
    
    left.huff = 0 
    right.huff = 1 
    
    newNode = Node(left.symbol + right.symbol,left.frequency + right.frequency,left,right)
    
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
    
print_nodes(nodes[0])