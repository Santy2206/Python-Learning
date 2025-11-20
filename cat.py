userInput=int(input("How Many Times?"))
def main():
    times=get_positive_value(userInput)
    meow(times)

def get_positive_value(input):
    while True:
        if input>0:
            break
    return input
def meow(amount):
    for _ in range(amount):
        print("meow")
main()


