import random
import time

class MinHeap():
    def __init__(self, arr, min = True):
        self.array = []  # initialize the heap array
        self.pos = {}  # initialize the locator dictionary
        self.size = len(arr)  # initialize the size of the heap
        self.type = min  # save the type of the heap (for display reasons only)

        for i, item in enumerate(arr):
            self.array.append((item[0], item[1]))  # save the item into the heap
            self.pos[item[0]] = i  # store the location into the locator
        
        for i in range(self.size // 2, -1, -1):
            self.heapify(i)  # maintain the heap properties


    def display(self):
        """display() -> void\n
        This method displays the heap.\n"""
        if self.type == True:  # if it is a minHeap
            print("Minheap: ", end = ' ')
            for i in range(self.size):
                print("{} : {:.2f}".format(self.array[i][0], self.array[i][1]), end = ' ')
            print()
        else:  # if it is a maxHeap
            print("Maxheap: ", end = ' ')
            for i in range(self.size):
                print("{} : {:.2f}".format(self.array[i][0], -self.array[i][1]), end = ' ')
            print()

    def isEmpty(self):
        """isEmpty() -> bool\n
        This method returns True if the heap is empty, else it returns False.\n"""
        return self.size == 0  # True if empty, else false
    

    def heapify(self, i):
        """heapify(i) -> void\n
        This method restructures the keys, from node i, so the tree with root the node i is a minHeap.\n"""
        smallest = i  # set the starting node as the smallest
        l = 2*i + 1  # store the index of left child
        r = 2*i + 2  # store the index of right child

        if l < self.size and self.array[l][1] < self.array[smallest][1]:  # if left isn't the terminal node and it's smaller than the current smallest
            smallest = l  # set left child as smallest
        if r < self.size and self.array[r][1] < self.array[smallest][1]:
            smallest = r  # set right child as the smallest
        
        if smallest != i:  # if smallest isn't the current node
            self.pos[self.array[smallest][0]] = i  # change locations in the locator
            self.pos[self.array[i][0]] = smallest

            self.array[smallest], self.array[i] = self.array[i], self.array[smallest]  #swap elements
        
            self.heapify(smallest)  # heapify again

    
    def getMin(self):
        """getMin() -> tuple\n
        This method returns the root element of the heap.\n"""
        if self.size == 0:  # if empty
            return None
        return self.array[0]  # return the top element's key
    

    def extractMin(self):
        """extractMin() -> tuple\n
        This method pops the root of the heap and recreates the heap.\n"""
        if self.size == 0:  # if empty
            return None
        
        root = self.array[0]  # set root as the top element
        lastNode = self.array[self.size - 1]  # set last node as last

        self.array[0] = lastNode  # put last node at top

        self.pos[lastNode[0]] = 0  # change last node loc in the locator
        del self.pos[root[0]]  # delete root from the locator

        self.size -= 1  # decrease the size of heap
        self.heapify(0)  # sort the heap from the start

        return root
    
    
    def insert(self, item):
        """insert(item) -> void\n
        This method adds a new node to the heap in the proper position.\n"""
        if self.size < len(self.array):  # if the array has empty positions
            self.array[self.size] = (item[0], 10**10)  # insert the item's key in the last position
        else:
            self.array.append((item[0], 10**10))  # append the item's key in the end
            
        self.pos[item[0]] = self.size  # save the key in the locator
        self.size += 1  # increase the size of the heap
        self.decreaseKey(item)  # call the decreaseKey method to put the key in the right position
    
    
    def decreaseKey(self, item):
        """decreaseKey(item) -> void\n
        This method checks if the item is in a higher position than it should and repositions it.\n"""
        i = self.pos[item[0]]  # get the item's position
        val = item[1]  # get the item's value

        if self.array[i][1] <= val:  # if the existing element in the position has lower or equal value
            return  # exit
        
        self.array[i] = item  # replace the element
        p = (i-1)//2  # go to the parent node
        while i > 0 and self.array[i][1] < self.array[p][1]:  # while the element's value is smaller than the parent's
            self.pos[self.array[i][0]] = p  # change the index in the locator
            self.pos[self.array[p][0]] = i  # change the index in the locator
            self.array[p], self.array[i] = self.array[i], self.array[p]  # swap the elements

            i = p  # change the i to show the element
            p = (i-1) // 2  # get the new parent node
    
    def increaseKey(self, item):
        """increaseKey(item) -> void\n
        This method checks if the item is in a lower position than it should and repositions it.\n"""
        i = self.pos[item[0]]  # get the item's position
        val = item[1]  # get the item's value

        if self.array[i][1] >= val:  # if the stored value in the position is greater or equal than the item's
            return   # exit
        
        self.array[i] = item  # replace the element
        self.heapify(i)  # heapify the array
    
    
    def isInHeap(self, k):
        """isInHeap(k) -> bool\n
        This method returns True if the key exists in the heap, else returns False.\n"""
        if k in self.pos:
            return True
        return False
    

    def deleteKey(self, item):
        """deleteKey(item) -> void\n
        Delete the item from the heap.\n"""
        self.decreaseKey((item[0], - 1e100))
        self.extractMin()


def locGenerator():
    """locGenerator() -> tuple\n
    This method creates a location with longtitude and latitude equal to a
    pseudo-random int between 0,1000 and a temp between -50.00 and 50.00.\n"""
    x = random.randint(0,1000)  # create the longtitude of the location
    y = random.randint(0,1000)  # create the latitude of the location
    temp = round(random.uniform(-50.00,50.00), 2)  # create the random temperature of the location
    return ((x,y), temp)


def newLoc(item, minh, maxh, curMed):
    """newLoc(item, minh, maxh, curMed) -> float\n
    This method adds the a new item into the proper heap and returns the median after the insertion.\n"""
    if not minh.isInHeap(item[0]) and not maxh.isInHeap(item[0]):  # if the location hasn't occured before
        if item[1] <= curMed:  # if is smaller than the median
            maxh.insert((item[0],-item[1]))  # insert in the maxHeap
        elif item[1] > curMed:  # if is greater than the median
            minh.insert((item[0],item[1]))  # insert in the minHeap
    else:  # if the location already existed
        if minh.isInHeap(item[0]) and item[1] > curMed:  # if it is in minHeap and must remain there
            i = minh.pos[item[0]]  # get the index
            minh.array[i] = item  # change the value
        elif maxh.isInHeap(item[0]) and item[1] < curMed:  # if it is in maxHeap and must remain there
            i = maxh.pos[item[0]]  # get the index
            maxh.array[i] = item  # change the value
        elif minh.isInHeap(item[0]) and item[1] < curMed:  # if it is in minHeap and must go to the maxHeap
            maxh.insert((item[0], -item[1]))  # put in maxHeap
            minh.deleteKey(item)  # delete from minHeap
        elif maxh.isInHeap(item[0]) and item[1] > curMed:  # if it is in maxHeap and must go to the minHeap
            minh.insert((item[0], item[1]))  # put in minHeap
            maxh.deleteKey(item)  # delete from maxHeap
    balanceHeaps(minh, maxh)  # balance heaps
    curMed = calcMedian(minh, maxh)  # calculate the median
    return curMed  # return the new median


def balanceHeaps(minh, maxh):
    """balanceHeaps(minh, maxh) -> void\n
    This method restructures the heaps in a way they have similar sizes (difference up to 1 element).\n"""
    if abs(minh.size - maxh.size) <= 1:  # if the sizes are similar
        return  # exit
    if maxh.size > minh.size:  # if maxHeap is longer than minHeap
        item = maxh.extractMin()  # get the root
        minh.insert((item[0], -item[1]))  # insert it in minHeap
    else:  
        item = minh.extractMin()  # get the root
        maxh.insert((item[0], -item[1]))  # insert it in maxHeap


def calcMedian(minh, maxh):
    """calcMedian(minh, maxh) -> float\n
    This method calculates the median value of the two heaps.\n"""
    if minh.size == maxh.size:
        med = (minh.getMin()[1] + (-maxh.getMin()[1]))/2
    elif minh.size > maxh.size:
        med = minh.getMin()[1]
    elif maxh.getMin() != None:
        med = -maxh.getMin()[1]
    return med


def arrayChanger(arr, minh, maxh, curMed):
    """arrayChanger(arr, minh, maxh, curMed) -> void\n
    This method is responsible to change the first 100 values of the locations.\n"""
    for item in arr:
        item = (item[0], round(random.uniform(-50.00, 50.00),2))  # change the value of the element
        print("Current Median Temperature: {:.2f}".format(newLoc(item, minh, maxh, curMed)))  # put in heap and print median
        if minh.size == maxh.size:  # if the heaps are equal
            print("{}: {}".format(minh.getMin()[0], minh.getMin()[1]))  # print minHeap's root
            print("{}: {}".format(maxh.getMin()[0], -maxh.getMin()[1]))  # print maxHeap's root
        elif minh.size > maxh.size:  # if minHeap is bigger
            print("{}: {}".format(minh.getMin()[0], minh.getMin()[1]))  # print minHeap's root
        else:
            print("{}: {}".format(maxh.getMin()[0], -maxh.getMin()[1]))  # print maxHeap's root

    
if __name__ == "__main__":
    curMed = 0
    minh = MinHeap([])
    maxh = MinHeap([],False)
    arr = []

    for _ in range(100):
        item = locGenerator()
        arr.append(item)
        curMed = newLoc(item, minh, maxh, curMed)

    for _ in range(499900):
        curMed = newLoc(locGenerator(), minh, maxh, curMed)

    t1 = time.perf_counter()
    arrayChanger(arr, minh, maxh, curMed)
    t1 = time.perf_counter() - t1
    print("{} s".format(t1))
