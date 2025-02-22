#################
#               #
# Problem Set 0 #
#               #
#################



#
# Setup
#

class BinaryTree:
    # left : BinaryTree
    # right : BinaryTree
    # key : string
    # temp : int
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.temp = None



#
# Problem 1
#

# Sets the temp of each node in the tree T
# ... to the size of that subtree
def calculate_size(T):
    # Base Case
    if T == None:
        return 0

    # Recursive Case
    T.temp = 1 + calculate_size(T.left) + calculate_size(T.right)
    return T.temp


#
# Problem 3
#

# Outputs a subtree subT of T of size in the interval [L,U] 
# ... and removes subT from T by replacing the pointer 
# ... to subT in its parent with `None`
def FindSubtree(T, L, U): 
    
    def FindSubtree2(T, L, U):
        if T.right and L <= T.right.temp <= U:
            subT = T.right
            T.right = None
            return subT
        if T.left and L <= T.left.temp <= U:
            subT = T.left
            T.left = None
            return subT
        if T.right:
            return FindSubtree2(T.right, L, U)
        else:
            return FindSubtree2(T.left, L, U)

    if calculate_size(T) > U and U >= 2*L:
        return FindSubtree2(T, L, U)
    else:
        return None
    
    


