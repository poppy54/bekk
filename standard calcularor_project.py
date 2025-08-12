from sys import exception


def calculator():
    print("Standard Calculator")
    try:
        while True:  
            op=input("Enter operation (+, -, *,**, /,and exit): ")
            if op == "exit":
                print("exiting the calculator")
                break
            list_op= ["+","-","/","*","**"]
            if op not in list_op:
                print("pleace enter valide opratore")
                continue
            #end
            numbers = []
            while True:
                number =input("entrr number or = sign in order to calculate")
                if number == "=":
                        if len(numbers)<2:
                            print("enter atlist 2 numbers")
                            continue
                        break
                try:
                     num = float(number)
                     numbers.append(num)
                except ValueError:
                    print("enter the number only! ")
                    continue
                #end 2
            if op == "+":
                result = numbers[0]
                for number in numbers[1:]:
                 result = result + number
                print("+".join(map(str,numbers))+"=" ,f"{   result}")

            elif op == "-":
                result = numbers[0]
                for number in numbers[1:]:
                    result = result - number
                print("-".join(map(str,numbers))+"=" , f"{   result}")
            elif op == "*":
                result = numbers[0]
                for number in numbers[1:]:
                    result = result * number
                print("*".join(map(str,numbers))+"=" , f"{   result}")
            elif op == "/":
                result = numbers[0]
                for number in numbers[1:]:
                    result = result / number
                print("/".join(map(str,numbers))+"=" , f"{  result}")

    except exception as e:
        print(f"invalid operation: {e}")
    print("developer by: kira & nejimi")

calculator()