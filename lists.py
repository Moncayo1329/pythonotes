#list: ordere mutable , allows duplicate elements 
mylist = ["banana", "cherry" , "applee"]
print(mylist)

#hoew many elements you hace inside your list 
len(mylist) 

print(len(mylist)) 

#this is for add a element  (append)

mylist.append("lemon") 
print(mylist)

# if we want to insert an item at a specific position from 0,1,2,3,4

mylist.insert(1,"blueberry") 
print(mylist)

# pop method, return the last item and also removes it  

item = mylist.pop()
print(item) 
print(mylist)


#new list 
mylist.sort()

new_list = sorted(mylist)
print(mylist) 
print(new_list)