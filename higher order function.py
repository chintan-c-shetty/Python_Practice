def greetlouder(name):
    print(f"the name is {name.upper()}")
def greetsofter(name):
    print(f"the name is {name.lower()}")
def display(other_def_func,name):
    print("this is display function")
    other_def_func(name)
display(greetlouder,"jenny")#here pass function only not calling it so no ()
