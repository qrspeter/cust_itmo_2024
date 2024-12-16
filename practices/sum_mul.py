def our_sum(a, b):
    return a+b

def our_mul(a, b):
    return a*b
    
    
    
n = input("Input a first digit")
if n.isdigit():
    n = int(n)
print(our_sum(5,6))
print(our_sum(5.4,6))
print(our_sum('ad', 'fg'))
print(our_sum(7, 'fg'))
print(our_mul(7, 'fg'))