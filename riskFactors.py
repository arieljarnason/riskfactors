import string

def openfile(filename):
    """Opens file and makes strings from csv file.
       returns string, or prints error if FileNotFound"""
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
    """Converts string to list seperated by returns
    as well as catigorizing words from different 
    columns. Sends directly to find min max function"""

    line_list = string_in.split("\n"); i=0
    states=[]; heart_disease=[]; motor_vehicle=[]
    teen_birthrate=[]; adult_smoking=[]; adult_obesity=[]

    while i < len(line_list):
        temp_string = line_list[i]; i+=1
        #make temp_string from each line in list of lines
        for word in temp_string:
            #find the items we want from differenct columns in temp_string
            words = temp_string.split(",")
            
            #we look at 5 different columns, + the states
            
        states.append(words[0])
        heart_disease.append(words[1])
        motor_vehicle.append(words[5])
        teen_birthrate.append(words[7])
        adult_smoking.append(words[11])
        adult_obesity.append(words[13])

    #strip % signs
    adult_smoking = ([s.strip('%') for s in adult_smoking])
    adult_obesity = ([s.strip('%') for s in adult_obesity])

    #turn strings into floats:
    
    adult_smoking[1:-1] = [float(i) for i in adult_smoking[1:-1]]
    adult_obesity[1:-1] = [float(i) for i in adult_obesity[1:-1]]
    heart_disease[1:-1] = [float(i) for i in heart_disease[1:-1]]
    motor_vehicle[1:-1] = [float(i) for i in motor_vehicle[1:-1]]
    teen_birthrate[1:-1] = [float(i) for i in teen_birthrate[1:-1]]
    
    

    #send items to find the min and max
    find_min_max(states, heart_disease, motor_vehicle, teen_birthrate, adult_smoking, adult_obesity)

def find_min_max(states, heart_disease, motor_vehicle, teen_birthrate, adult_smoking, adult_obesity):
    """Finds the min and max in each list of words, as well
    as the index place in order to find correct correlating
    state. """

    #heart disease:
    hd_max_nr = max(heart_disease[1:-1])
    hd_min_nr = min(heart_disease[1:-1])
    hd_max_st = states[heart_disease.index((max(heart_disease[1:-1])))]
    hd_min_st = states[heart_disease.index((min(heart_disease[1:-1])))]
    print_list(heart_disease[0], hd_min_st, hd_min_nr, hd_max_st, hd_max_nr)

    #Motor vehicle death rate:
    mv_max_nr = max(motor_vehicle[1:-1])
    mv_min_nr = min(motor_vehicle[1:-1])
    mv_max_st = states[motor_vehicle.index((max(motor_vehicle[1:-1])))]
    mv_min_st = states[motor_vehicle.index((min(motor_vehicle[1:-1])))]
    print_list(motor_vehicle[0], mv_min_st, mv_min_nr, mv_max_st, mv_max_nr)

    #Teen Birth rate:
    tb_max_nr = max(teen_birthrate[1:-1])
    tb_min_nr = min(teen_birthrate[1:-1])
    tb_max_st = states[teen_birthrate.index((max(teen_birthrate[1:-1])))]
    tb_min_st = states[teen_birthrate.index((min(teen_birthrate[1:-1])))]
    print_list(teen_birthrate[0], tb_min_st, tb_min_nr, tb_max_st, tb_max_nr)

    #Adult smoking: 
    as_max_nr = max(adult_smoking[1:-1])
    as_min_nr = min(adult_smoking[1:-1])
    as_max_st = states[adult_smoking.index((max(adult_smoking[1:-1])))]
    as_min_st = states[adult_smoking.index((min(adult_smoking[1:-1])))]
    print_list(adult_smoking[0], as_min_st, as_min_nr, as_max_st, as_max_nr)

    #Adult Obesity:
    ao_max_nr = max(adult_obesity[1:-1])
    ao_min_nr = min(adult_obesity[1:-1])
    ao_max_st = states[adult_obesity.index((max(adult_obesity[1:-1])))]
    ao_min_st = states[adult_obesity.index((min(adult_obesity[1:-1])))]
    print_list(adult_obesity[0], ao_min_st, ao_min_nr, ao_max_st, ao_max_nr)



def print_error(filename):

    error = "Cannot find file"
    print(error, filename)

def print_form():
    
    print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format("Indicator","Min", '','', "Max", ''))
    print('-' * 87)


def print_list(col_1, col_2, col_3, col_4, col_5):
    
    print('{:<33}{:<21}{:>6}{:6}{:<15}{:>6}'.format(col_1, col_2, col_3,'', col_4, col_5))





def main():
    filename = input("Enter name of file: ")
    print_form()
    string = openfile(filename)
    make_list(string)






main()