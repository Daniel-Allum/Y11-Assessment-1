
Name1 = input('Name: ')
Cookie_sold1 = int(input('Cookie dough Sold: '))
Name2 = input('Name: ')
Cookie_sold2 = int(input('Cookie dough Sold: '))
Name3 = input('Name: ')
Cookie_sold3 = int(input('Cookie dough Sold: '))

print('Selling over! Lets see how everyone did!')

if Cookie_sold1 <9:
    print(f'{Name1} had {Cookie_sold1} no prize')
else:
    print(f'{Name1} had {Cookie_sold1} they recieved a prize')



if Cookie_sold2 <9:
    print(f'{Name2} had {Cookie_sold2} no prize')
else:
    print(f'{Name2} had {Cookie_sold2} they recieved a prize')



if Cookie_sold3 <9:
    print(f'{Name3} had {Cookie_sold3} no prize')
else:
    print(f'{Name3} had {Cookie_sold3} they recieved a prize')