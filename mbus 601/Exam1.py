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


# Input wages0, taxable interest1, unemployment compensation2, status3 (1=single and 2=married) and taxes withheld4 as integers.
GI = input().split()
wages = int(GI[0])
taxable_interest = int(GI[1])
unemployment = int(GI[2])
status = int(GI[3])
withholding = int(GI[4])
#Calculate and output AGI (wages + interest + unemployment). 
AGI = (wages + taxable_interest +   unemployment)
#Output error message if AGI is above $120,000 and the program stops with no additional output
if AGI > 120000:
    print(f'AGI: ${AGI:,}\nError: Income too high to use this form')
else:
    print(f'AGI: ${AGI:,}')
#deduction amount based on status: (1) Single=$12,000 or (2) Married=$24,000.
    if status == 1:
        deduction = 12000
    elif status == 2:
        deduction = 24000
    else:
        status = 1 
        deduction = 12000
#Set status to 1 if not input as 1 or 2.
#calc taxable income (AGI - deduction)
    Taxable_income = AGI - deduction
    if Taxable_income < 0:
        Taxable_income = 0
    print(f'Deduction: ${deduction:,}')
    print(f'Taxable income: ${Taxable_income:,}')
    if deduction == 12000:
        if Taxable_income <= 10000:
            tax = Taxable_income*.10
            print(f'Federal tax: ${round(tax):,}')
        elif Taxable_income <40000:
            tax = 1000 + .12 * (Taxable_income - 10000)
            print(f'Federal tax: ${round(tax):,}')
        elif Taxable_income <= 85000:
            tax = 4600 + .22 *(Taxable_income - 40000)
            print(f'Federal tax: ${round(tax):,}')
        else:
            tax = 14500 + .24 * (Taxable_income - 85000)
            print(f'Federal tax: ${round(tax):,}')       
    elif deduction == 24000: 
        if Taxable_income <= 20000:
            tax = Taxable_income*.10
            print(f'Federal tax: ${round(tax):,}')
        elif Taxable_income <= 80000:
            tax = 2000 + .12 * (Taxable_income - 20000)
            print(f'Federal tax: ${round(tax):,}')
        else:
            tax = 9200 + .22 * (Taxable_income - 80000)
            print(f'Federal tax: ${round(tax):,}')
    Tax_result = (tax-withholding)
    if Tax_result <= 0:
        print(f'Tax refund: ${abs(Tax_result):,}')
    else:
        print(f'Tax Due: {abs(Tax_result):,}')        
#Calculate amount of tax due (tax - withheld). If the amount due is negative refund
#Output tax due or tax refund as positive values
            



    
         
        
        
    #if deduction == 24000 and Taxable_income < 10001 or Taxable_income >= 40000

#Calculate tax amount based on exemption and taxable income
#Tax amount should be stored as a double and rounded to the nearest whole number using round()
# Set taxable income to zero if negative. Output deduction and taxable income.
