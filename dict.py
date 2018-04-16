dict = {'nama':'Jane Doe','hp':'+27 555 5367'}
dict1 = {'nama':'John Smith','hp':'+27 555 6254'}
dict2 = {'nama':'Bob Stone','hp':'+27 555 5689'}
#MENGUBAH NOMOR HP JOHN SMITH
dict['hp'] = '+27 555 1024'
#MENAMBAH DATA BARU 
dict3={}
dict3['nama']= 'Anna Cooper'
dict3['hp'] = '+27 555 3237'
print(dict)
print(dict1)
print(dict2)
print(dict3)
#MENAMPILKAN NOMOR TELEPON BOB
print(dict2['hp'])
#MENAMPILKAN KEY DAN VALUE PADA DICTIONARY
print(dict.keys())
print(dict.values())
print(dict1.keys())
print(dict1.values())
print(dict2.keys())
print(dict2.values())
print(dict3.keys())
print(dict3.values())
