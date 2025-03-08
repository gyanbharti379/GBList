import ctypes
class GBList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()

    def __len__(self):
        return self.n
    
    def count(self):
        return self.n
    
    def index(self):
        """Return a dictionary with item values as keys and their indices as values."""
        index_map = {}
        for i in range(self.n):  
            if self.A[i] not in index_map:  # Avoid duplicates
                index_map[self.A[i]] = i
        return index_map
         
    def __str__(self):
        """User-friendly output."""
        result = ''
        for i in range(self.n):
            if ctypes.cast(id(self.A[i]), ctypes.POINTER(ctypes.c_void_p)).contents.value != 0:  
                result = result + str(self.A[i]) + ','
        return "[" + result[:-1] + "]"
    
    def __repr__(self):
        """Developer-friendly output (debugging)."""
        return f"GBList({[self.A[i] for i in range(self.n)]})"

    def append(self,item):
        if self.find(item) != "error - ValueError! item not in a list":
            return "error - ValueError! item already in a list"
        else:  
            if self.n == self.size: #if list is full
                self.__resize(self.size*2)
                self.A[self.n] = item
                self.n = self.n + 1
            else:
                self.A[self.n] = item
                self.n = self.n + 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __getitem__(self, index):
        """Support both indexing and slicing"""
        if isinstance(index, slice):
            start = index.start if index.start is not None else 0
            stop = index.stop if index.stop is not None else self.n
            step = index.step if index.step is not None else 1

            # Adjust negative indices
            if start < 0:
                start += self.n
            if stop < 0:
                stop += self.n

            # Handle out-of-bounds slicing
            start = max(0, min(self.n, start))
            stop = max(0, min(self.n, stop))

            new_list = GBList()
            for i in range(start, stop, step):
                new_list.append(self.A[i])
            return new_list

        elif isinstance(index, int):
            # Handle negative indexing
            if index < 0:
                index += self.n
            if 0 <= index < self.n:
                return self.A[index]
            else:
                raise IndexError("Index out of range")

        else:
            raise TypeError("Index must be an integer or a slice")


    def __setitem__(self, index, item):
            if 0 <= index < self.n: 
                self.insert(index,item)  
            elif index == self.n:  
                self.append(item)
            else:  
                raise IndexError("list assignment index out of range")


    def insert(self, pos, item): #first check item present in the list or not
        if self.find(item) != "error - ValueError! item not in a list":
            return "error - ValueError! item already in a list"
        else:  
            if self.n == self.size:  # if list is full
                self.__resize(self.size * 2)

            for i in range(self.n, pos, -1):
                if i > pos:
                    self.A[i] = self.A[i - 1]

                # Insert item and update size outside the loop
                self.A[pos] = item  
                self.n = self.n + 1

    def __delitem__(self, pos):  
        if 0 <= pos < self.n:  
            for i in range(pos, self.n - 1):
                self.A[i] = self.A[i + 1]
            self.n = self.n - 1
        else:
            raise IndexError("list assignment index out of range")   

    def pop(self):
        """Remove and return item at index (default last) from the GBList."""
        if self.n == 0:
            return "error - pop from empty list"

        print(f"Pop element is {self.A[self.n-1]}")
        self.n = self.n - 1


    def clear(self):
        """Clear GBList."""
        self.n = 0
        self.size = 1

    def find(self,item):
        """Return a index of value in the list of GBList."""
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "error - ValueError! item not in a list"

    def remove(self,item):
        if self.find(item) != "error - ValueError! item not in a list":
            n = self.find(item) 
            self.__delitem__(n)
        else:
            return "error - ValueError! item not in a list"
        
    def max_item(self):
            """Return a max number from all integer in the list of GBList."""
            if self.n == 0:
                return "error - List is empty"  

            if not isinstance(self.A[0], str):  # Check if A[0] is not a string
                max_val = self.A[0]  
                for i in range(1, self.n):
                     if not isinstance(self.A[i], str): 
                        if self.A[i] is not None and self.A[i] > max_val: 
                            max_val = self.A[i]

                return max_val

    def min_item(self):
        """Return a min number from all integer in the list of GBList."""
        if self.n == 0:
            return "error - List is empty"  

        if not isinstance(self.A[0], str):  # Check if A[0] is not a string
            min_val = self.A[0]  
            for i in range(1, self.n):
                if not isinstance(self.A[i], str): 
                    if self.A[i] is not None and self.A[i] < min_val: 
                        min_val = self.A[i]

            return min_val 

    def average(self):
        """Return a average of all integer and float items in the list of GBList."""
        if self.n == 0:
            return "error - List is empty"

        total = 0
        count = 0
        for i in range(self.n):
            if not isinstance(self.A[i], str):  # Check if A[0] is not a string
                if isinstance(self.A[i], (int, float)):  # Check if element is numeric
                    total += self.A[i]
                    count += 1

                if count == 0:
                        return "error - No numeric values to calculate the average"

        return total / count        

    def sum(self):
        """Return a sum of all integer and float items in the list of GBList."""
        if self.n == 0:
            return "error - List is empty"

        total = 0
        for i in range(self.n):
            if not isinstance(self.A[i], str):  # Check if A[0] is not a string
                if isinstance(self.A[i], (int, float)):  # Check if element is numeric
                    total += self.A[i]
                  
        return total

    def sort(self):
        """Return a sorted arrary of GBList."""
        B = []
        
        for i in range(0, self.n):  # Change loop range to 0 to self.n - 2
           if not isinstance(self.A[i], (str, float)): 
              B.append(self.A[i])
              
           else:
                continue 
        for i in range(1, len(B)):  
            for j in range(i, 0, -1):  
                if B[j - 1] > B[j]:
                    B[j - 1], B[j] = B[j], B[j - 1]  
                else:
                    break  

        return B
    
    def reverse(self):
        """Return a reverse of GBList."""
        self.A = self.A[::-1]
        return self.A
    
    def copy(self):
        """Return a shallow copy of GBList, excluding nested lists."""
        new_list = GBList()  # Create new instance
        for i in range(self.n):  
            if not isinstance(self.A[i], GBList):  # Only copy non-list items
                new_list.append(self.A[i])
        return new_list
    
    def deepcopy(self):
        """Return a deep copy of GBList."""
        new_list = GBList()  # Create new instance
        for i in range(self.n):  # Copy elements
            new_list.append(self.A[i])
        return new_list
    
    def extend(self, other_list):
        """Extend the GBList with the items from another GBList."""
        for i in range(other_list.n):  
            self.append(other_list.A[i])    
        return self 
    

                          
