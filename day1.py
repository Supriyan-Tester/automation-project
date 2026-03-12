name='john'
age= 25
print(name)
print(age)
print(f"My name is {name} and I am {age} years old.")

if age >= 20:
    print("You are an senior learner.")
else:
    print("You are a junior learner.")


for i in range(3):
    print(name)

def greet():
    print(f"Hello, {name}!")

greet()


def login_accept_info(username,password):
    print(f"Username: {username}")
    print(f"Password: {password}")

login_accept_info("standard_user01","secret_sauce01")