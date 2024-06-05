def Ladd(a, b):
    result = []
    for elem1 in a:
        result.append(elem1)
        print(result)
    for elem2 in b:
        result.append(elem2)
        print(result)
    return result

a = [0,1,2,3,4,5,6,7]
b = [0,1,2,3,4,5,6,7]
output = Ladd(a, b)
print(output)
