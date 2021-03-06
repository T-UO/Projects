# the _repr_ method is one of several ways to provide nicer string representation

class User:

	active_users = 0 # to define a class attribute, don't user "self"

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first, last, age = data_str.split(",")
		return cls(first, last, age)

	

	def __init__(self, first, last , age):
		self.first = first # attribute
		self.last = last # attribute
		self.age = age # attribute
		User.active_users += 1


	def __repr__(self):
	return f"{self.first} is {self.age}"	

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self): # becomes a mehtod because we are adding it to an object
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

	def say_hi(self):
		print("Hello!!!")


#	user1 = User("Joe", "Smith", 68)
#	user2 = User("Blanca", "Lopez", 41)
#	print(User.display_active_users)
#	user1 = User("Joe", "Smith", 68)
#	user2 = User("Blanca", "Lopez", 41)
#	print(User.display_active_users)

tom = User.from_string("Tom, Jones, 89")
print(tom.first)
print(tom.full_name())
#	User("Sue, Prichet, 12")



