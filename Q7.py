class Animal:  
    def speak(self):  
        print("Animal Speaking")  
    #child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  

d = Dog()  
d.bark()  
d.speak()  

"""

~/Desktop/sem3_a/python ❯ python3 Q7.py                                15:26:51
dog barking
Animal Speaking

"""