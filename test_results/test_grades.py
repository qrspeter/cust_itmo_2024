import pprint

def load_names(filename):

    fin = open(filename, 'r')
    members = fin.readlines()
    fin.close()

    dct = {}

    for name in members:
        name = name.strip()
        dct[name] = []
    
    return dct
    
def load_results(filename, dct):
    
    fin = open(filename, 'r')
    members = fin.readlines()
    fin.close()

    for m in members:
        m = m.strip()
        lst = m.split(sep='\t')
        name = lst[0] + " " + lst[1]
        result = [float(lst[2])]
        dct[name] = dct[name] + result
        
def normalize_dct(dct, max_points):
    dct_norm = {}
    max_point = 10
    for name, grades in dct.items():
        grades_norm = []
        for n, grade in enumerate(grades):
            grades_norm.append(round(max_point * grade/max_points[n]))
        dct_norm[name] = grades_norm
        
    return(dct_norm)
    

if __name__ == "__main__":    

    test_files = ['input_test.txt', 'test1.txt', 'test2.txt'] 
    max_points = [15, 27, 19]
    practice_files = ['practice1.txt', 'activity1.txt']
    names = 'students_names.txt'

    dict_31 = load_names(names)

    for file in test_files:
        #print(file)
        load_results(file, dict_31)

    #print(dict_31)
    pprint.pprint(dict_31, sort_dicts=False)
    
    dict_31_norm = normalize_dct(dict_31, max_points)

    for file in practice_files:
        load_results(file, dict_31_norm)

    with open(__file__[:-2] + 'txt', 'w') as f:  
        for name, grades in dict_31_norm.items():  
            st = ',\t'.join([str(round(i)) for i in grades])
            fstring = f'{name + ":":15s} {st}'
            f.write(fstring + '\n')
            print(fstring)