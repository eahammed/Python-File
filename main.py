from bank_operations.bank import credit,debit,transfer

print("hello world")
print("new  program")


class fruits:
    def _init_(self,name,color) -> none:
        self.name = name
        self.color =  color
    def say_color(self):
        print("my color is",self.color)
class appple(fruits):
    def my_type(self):
        print("i am an apple...")


    def say_color(self):
        print("i am red in color")
        
a = apple("apple","red")        

print(a.color)
