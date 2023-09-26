#map() = applies a fun to each item in an iterable (list, tuple, etc)
#map(fun, iterable)

store = [("shirt",20.00), 
         ("pants",25.00), 
         ("jacket",50.00), 
         ("socks",10.00)]

to_euros = lambda data: (data[0], data[1]*0.82)

store_euros = map(to_euros, store)

for i in store_euros: print(i)