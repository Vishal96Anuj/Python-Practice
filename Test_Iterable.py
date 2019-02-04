#check object is iterable or not
def check_Iterable(obj):
  try:
    iter(obj)
    return True
  except TypeError:
    return False

l=['V',25,30.5,'Hello',[45,30.2,78,'S'],('yes',56,23.8,63,'No'),{'a':8}]
  
for i in l:
  print(i," is ITERABLE :",check_Iterable(i))
