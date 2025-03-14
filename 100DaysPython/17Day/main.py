# PascalCase for classes
# camelCase
# snake_case name everything in Python
class User:

    # Constructor : Part of the blueprint which allows us to specify what should happen when our object is being constructed
    # Initialize : To set (variables, counters, switches) to their starting values at the beginning of program
    # In python it is special function which contains __init__ in syntax
    # def __init__(self):
    # initialise attributes
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # we don't need to put it into constructor
        self.following = 0
        print("New user being created....")

    # Method : Methods are function which are in class. Methods always getting 'self' parameter as the first parameter
    # Self parameter : It means when this method is called it knows the object callled it
    def follow(self,user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "Ranczo"

user_2 = User("002","Sherlock")
user_3 = User("003","Holmes")
print(user_2.username)
print(user_2.followers)

user_2.follow(user_3)
print(user_2.following)