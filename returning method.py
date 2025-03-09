def hello(name):
    def greet():
        print("jai shree ram")
    def welcome():
        print("hare krishna")
    if name=="jenny":
        return greet#here we only pass
    else:
        return welcome
new_method=hello("jenny")
new_method()#here we call the function
new_method1=hello("jennyy")
new_method1()