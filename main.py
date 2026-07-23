users = []
count = int(input("How many students do you want to add?"))
for i in range(count):
    name = input("Enter student name: ")
    while True:
        try:
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Please enter a valid age.")

    user = {
            "name":name,
            "age":age
    }
    users.append(user)

print("\nStudents older than 18:")

for user in users:
    if user["age"] > 18:
        print(f"{user['name']}, {user['age']}")
        

