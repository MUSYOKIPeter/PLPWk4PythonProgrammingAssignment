class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Greetings! I am {self.name}, {self.age} years old, and py{self.gender}.")

# Creating an instance of the Person class
person1 = Person("MUSYOKI Peter", 33, "male")

# Calling the introduce method to display the person's information
person1.introduce()
