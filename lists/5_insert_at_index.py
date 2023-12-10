lst = [10,50,"mia","tez","domnick"]
print("list is => ",lst)
for x in lst:
    print("item: ",x,"index: ",lst.index(x))

# let's add element "tez" into index 1
lst.insert(1,"tez")
print("list now => ",lst)
for x in lst:
    print("item: ",x,"index: ",lst.index(x))