# Kelly Ann  Greene
# assignment 10- CSE 20
# This is a class that is based off of a real world object 
# Credit- I used the lecture, the textbook, and my own notes to create this script
# to get the month- https://www.geeksforgeeks.org/python-program-to-print-current-year-month-and-day/
# accessing class varibales with self- https://stackoverflow.com/questions/44460724/can-i-access-class-variables-using-self
# import random module 
import random

# define the class- 
# this class is specific lizards, their type, color, name, and where the are found
class Lizard:

# class variable
# all lizards are green
    color= "green"
# init function
# arguments are self, name, breed and color
# default arguments are leopard gecko and the continent is in a cage
    def __init__(self, name, continent):
        self.__name= name
        self.__continent= continent
    # set the country of the lizard but it can't be antartica because they are not found there
    def set_continent(self, continent):
        if "North/South America":
            self.__continent= continent
        elif "Africa":
            self.__continent= continent
        elif "Asia":
            self.__continent= continent
        elif "Europe":
            self.__continent= continent
        else:
            print("Lizards are not found there. The continents where lizards are found are 'North/South America', 'Africa', 'Asia', or 'Europe'. ")
            # raise value error
            raise ValueError
    
    # this fucntion returns the country     
    def get_continent(self):
        return self.__continent
    # this function sets the name
    def set_name(self, name):
        self.__name = name
    # this function gets the name
    def get_name(self):
        return self.__name
    
    # this function will determine the number of offspring the lizard will have

    def offspring(self):
        # if the lizard is found in Asia or Africa it will be larger and lay more eggs
        if self.__continent== "Asia" or "Africa":
            # the num of offspring will be randomly choosen between the range of 25-80
            # using the random integer module
            num_offspring= random.randint(25, 80)
            # if found in the AMericas, medium sized lizards will lay between 10 and 25 eggs
        elif self.__continent== "North/South America":
            num_offspring= random.randint(10, 25)
            # if found in Europe, small lizards will lay 1-10 eggs
        elif self.__continent == "Europe":
            num_offspring= random.randint(1, 10)
        return num_offspring
# this function counts howm many sheds the lizard has had per yea
# lizards shed every month
    def shed(self, month):
        # list of all months
        month_list = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "Decemeber"]
        # counter of how many months there are 
        shed_count= 1

        # in loop, iterate thorugh the list of month
        for i in month_list:
            # if the month is the same month as the inputted month, break out of the loop and stop iterating
            if i == month:
                break
            # increment count for each mont
            else:
                shed_count += 1
        return shed_count
    
    def __str__(self):
        # string representation 
        return(f"{self.__name} is a {(type(self).color)} lizard from {self.__continent}.")

# demo
def main():
    # this demo allows for users to input their lizard specifications 
    # then it enters an informational shell that gives tem commands they can pick to find out information about their lizard
    lizard_name = input("Input a name for your lizard:")
    lizard_continent = input("Input continent lizard is from:")
    month = input("What month is it currently?")
    x = Lizard(lizard_name, lizard_continent)
    y= (x.set_continent)
    #set new variables to the class
    print("Cool! What would you like to know about your lizard?")
    # enter while loop
    while True:
        command = input(">>>")
        # if they want to know the number of times the lizard has shed this month
        if command == "shed count":
            # calls the shed method to return the number of times it has shed
            print(f"{lizard_name} has shed {x.shed(month)} times this year.")
        # if they want to know the number of offpring

        elif command == "offspring":
            # calls the offspring method
            print(f"{lizard_name} has {x.offspring()} offspring.")
# if they just want to know the basic information about their lizard
        elif command== "basics":
            # calls the str method
            print(x)
        # give diffent options
        elif command == "help":
            print("The different commands you can choose from are: 'basics', shed count', 'offspring', 'help', or 'exit'")
        # leaves the loop
        elif command == 'exit':
            break
        # if the user inputs something else, prints an error message.
        else:
            print("Command not found. Please type 'help' to see the list of commands available.")


    
if __name__ == "__main__":
    main()