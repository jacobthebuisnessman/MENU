def counter():
    a = 1
    while a < 50:
     print("\n")
     a = a + 1
def menu():
  print("MENU v1.02")
  print("""
  Function1:              Function6: 
  Function2:              Function7: 
  Function3:              Function8:
  Function4:              Function9:
  Function5:              Function10:
  """)

  x = input("MENU_INPUT: ")

  if x == "1":
    Function1()

  elif x == "2": 
    Function2()

  elif x == "3": 
    Function3()

  elif x == "4": 
    Function4()

  elif x == "5": 
    Function5()

  elif x == "6":
    Function6()

  elif x == "7":
    Function7()

  elif x == "8":
    Function8()

  elif x == "9":
    Function9()

  elif x == "10":
    Function10()

############################Functions#############################

def Function1():
    print("---Function1---")
    x = input("Input1: ")
    counter()
    menu()

def Function2():
    print("---Function2---")
    x = input("Input2: ")
    counter()
    menu()

def Function3():
    print("---Function3---")
    x = input("Input3: ")
    counter()
    menu()

def Function4():
    print("---Function4---")
    x = input("Input4: ")
    counter()
    menu()

def Function5():
    print("---Function5---")
    x = input("Input5: ")
    counter()
    menu()

def Function6():
    print("---Function6---")
    x = input("Input6: ")
    counter()
    menu()

def Function7():
    print("---Function7---")
    x = input("Input7: ")
    counter()
    menu()

def Function8():
    print("---Function8---")
    x = input("Input8: ")
    counter()
    menu()

def Function9():
    print("---Function9---")
    x = input("Input9: ")
    counter()
    menu()

def Function10():
    print("---Function10---")
    x = input("Input10: ")


    menu()

############################starter######################################

menu()
