def name(first_name,last_name):
    full=first_name+last_name
    return full.title()
first_name=input('Enter first name：')
last_name=input('Entert last name:')
print('Full name is:'+name(first_name,last_name))
