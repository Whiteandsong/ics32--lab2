#lab2.py

# Starter code for lab 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Ziyan Bi
# ziyanb@uci.edu
# 75947710

def add(a, b):
    return  a + b

def sub(a, b):
    return  a - b

def div(a, b):
    return  a / b

def mul(a, b):
    return  a * b

def reload():
    response = input("Run another calculation (y/n)? ") 
    if response.lower() == "y":
        run()
    elif response.lower() != "n":
        raise Exception("Invalid input. Please enter 'y' to run another calculation or 'n' to stop.")


def run():
    a = input("Enter left operand: ")
    b = input("Enter right operand: ")
    operator = input("What type of calculation would you like to perform (+, -, x, /)? ")
    
    r = 0
    
    try:
        if not a.isdigit() or not b.isdigit():
            raise Exception("Invalid operand! Please enter integers.")
        if operator == "+":
            r = add(int(a),int(b))
        elif operator == "-":
            r = sub(int(a),int(b))
        elif operator == "x":
            r = mul(int(a),int(b))
        elif operator == "/":
            r = div(int(a),int(b))
        else:
            raise ValueError("Invalid operator!")
    except Exception as e:
        print("Unable to perform the desired calculation, please try again.")
        print(f'Error: {e}')
    else:
        print(r)
    finally:
        try:
            reload()
        except Exception as e:
            print(f'Error: {e}')
            reload()

if __name__ == "__main__":
    print("Welcome to PyCalc!")
    run()
    
    
        
