# Python OOP

![Screenshot 2022-08-04 at 11 36 40](https://user-images.githubusercontent.com/102330725/182827196-3560be4f-dcc3-4eca-b768-255b9df7bc34.png)

## Step 1

```python
# Create an Animal Class
# syntax class Name:

class Animal:

    # __init__ to declare class attributes
    def __init__(self): # self refers current class
        self.alive = True
        self.spine = True

    def sleep(self):
        return "8 hours of sleep is adviced."

    def eat(self):
        return "eat if you like to stay alive.. and eat healthy"

# create an object of the class before using it
cat = Animal()
print(cat.eat()) #abstracted how was eat created or what info is available
```

## Step 2:

```python
# inherit everything from Animal class into reptile
from animal import Animal

# create a reptile class
class Reptile(Animal): # write the name of the class in (parent class) to inherit
    # parent class - base class - super class
    def __init__(self):
        # let it know to inherit everything from parent class
        super().__init__() # super is used to inherit everything from base class
        self.cold_blooded = True
        self.heart_chambers = [3,4]

    def seek_heat(self):
        return "looking for the sun shine"

    def hunt(self):
        return "working hard to catch a next meal"

#create object

reptile_object = Reptile()

print(reptile_object.eat())
print(reptile_object.hunt())
```

## Step 3:
```python
# inherit Reptile from Reptile class

from reptiles import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def _use_tounge_to_smell(self):
        try:
            return snake_object._use_tongue_to_smell()

        except AttributeError:
            return "this information is protected"

    # create 2 more functions one with _ the other with __
    # execute them both - return message should explain Encapsulation breakdown - public -protected - private

    def _snake_hunt(self):
        return "I'm good at hunting"

    def __venom(self):
        return "A lot of venom"


snake_object = Snake()

print(snake_object.eat()) # this function is inherited from Animal
print(snake_object.seek_heat()) #this function is inherited from Reptile class
print(snake_object._use_tounge_to_smell()) # public
print(snake_object._snake_hunt()) # protected
# print(snake_object.__venom()) # private
```