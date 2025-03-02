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

    def __str__(self):
        result = ''
        for i in range(self.n):
            if ctypes.cast(id(self.A[i]), ctypes.POINTER(ctypes.c_void_p)).contents.value != 0:  
                result = result + str(self.A[i]) + ','
        return "[" + result[:-1] + "]"

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

    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            return "error - List index out of range"

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
        if self.n == 0:
            return "error - pop from empty list"

        print(f"Pop element is {self.A[self.n-1]}")
        self.n = self.n - 1


    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
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
        if self.n == 0:
            return "error - List is empty"

        total = 0
        for i in range(self.n):
            if not isinstance(self.A[i], str):  # Check if A[0] is not a string
                if isinstance(self.A[i], (int, float)):  # Check if element is numeric
                    total += self.A[i]
                  
        return total

    def sort(self):
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
        for i in range(self.n // 2):  
            self.A[i], self.A[self.n - i - 1] = self.A[self.n - i - 1], self.A[i]

        return self.A
                          