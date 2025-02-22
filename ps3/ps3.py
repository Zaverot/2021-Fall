class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: string
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Problem 1 #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind - left_size - 1)
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree

    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            self.size += 1
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            self.size += 1
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        return self

    
    ####### Problem 2 #######

    '''
    Deletes a key from the tree
    Returns the root of the tree or None if the tree has no nodes   
    '''
    def deleteHelper(self, key):
        self.size -= 1

        if self.key == key:
            if self.left is None and self.right is None and self.key == key:
                return None
            # nodes with single subtrees
            elif self.left is None:
                return self.right

            elif self.right is None:
                return self.left
            # nodes with two subtrees
            else: 
                temp = self.left.select(self.left.size - 1)
                temp.left = self.left.deleteHelper(temp.key)
                temp.right = self.right
                temp.size = self.size - 1
                return temp
        
        if key < self.key and self.left is not None:
            self.left = self.left.deleteHelper(key)    
        if key > self.key and self.right is not None:
            self.right = self.right.deleteHelper(key)

        return self

    def delete(self, key):
        # Your code goes here
        if self.search(key) is None:
            return self
        
        return self.deleteHelper(key)

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)

    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on

    Returns: the root of the tree/subtree

    Example:

    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10

    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        # store size information
        sizeRight = 0 if self.right is None else self.right.size
        sizeLeft = 0 if self.left is None else self.left.size

        if direction == 'L':
            if child_side == 'R':

                # store subtree size info
                sizeRightRight = self.right.right.size
                sizeRightRightLeft = self.right.right.left.size if self.right.right.left is not None else 0

                # rotate tree
                temp = self.right.right
                self.right.right = temp.left
                temp.left = self.right 
                self.right = temp

                # adjust sizes of subtrees
                self.right.size = sizeRight
                self.right.left.size = sizeRight - sizeRightRight + sizeRightRightLeft
            # if child_size == 'L'
            else:
                sizeLeftRight = size.left.right.size
                sizeLeftRightLeft = self.left.right.left.size if self.left.right.left is not None else 0

                # rotate tree
                temp = self.left 
                temp2 = self.left.right
                temp.right = temp2.left
                temp2.left = temp
                self.left = temp2 

                # adjust subtree sizes
                self.left.size = sizeLeft
                self.left.left.size = sizeLeft - sizeLeftRight + sizeLeftRightLeft

        # direction == 'R'          
        else:  
            if child_side == 'L':
                # store subtree size info
                sizeLeftLeft = self.left.left.size
                sizeLeftLeftRight = self.left.left.right.size if self.left.left.right is not None else 0

                # rotate tree
                temp = self.left.left
                self.left.left = temp.right
                temp.right = self.left 
                self.left = temp

                # adjust sizes of subtrees
                self.left.size = sizeLeft
                self.left.right.size = sizeLeft - sizeLeftLeft + sizeLeftLeftRight
            # if child_size == 'R'
            else:
                sizeRightLeft = self.right.left.size
                sizeRightLeftRight = self.right.left.right.size if self.right.left.right is not None else 0

                # rotate tree
                temp = self.right
                temp2 = self.right.left
                temp.left = temp2.right
                temp2.right = temp
                self.right = temp2 

                # adjust subtree sizes
                self.right.size = sizeRight
                self.right.right.size = sizeRight - sizeRightLeft + sizeRightLeftRight


        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self

