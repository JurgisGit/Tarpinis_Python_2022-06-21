# Turimas "audi" dict.

# Parašykite funkciją "show_object_values", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def show_object_values(object):
  result = object.values()
  return list(result)

list = show_object_values(audi)
print(list)


'''
for value in object.values():
  list.append(value)
return list
'''