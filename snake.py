# inherit Reptile from Reptile class

from reptiles import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tounge_to_smell(self):
        return "I can use my tongue to smell food"

    # create 2 more functions one with _ the other with __
    # execute them both - return message should explain Encapsulation breakdown - public -protected - private

    def _snake_hunt(self):
        return "I'm good at hunting"

    def __venom(self):
        return "A lot of venom"


snake_object = Snake()

print(snake_object.eat()) # this function is inherited from Animal
print(snake_object.seek_heat()) #this function is inherited from Reptile class
print(snake_object.use_tounge_to_smell()) # public
print(snake_object._snake_hunt()) # protected
# print(snake_object.__venom()) # private

# what type of errors and exceptions have you seen so far
# syntax error
# indentation Error - value errors - attribute error

# Try :
      # print()
      # return

# except name_of_error:
      # print()
      # return

 # finally:
      #print("Better luck next time")



