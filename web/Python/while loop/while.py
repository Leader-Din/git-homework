frouits = ['appple', 'banana', 'orange', 'mango']
frouits_len = len(frouits)
index = 0

frouits_found = False

while index < len(frouits):
    if frouits[index] == 'orange':
        frouits_found = True
        print('orange is veriable.')
        break
    index += 1
else:
    print("orange is not veriable.")