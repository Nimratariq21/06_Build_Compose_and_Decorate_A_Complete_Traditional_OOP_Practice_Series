# project06
# 1.using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

student1 =Student("aliza",40)
student1.display()


# 2.using cls
class counter:
    count =0
    def __init__(self):
        counter.count +=1
    @classmethod
    def display_counter(cls):
        print(f"my total created object count are{cls.count}")
object1=counter()
object2=counter()
object3=counter()
object4=counter()
counter.display_counter()


# 3.public variable and method
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting...")

# Usage
my_car = Car("Toyota")
print(my_car.brand)
my_car.start()


# 4. Class Variables and Class Methods
class Bank:
    bank_name = "UBL"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):  # ✅ Now it's properly indented at the class level
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")
# Usage
account1 = Bank("aliza")
account2 = Bank("nimra")

account1.display()
account2.display()

Bank.change_bank_name("azaan bank")

account1.display()
account2.display()


# 5 static variable and static method
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Usage
result = MathUtils.add(10, 5)
print("Sum of my two number are:", result)


# 6. Constructors and Destructors
class Logger:
  def __init__(self,message): # constructor
    self.message = message
    print(f"Object created with message: {self.message}")
  def __del__(self): # destructor
    print(f"Object destroyed with message: {self.message}")
logger1 = Logger("aliza is logged in")
del logger1


# 7. Access Modifiers: Public, Private, and Protected
class Employee:
  def __init__(self,name,_salary,__ssn):
    self.name = name
    self._salary = _salary
    self.__ssn = __ssn
  def get_salary(self):
    return self._salary
  def get_ssn(self):
    return self.__ssn
emp1 = Employee('Alice',100000,'123456789')
print(emp1.get_salary())
print(emp1.get_ssn())
print(emp1.name) # name is public so it is accessible
print(emp1._salary) # salary is protected so it shouldn't
# print(emp1.__ssn) # ssn is private it raise an error and can't be accessible


# 8. The super() Function
class Person:
  def __init__(self,name):
    self.name = name
class Teacher(Person):
  def __init__(self,name,subject):
    super().__init__(name)
    self.subject = subject
teacher1 = Teacher("aliza","Math")
print(teacher1.name)
print(teacher1.subject)


# 9. Abstract Classes and Methods
from abc import abstractmethod
class Shape:
  @abstractmethod
  def area(abc):
    pass
class Rectangle(Shape):
  def __init__(self,length,width):
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width
rectangle1 = Rectangle(30,20)
print(rectangle1.area())


# 10. Instance Methods
class Dog:
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed
  def bark(self):
    print(f"{self.name} the {self.breed} dog is barking")
dog1 = Dog("Buddy","Labrador")
dog1.bark()


# 11. Class Methods
class Book:
  total_books = 0
  def __init__(self,title):
    self.title = title
  @classmethod
  def increment_book_count(cls):
    cls.total_books += 1
book1 = Book("Pride and Prejudice")
Book.increment_book_count()
print(f"{book1.title} is book {book1.total_books}")

book2 = Book("Harry Potter and the Philosopher's Stone")
Book.increment_book_count()
print(f"{book2.title} is book {book2.total_books}")


# 12. Static Methods
class TemperatureConverter:
    def __init__(self, celsius_temp):
        self.celsius_temp = celsius_temp

    @staticmethod
    def celsius_to_fahrenheit(celsius_temp):
        fahrenheit_temp = (celsius_temp * 9/5) + 32
        return fahrenheit_temp
temp1 = TemperatureConverter(30)
print(f"{temp1.celsius_temp}C to {temp1.celsius_to_fahrenheit(30)}F")


# 13. Composition
class Engine:
  def __init__(self,engine_type):
    self.engine_type = engine_type
  def start(self):
    print(f"The {self.engine_type} engine is starting")
class Car:
  def __init__(self,engine):
    self.engine = engine
  def start_engine(self):
    self.engine.start()
engine1 = Engine("V8")
car1 = Car(engine1)
car1.start_engine()


# 14. Aggregation
class Department:
  def __init__(self,name):
    self.name = name
class Employee:
  def __init__(self,name,department):
    self.name = name
    self.department = department
dep1 = Department("IT")
emp1 = Employee("aliza",dep1)
print(emp1.name)
print(emp1.department.name)


# 15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
  def show(self):
    print("Method from class A")
class B(A):
  def show(self):
    print("Method from class B")
class C(A):
  def show(self):
    print("Method from class C")
class D(B,C):
  pass
d1 = D()
d1.show()


# 16. Function Decorators
def log_function_call(func):
  def wrapper(*args,**kwargs):
    print("Function is being called")
    return func(*args,**kwargs)
  return wrapper
@log_function_call
def say_hello(): # decoractor function call that first call wrapper function then say_hello
  print("Hello")
say_hello()


# 17. Class Decorators
class add_greeting:
  def __init__(self,cls):
    self.cls = cls
  def __call__(self,*args,**kwargs):
    obj = self.cls(*args,**kwargs)
    obj.greet = self.greet
    return obj
  def greet(cls):
    return "Hello from Decorator!"
@add_greeting
class Person:
  def __init__(self,name):
    self.name = name
person1 = Person("Muniba")
print(person1.name)
print(person1.greet())


# 18. Property Decorators: @property, @setter, and @deleter
class Product:
  def __init__(self,price):
    self._price = price
  @property
  def price(self):
    return self._price
  @price.setter
  def price(self,price):
    self._price = price
  @price.deleter
  def price(self):
    del self._price
product1 = Product(100)
print(product1.price)


# 19. callable() and __call__()
class Multiplier:
  def __init__(self,factor):
    self.factor = factor
  def __call__(self,x):
    return x * self.factor
multiplier1 = Multiplier(2)
print(multiplier1(5))
print(callable(multiplier1))
     

# 20. Creating a Custom Exception
# Step 1: Create a custom exception
class InvalidAgeError(Exception):
    """Exception raised for errors in the input age below 18."""
    def __init__(self, age, message="Age must be at least 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Step 2: Create a function that checks the age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Age is valid.")

# Step 3: Use try...except to handle the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
except ValueError:
    print("Please enter a valid number.")


# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # Resetting current for new iteration
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num

# Example usage
for number in Countdown(5):
    print(number)
