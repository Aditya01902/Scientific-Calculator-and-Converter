def parser(expression):

    tokens = []
    number = ""

    for idx, value in enumerate(expression):
        
        if value.isdigit() is True or value == ".":
            number += value
            continue

        if value in ["+", "-", "*", "/", "(", ")"]:
            
            pass

            if idx == 0 and value == "-": 
                number += "-"
                continue

            if value in ["-", "+"] and (idx == 0 or expression[idx-1] in ["(", "+", "-", "*", "/"]):
                # flush existing number first
                if number != "":
                    tokens.append(number)
                    number = ""
                number += value
                continue

            if (value in  ["+", "-"] and expression[idx+1] in ["(", "+", "-", "*", "/"] and expression[idx-1].isdigit() is False):
                print("Here ", idx, expression[idx+1])
                tokens.append(value)
                continue

            if number:
                tokens.append(number)
                number = ""
            tokens.append(value)

        
    if number != "": # To append the last element of expression
        tokens.append(number)

    print(expression)   
    print(tokens)

parser("4-+-3+5") #-(-3.5+2)
parser("-(-3.5+2)")

