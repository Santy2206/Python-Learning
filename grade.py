myGrade=float(input("What's Your Grade?"))

def main():
  gradeStatus()

def gradeStatus():
  if myGrade >= 0 and myGrade<=5 or myGrade >= 10 and myGrade<=50 :
    print("Your Failed")
  elif myGrade<0 :
    print("Gosh, go and work at McDonald's")
  elif myGrade >= 5 and myGrade<=8 or myGrade >= 50 and myGrade<=80  :
    print("You Passed But Not The Best")
  else:
    print("You're Awesome")

main()