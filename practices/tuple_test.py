tpl1 = (1, 2.2, 'wer')
tpl2 = tpl1
print(id(tpl1))
print(id(tpl2))
del tpl1
print(tpl2)
print(tpl1)