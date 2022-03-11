users_number = input("Enter the number:")
users_number = int(users_number)
  
data = []

for x in range (users_number):

    list_name = input ("Enter your name: ")
    list_age = input ("Enter your age: ")
    dict = {
            
            'name': list_name,
            'age' : list_age,
 }
    data.append(dict)

search_name = input ("Enter the name to search : ") 

for user in data:
    if user['name'] == search_name:
        print ("age :" + user['age'])
        break
    elif list_name != search_name:
        print("This name doesn't exist!")
        break