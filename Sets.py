#sets are collection data type that is unordered and mutable. no duplicates 

myset = {1,2,3,1,2} 
print(myset)

# We can use a set function 
myset = set([1,2,3,]) 
print(myset) 

#lets create 3 diferents sets 

odds = {1,3,5,7,9}
evens= {0,2,4,6,8}
primes={2,3,5,7}

u = odds.union(evens)
print(u)

#interseccion of 2 sets 

i = odds.intersection(primes)
print(i) 

