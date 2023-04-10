# get two integer parameters
# return sum
def plus(x, y):
    return x+y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus")
        check = int(input())
        if check == 1:
            check2 = 1
            while check2 == 1:
                print("First Number")
                x = input()
                if not x.isdigit():
                    print("숫자를 입력하시오")
                else:
                    break
            check3 = 1
            while check3 == 1:
                print("Second Number")
                y = input()
                if not y.isdigit():
                    print("숫자를 입력하시오")
                else:
                    check3 = 2
            print("answer : ", plus(int(x), int(y)))
        elif check > 1:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
