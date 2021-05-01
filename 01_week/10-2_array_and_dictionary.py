dictionary = {
    'pencil' : 3500,
    'pen' : 2500,
    'notebook' : 3000,
    5000 : 1500
}

#print(dictionary[0]) #출력불가
#pint(dictionary{'pencil'}] #출력불가
print(dictionary['pencil']) #정상출력
print(dictionary[5000]) #정상출력

array = [1, 2, 3]
print(array[0]) #정상출력

dictionary_in_array = [{'pencil': 3500}, {'pen' : 2500}]
print(dictionary_in_array[0]) #정상출력
print(dictionary_in_array[0]['pencil']) #정상출력