#1Code: If a string, must provided encoding and errors parameters, bytearray() converts the string to bytes using str.encode()
str = "Geeksforgeeks" 
# encoding the string with unicode 8 and 16
array1 = bytearray(str, 'utf-8')
array2 = bytearray(str, 'utf-16')
  
print(array1)
print(array2)

#3Code: If an Object, read-only buffer will be used to initialize the bytes array.
# Creates bytearray from byte literal
arr1 = bytearray(b"abcd")
  
# iterating the value
for value in arr1:
    print(value)
      
# Create a bytearray object
arr2 = bytearray(b"dianacernopitchi")
  
# count bytes from the buffer
print("Count of i is:", arr2.count(b"i"))

#4Code : If an Iterable(range 0<= x < 256), used as the initial contents of an array.


# simple list of integers
list = [1, 2, 3, 4]
  
# iterable as source
array = bytearray(list)
  
print(array)
print("Count of bytes:", len(array))