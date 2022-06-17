#start with the inputs
organisms = int(input("Enter a number of organisms: "))
rateOfGrowth = int(input("Enter a rate of growth (number greater than zero): "))
rateHours = int(input("Enter number of hours needed to achieve the growth rate: "))
popHours = int(input("Enter number of hours the population will grow: "))

hours=0

while hours < popHours:
    organisms *= rateOfGrowth
    hours += rateHours

print("The total population:", str(organisms))