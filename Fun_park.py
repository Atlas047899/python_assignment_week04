children = [ 
{"name": "Alice", "age": 2, "height": 95}, 
{"name": "Bob", "age": 4, "height": 105}, 
{"name": "Charlie", "age": 3, "height": 110}, 
{"name": "David", "age": 5, "height": 102}, 
{"name": "Eve", "age": 6, "height": 99} 
]

'''def criteria(x):
    if x["age"] > 3 and x["height"] > 100:
        return True
    else:
        return False

eligible_children = list(filter(criteria , children))

print(eligible_children)
'''

eligible_children = [x for x in children if x["age"] > 3 and x["height"] > 100]
print(eligible_children)