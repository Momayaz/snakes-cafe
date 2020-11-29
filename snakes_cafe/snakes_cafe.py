
from menu import Appetizers,Entrees,Desserts,Drinks

def basics():
 print("**************************************")
 print("**    Please see our menu below.    **")
 print("**")
 print("** To quit at any time, type quit **")
 print("**************************************")
 
 print("Appetizers")
 for i in Appetizers:
    print(i)

 print("Entrees")
 print("-------")

 for i in Entrees:
    print(i)

 print("Desserts")
 print("-------")

 
 for i in Desserts:
    print(i)

 print("Drinks")
 print("-------")
 for i in Drinks:
    print(i)


 i = 1
 while True:
     print("***********************************")
     order = input("** What would you like to order? **")
     print('***********************************')

     print(f">{order}")
     print(f"** {i} order of Wings have been added to your meal **")

     i+=1
     reply = input("If you want to exit, just type quit!")
     if reply == "quit":
       break
    

if __name__ == "__main__":
    basics()

   
    
