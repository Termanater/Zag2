#import math
#Read from input the number of people (int), average slices per person (float) and cost of one pizza (float).
#num_ppl = int(input())
#slicesEa = float(input())
#price_1pizza = float(input())
#slices_1pizza = 8

#Calculate the number of whole pizzas needed (8 slices per pizza).
#total_slices = num_ppl * slicesEa
#num_pizzas = math.ceil(total_slices / slices_1pizza)

#cost = price_1pizza * num_pizzas
#print('Friday Night Party')
#print(f"{num_pizzas} Pizzas: ${cost:.2f}")
#Set party schedule
# Type your code here. 


TI = input().split()
wages = int(TI[0])
taxable_intrest = int(TI[1])
unemployment = int(TI[2])
status = int(TI[3])
withholding = int(TI[4])
#Calculate and output AGI (wages + interest + unemployment). 
AGI = (wages + taxable_intrest +   unemployment)

if AGI > 120000:
    print(f' AGI: ${AGI:,}\nError: Income too high to use this form')
    break
else:
    print(f'AGI: ${AGI}')