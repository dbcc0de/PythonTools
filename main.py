#Welcome to Bond Bot. I calculate potential earnings on government notes and bonds. I would be happy to help with your savings calculations.

name = input("Hello, I'm Bot...Bond Bot. What's your name?\n")
cash = input("It's nice to meet you, " + name + ". \nHow much money do you want to save in a US bond?\n")
bond_years = input("That's great! Now would you like to invest in a 2-year note, a 10-year note, or a 30-year bond?\nSelect 1 for a 2-year note\nSelect 2 for a 10-year note\nSelect 3 for a 30-year bond\n")

# print(f"{name} + {cash}") 
# f string helps print different data types 


while int(bond_years) <= 3 and int(bond_years)>= 1:
  if bond_years == "1":
#    print("The current rate for 2-year notes is at 5.05%, so after 2 years your initial " + "$" +  str(cash) + " will become:")
#    print((float(cash) * (1 + (.0505)/2)**(2*2)))    
    print(f"${float(cash) * (1 + (.0505)/2)**(2*2):.2f}")

  if bond_years == "2":
    print("The current rate for a 10-year note is at 3.97% so after 10 years your initial " + "$" + str(cash) + " will become:")
#    print((float(cash) * (1 + (.0397)/2)**(2*10)))
    print(f"${float(cash) * (1 + (.0397)/2)**(2*10):.2f}")

  if bond_years == "3":
    print("The current rate for a 30-year bond is 3.88% so your initial " + "$" + str(cash) + " will become :")
    print((float(cash) * (1 + (.0388)/2)**(2*30)))
    print(f"${float(cash) * (1 + (.0388)/2)**(2*30):.2f}")
  break
else:
    print("Please try running this code again.\n Input the number 1 for a 2-year note.\n Input the number 2 for a 10-year note.\n Input the number 3 for a 30-year bond.")

#Would this work? print(f"{float(cash) * (1 + (.0388)/2)**(2*30)):.2f}")

#finalamount = float(cash) * (1 + (interestrate)/12)**(12 * float(years))
# (1 + (interestrate divided by times interest compounded in year) to the power of (how often interest compounded in year * the years saved)

# finalamount = principal * (1 + interest_rate/times_compounded_in_year)**(times_compounded_in_year*years)

# Amount = Principal (1 + r/n)^nt


#print("At the end of " + str(years) + " years your initial " + str(cash) + " will become:\n"+ str(finalamount))

#Prototype calculation graveyard
  #print(cash + months + endgoal)
  #print(type(cash))
  #print(type(months))
  #print(type(endgoal))

#  if bond_years < 1 and bond_years > 3:
#    print("Invalid input, please enter 1 for a 2-year note, 2 for a 10-year note, and 3 for a 30-year bond\n")

# 