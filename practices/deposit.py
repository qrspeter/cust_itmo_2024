'''
P is the initial deposit,
r is the interest rate,
n is the number of years

A is the final amount.
'''
'''
depose = 1
rate = 1
years = 1

result = depose(1 + rate*years/100)

print(result)
'''

def depose_output(depose, rate=1, years=1):
  return 1 + rate*years/100
  
assert depose_output(1, 1, 1) == 1.01

i = int(input())


result = depose_output(i)
#print(result)
print(f"The total result is {result}.")

def round_to_n(x, n):
  if x == 0:
    return x 
  else:
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))
