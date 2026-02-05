users = []

for i in range(3):
    name = input("Enter student name: ")
    age = int(input("Enter age: "))

    user = {
        "name": name,
        "age": age
    }

    users.append(user)

print("\nStudents older than 18:")

for user in users:
    if user["age"] > 18:
        print(f'{user["name"]}, {user["age"]}')
