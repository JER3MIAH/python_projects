# The scope of a variable is the region that the variable is recognized

name = "Jeremiah"   # Global variable

def show_name():
    name = "Kenneth"  # Local scoped variable
    print(name)


show_name()
print(name)
