th_b = [0, 150000, 300000, 500000, 750000, 1000000, 2000000, 5000000]
th_r = [0, .05, .1, .15, .2, .25, .3, .35]

us_b = [0, 9700, 39475, 84200, 160725, 204100, 510300]
us_r = [.1, .12, .22, .24, .32, .35, .37]

def tax(income, brackets, rates):
    i = 0
    result = 0
    # Handle brackets
    while i+1 < len(brackets):
        if income > brackets[i] and income <= brackets[i+1]:
            taxable = income - brackets[i]
        elif income > brackets[i+1]:
            taxable = brackets[i+1] - brackets[i]
        else:
            taxable = 0
        result += rates[i] * taxable
        i += 1
    # Now the top bracket
    if income > brackets[i]:
        taxable = income - brackets[i]
        result += taxable * rates[i]
    return result

gross_th = 600000*12
gross_us = gross_th / 30
tax_th = tax(gross_th, th_b, th_r)
tax_us = tax(gross_us, us_b, us_r)

total_us = tax_us + tax_th/30
total_th = total_us * 30
print("Gross income:", gross_us)
print("Total TH+US taxes:", total_us)
print("Net income:", gross_us-total_us)
