import string

def openfile(filename):
    """Opens file and makes strings from csv file"""
    wordString = ''	# start with an empty string of words 
    
    try:
        with open(filename, 'r', encoding='utf-8') as dataFile:
            for line in dataFile: 
                wordString += line # add each line of words to the word string 
        return wordString

    except FileNotFoundError:
        print_error(filename)
        print_form()
   

def make_list(string_in):
    """Converts string to list seperated by spaces"""
    newlist = string_in.split(",") 

    return newlist

def print_error(filename):

    error = "Cannot find file"
    print(error, filename)

def print_form():
    
    print('{:<33}{:<21}{:<6}'.format("Indicator","Min","Max"))
    print("---------------------------------------------------------------------------------------")


def print_list(output):
    print_form()
    print(output)


def main():
    filename = input("Enter name of file: ")
    fancy_output = openfile(filename)
    print_list(fancy_output)


main()