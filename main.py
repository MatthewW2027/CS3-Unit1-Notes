# main() is defined with no arguments 
# def Name_of_function(): 
#   indent for code that belongs to function 
def main():
    name = "Matthew"
    other_name = "Danny"
    function_with_args(name)
    function_with_args(other_name)
    class_size = 7
    # Quotes for strings
    # prtinting with type casting and concatenating 
    print("hello world " + str(class_size) + "!")
    # single apostraphes 
    print('hello world')
    # triple quotes 
    print("""hello world""")

    # prtinting with fStrings 
    print(f"hellow class of {class_size}!")


    number = "5.0" 
    print(f"My number is {int(float(number))}")
    print(f"My number is {type(int(float(number)))}")
    name_of_function()
    print("all done!")

def name_of_function():
      # sample function to show structure 
      print("good example!")

def function_with_args(name):
      print(f"Hello, thank you for your focus {name}")
    


if __name__ == "__main__":
        main()

# variable name example: more_than_one_word 
# NOT ALLOWED TO START VARIABLE NAMES LIKE THIS
# starting with a number, special char, keywords: and, if, ture, false 
# careful: int, list, str - can be overwritten 

# numbers: 
    # int: x = 500 
    # floats: x = 500.1 
    # complex: x = 30j 
    # x = 75 float(75) - used to change a varibale type 
        # example: grade = 92.875 
        # print("your grade is: ")
        #print (int(grade))
    # division automatically gives you a float and if you wanted an int you would have to cast it 
    