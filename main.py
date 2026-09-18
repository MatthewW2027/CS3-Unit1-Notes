# main() is defined with no arguments 
# def Name_of_function(): 
#   indent for code that belongs to function 
def main():
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

    name = "Matthew" 
    print(f"my name is {name} and I am in a class of {class_size} students")


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
    