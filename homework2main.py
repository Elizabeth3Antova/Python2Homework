
#1
Degrees = float(input("Enter degrees to convert them into radians: "))
pi= 3.14159265359
Radians = (Degrees*pi)/180
print(round(Radians,5))

#2 Write a program that calculates the subscription fee for a utility meter (for example, electricity or gas).
PreviousCounterReading = 58.758
CurrentReading = 86.896
TariffPerKilowatt = float(input("Please the price for one kilowatt : "))
#how much to pay, rounded to two decimal places
Total_for_thelight = (CurrentReading-PreviousCounterReading)*TariffPerKilowatt
print(round(Total_for_thelight,2))

# 3 Write a program that calculates the income tax on the entrepreneur's account.
income=15000.59 
tax_percentage= 5
tax_should_be_paid = (income*tax_percentage)/100
net_profit= income - tax_should_be_paid
#both values are rounded to two decimal places
print("Tax that should be paid =")
print (round(tax_should_be_paid, 2))
print("Net profit =",net_profit)
print (round(net_profit,2))

# 4. Write a program that calculates fuel costs.
fuel_consumption_per100_km = 7.1
PricePer1Liter= 51.44
Km = TariffPerKilowatt = float(input("How many kilometers do you have to travel?  "))
Price = ((Km*fuel_consumption_per100_km)/100) * PricePer1Liter
print("The total price  for the fuel will be:")
print(round(Price,2))
