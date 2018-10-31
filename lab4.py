class Animal(object) :
	def __init__(self,sound,name,age,favourite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favourite_color = favourite_color
	def eat(self,food):
		print("Yummy!!" + self.name + "is eating" + food)
	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self):
		print(self.sound *3)

Lion = Animal(" roar " , "king" , 28 , "black" )
Lion.make_sound()

cat = Animal(" meow " , "kk" , 12 , "brown" )
cat.make_sound()

class Person(object) :
	def __int__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender

G = Person(" geo " , 15 , " Jerusalem " , " male ")
