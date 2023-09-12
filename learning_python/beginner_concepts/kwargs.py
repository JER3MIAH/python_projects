# **kwargs is a parameter that will pack all arguments into a dictionary
#   Its useful so a function can accept a varying amount of keyword arguments

def hello(**kwargs):  # the important thing is to have the (**), you can use any name
    print("Hello",end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(title="Mr.", first="Jeremiah", Middle="Oluwatofarati", last="Owoade")
