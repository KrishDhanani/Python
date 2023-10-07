# As java Getter and Setter are same here.
# setter take value and update it; then getter return that value.
# for getter we use "@property" <-- Decorator (Inside it all fun is writen alrady to how it return the value).
# for setter we use "@getter_method_name.setter"
# Remember that for use setter you need to define getter.




class Car:
    def __init__(self, tyers):
        self.wheel = tyers

    @property                                                     # getter
    def new_wheel1(self):
        return self.wheel 
    
    @new_wheel1.setter                                             #setter
    def new_wheel1(self, new_wheel):
        # Subtract 2 from the provided value and set it as the new wheel count
        self.wheel = new_wheel - 2

    def show(self):
        print(f"Wheel value is {self.wheel}")

c = Car(4)
c.new_wheel1 = 6  # This will set the number of wheels to 4 (6 - 2)  # remember we use here property name
print(c.wheel)
c.show()








# e.g.:
class Car:
    def __init__(self, value):
        self.cc = value

    @property
    def ccc(self):
        return self.cc
    
    @ccc.setter
    def ccc(self, new_cc):
        self.cc = new_cc  
    
    def show(self):
        print(f"My car cc is {self.cc}")

c = Car(100)
c.ccc = 200  # Use the property name, not new_cc
c.show()
