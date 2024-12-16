'''
1. deviation - ?
2. histogram - ?
'''
'''
for(int i= 0, i < 10, ++i)
for(auto &i : array)

i = 0
while i<10:

    i += 1

'''

def standart_deviation(lst):
    average = sum(lst)/len(lst)
    
    accum = 0
    
    
    #for i in range(len(lst)):
    for i in range(len(lst)):
        accum = accum + (lst[i] - average)**2
    
    
    for i in lst:
        accum = accum + (i - average)**2
    return (accum/len(lst))**(0.5)

# 10% error is OK
assert abs(standart_deviation([0, 1, 2, 3, 4, 5]) - 1.7078251276599)/1.7078251276599 < 1e-12
assert abs(standart_deviation([0, 1, 2, 3, 4]) - 1.4142135623731)/1.4142135623731 < 1e-12

print(abs(standart_deviation([0, 1, 2, 3, 4]) - 1.4142135623731))
print((standart_deviation([0, 1, 2, 3, 4]) - 1.4142135623731))

print('Tests done')
'''
// c-style way:
double nub=standart_deviation([0, 1, 2, 3, 4, 5]);
double res = 1.7078251276599
double max=res*1.1;
double min=res*0.9;
assert (nub<=max&&nub>=min);
'''

results = [11, 11, 11, 11, 11, 10, 10, 10, 10, 
9, 9, 9, 9, 8, 8, 7, 7, 7, 7, 6, 6, 5, 4]


average = sum(results)/len(results)
deviation = standart_deviation(results)
print('The average is ', average, ', the deviation is ', deviation, '.', sep="")
print('The average is ' + str(average) + ', the deviation is ' + str(deviation) + '.')
print(f'The average is {average:.1f}, the deviation is {deviation:.1f}.')
print(f'The average is {average:.2f}, the deviation is {deviation:.3f}.')





