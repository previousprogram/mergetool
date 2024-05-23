print("This is the merge game tool for merge games!")
print("Made by PreviousProgram!")

#empty dictionary to set up the usage
matdict = {
    
}

numvar = int(input('How many different types of materials do you need? '))

#sets up values in the dictionary
for x in range(numvar):
    numb = input('Input number of the ' + str(x + 1) + ' type of material needed: ')
    matdict[x] = numb


lvl = int(input('And how many levels are we going up? '))

#modifies each value in the dictionary based on the lvl put in
for x in range(numvar):
    y = matdict[x]
    modif = y * pow(2, lvl-1)
    matdict[x] = modif

print('')
#grabs these new modified values then spits them out into string form
print('To get this station to level ' + str(lvl) + '...')
for x in matdict.keys():
    print('You will need ' + str(matdict.get(x)) + ' amount of material ' + str(x+1))
