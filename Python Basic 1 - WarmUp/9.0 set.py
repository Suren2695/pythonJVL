'''A set is a collection of unique items in Python.
Characteristics of Sets
✅ Unordered
 ✅ No duplicate values allowed
 ✅ Mutable (you can add/remove items)
 ✅ Uses {} brackets'' '''

#set of integer
my_set = {1,2,3}

print(my_set)

#set of mixed datatypes
my_mix = {1.0, "Hello", (1,2,3)}
print(my_mix)

#add 4 in the set 
my_set.add(4)
print(my_set) #{1, 2, 3, 4}

#if you try to duplicate it wont allow
my_set.add(2)
print(my_set) #{1, 2, 3, 4}

#Update
my_set.update([9,4,5,2])
print(my_set) #{1, 2, 3, 4, 5, 9}

#remove
my_set.remove(9)
print(my_set) #{1, 2, 3, 4, 5}

#Union
A={1,2,3,7,8}
B={4,5,6,2,3}
print(A|B) #{1, 2, 3, 4, 5, 6,7,8} - #pipe symbol |
print(B|A) #same

#Intersection
print(A&B) #{2, 3}

# A-B set difference
print(A-B) #{8, 1, 7}

#Symentric difference
#It acts as opposite to the intersection - It gives a uncommon valude from both the sets
print(A^B) #{1, 4, 5, 6, 7, 8}
