from utils import timer, read_file

def roman(n:int) -> str:
    """ 
        Takes a number in base 10 and returns its
        Roman Numeral representation as a string
    """

    roman_num = ""

    # Thousands
    roman_num += "M" * (n//1000)
    n %= 1000

    # Hundreds
    if n >= 900:
        roman_num += "CM"
        n -= 900
    
    else:
        if n >= 500:
            roman_num += "D"
            n -= 500

        if n >= 400:
            roman_num += "CD"
            n -= 400

        roman_num += "C" * (n//100)
        n %= 100
    
    # Tens
    if n >= 90:
        roman_num += "XC"
        n -= 90
    
    else:
        if n >= 50:
            roman_num += "L"
            n -= 50
        
        if n >= 40:
            roman_num += "XL"
            n -= 40

        roman_num += "X" * (n//10)
        n %= 10

    # Units
    if n == 9:
        roman_num += "IX"
        n -= 9
    

    else:
        if n >= 5:
            roman_num += "V"
            n -= 5

        if n >= 4:
            roman_num += "IV"
            n -= 4

        roman_num += "I" * n


    return roman_num


def parse_roman(roman:str) -> int:

    """ 
        Takes a number in its Roman Numeral representation as a string
        and returns its integer representation in base 10
    """

    result = 0

    roman = list(roman)
    
    while roman:

        # print("=======================")
        # print("roman: ", roman)
        # print("result: ", result)
        char = roman.pop(0)
        # print("char: ", char)

        if char == "M":
            result += 1000

        if char == "D":
            result += 500

        if char == "C":

            if len(roman) >= 1:
                char2 = roman.pop(0)
                # print("char2: ", char2)
            else:
                result += 100
                return result

            if char2 == "M":
                result += 900

            elif char2 == "D":
                result += 400
            
            else:
                result += 100
                roman = [char2] + roman
        


        if char == "L":
            result += 50

        if char == "X":

            if len(roman) >= 1:
                char2 = roman.pop(0)
                # print("char2: ", char2)
            else:
                result += 10
                return result

            if char2 == "C":
                result += 90

            elif char2 == "L":
                result += 40
            
            else:
                result += 10
                roman = [char2] + roman



        if char == "V":
            result += 5

        if char == "I":

            if len(roman) >= 1:
                char2 = roman.pop(0)
            else:
                result += 1
                return result

            if char2 == "X":
                result += 9

            elif char2 == "V":
                result += 4
            
            else:
                result += 1
                roman = [char2] + roman
        

    return result



@timer
def solve():

    lines = read_file("PE_89.txt")
    savings = 0
    for line in lines:

        num = parse_roman(line)

        savings += len(line) - len(roman(num))

    return savings

print(solve())
