firstNumber=float(input("Value Of 1st?"))
secondNumber=float(input("Value of 2nd?"))

def main():
  compare()  

def compare():
  if firstNumber > secondNumber:
      print("firstNumber Its Grater Than secondNumber")
  elif firstNumber < secondNumber:
      print("firstNumber Its less Than secondNumber")
  else:
    print("firstNumber And secondNumber Are Equal ")
  


main()