def answer(num_1,num_2):
    add=num_1+num_2
    multiplication=num_1*num_2
    divided=num_1/num_2
    return add, multiplication, divided
num_1=int(input('Enter first number:'))
num_2=int(input('Enter second number:'))
print("result:",answer(num_1,num_2))
