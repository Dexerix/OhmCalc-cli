#----------------------------------------------------------------------------
#                              OhmCalc-cli
# Written by                         : Dorian Luyet
# Creation date                      : 20.06.2025
# License                            : MIT
# Repository                         : https://github.com/Dexerix/OhmCalc-cli
#
# Short program description          :
#   Performs different electrical calculations based on Ohm's law   
#----------------------------------------------------------------------------

import os
import sys
import math

def treat_exp(raw_v) -> float:
    '''
    Takes the value from the input, checks if the symbol '*' is present.
    If yes, splits and calculates the value into a float to work with.

    Parameter
        raw_v (str) : value from the input
    
    Return:
        float
    '''
    if "*" in raw_v:
            split_parts = raw_v.split("*")
            base_value = float(split_parts[0])
            exponent = split_parts[1]
            exp_parts = exponent.split("^", 1)
            power = int(exp_parts[1])
            exponent = 10**power
            
            calculated_value = base_value*exponent
    else: 
            calculated_value = float(raw_v)
    
    return calculated_value

# Creation of the "Ohm" class
class Ohm():
    '''Groups the calculation methods'''
    def __init__(self) -> None:
        pass

    def voltage(self):
        '''Calculates the voltage using the resistance(Ω) and the current(Ampere)'''
        raw_r = input("Enter R : ")
        raw_i = input("Enter I : ")
        r = treat_exp(raw_r)
        i = treat_exp(raw_i)

        u = float(r*i)
        print(f"{u:.2f} V")
            
    def amperage(self):
        '''Calculates the current using the voltage(Volts) and resistance(Ω)'''
        raw_u = input("Enter U : ")
        raw_r = input("Enter R : ")
        r = treat_exp(raw_r)
        u = treat_exp(raw_u)

        i = float(u/r)
        print(f"{i:.2f} A")
    
    def resistance(self):
        '''Calculates the resistance using the voltage(Volts) and the current(Ampere)'''
        raw_u = input("Enter U : ")
        raw_i = input("Enter I : ")
        u = treat_exp(raw_u)
        i = treat_exp(raw_i)
        
        r = float(u/i)
        print(f"{r:.2f} Ω")

    def section(self):
        '''Calculates the cable\'s section using the diameter(millimeter)'''
        diameter = float(input("Enter the diameter(mm) : "))
        a = round(float((math.pi*(diameter**2)/4)), 2)
        print(f"{a:.2f} mm2")

    def resistivity(self):
        '''Calculates the resistivity(ρ) using the resistance(Ω), the section(mm2) and the length(meter)'''
        raw_r = input("Enter the resistance (Ω) : ")
        a = float(input("Enter the cable's section (mm2) : "))
        l = float(input("Enter the lenght (m) : "))
        r = treat_exp(raw_r)
    
        rho = (r*a)/l
        print(f"{rho:.2f} Ωmm2/M")
        
    def rhosistence(self):
        '''Calculates the resistance(Ω) using the resitance(ρ), the section(mm2) and the lenght(meter)'''
        rho = float(input("Enter the rho(ρ) : "))
        l = float(input("Enter the lenght(m) : "))
        a = float(input("Enter the section (mm2) : "))
        r = (rho*l)/a
        print(f"{r:.2f} Ω")

    def parallel_resistor(self):
        '''Calculates the total resistance of resistors in parallel.'''
        num_resistors=int(input('How many resistance are present on the circuit : '))
        r_list=[]
        for idx in range(num_resistors):
            ask_r=input(f'Enter the resistance {idx+1}: ')
            r = treat_exp(ask_r)
            r_list.append(r)
            total_resistance = 0
            if len(r_list) > 1:
                for r in r_list:
                    total_resistance += 1/r
                total_resistance = 1/total_resistance
            else:
                total_resistance = r_list[0]
        print(f"{total_resistance:.2f} Ω")

    def serial_resistor(self):
        '''Calculates the total resistance of resistors in serial.'''
        num_resistors=int(input('How many resistance are present on the circuit : '))
        r_list=[]
        for idx in range(num_resistors):
            ask_r=input(f'Enter the resistance {idx+1}: ')
            r = treat_exp(ask_r)
            r_list.append(r)
            total_resistance = 0
            if len(r_list) > 1:
                for r in r_list:
                    total_resistance += r
            else:
                total_resistance = r_list[0]
        print(f"{total_resistance:.2f} Ω")

# Displays the menu
def display_menu():
    '''Print a menu with the available choices'''
    menu = "===============================================\n"
    menu += "             Choose your formula\n"
    menu += "-----------------------------------------------\n"
    menu += " U - Voltage\n"
    menu += " R - Resistance (Ohm's law)\n"
    menu += " I - Current\n"
    menu += " P - Resistivity\n"
    menu += " A - Section\n"
    menu += " O - Resistence (with ρ)\n"
    menu += "PR - Parallel Resistance\n"
    menu += "SR - Serial Resistance\n"
    menu += "...\n"
    menu += ' Q - Quit\n'
    menu += "===============================================\n"
    print(menu)

def ask_user_choice(question:str):
    choice = input(question)
    try:
        letter_choice = choice
    except:
        pass
    return letter_choice

# Main function 
def main():
    '''Main function'''
    is_end_loop = False
    while not is_end_loop:
        os.system('cls')
        display_menu()
        user_choice = ask_user_choice("Your choice : ")
        user_choice = user_choice.lower()
        print()

        if user_choice == "u":
            ohms.voltage()
            input()
        elif user_choice == "r":
            ohms.resistance()
            input()
        elif user_choice == "i":
            ohms.amperage()
            input()
        elif user_choice == "p":
            ohms.resistivity()
            input()
        elif user_choice == "a":
            ohms.section()
            input()
        elif user_choice == "o":
            ohms.rhosistence()
            input()
        elif user_choice == "pr":
            ohms.parallel_resistor()
            input()
        elif user_choice == "sr":
            ohms.serial_resistor()
            input()
        elif user_choice == "q":
            is_end_loop = True
            os.system('cls' if sys.platform == 'win32' else 'clear')

ohms = Ohm()
main()
