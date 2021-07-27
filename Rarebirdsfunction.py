#Nested dicitonary which was used to capture the different species of exotic birds as outer dictionary keys and the values are dictionaries
#of the height(m), weight(kg), color, endangered category, aggrssiveness category specifications.

rarebirds = {
    'Gold-crested Toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggressive': True },
    'Pearlescent Kingfisher': {
        'Height (m)': 0.25,
        'Weight (kg)': 0.5,
        'Color': 'White',
        'Endangered': False,
        'Aggressive': False },
    'Four-metre Hummingbird': {
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggressive': False },
    'Giant Eagle': {
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggressive': True },
    'Ancient Vulture': {
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggressive': False }    
}

#List which was used to store the various possible locations of the exotic birds

birdlocation = [
    "In the canopy directly above our heads",
    "Between my 6 and 9 o’clock above",
    "Between my 9 and 12 o’clock above",
    "Between my 12 and 3 o’clock above",
    "Between my 3 and 6 o’clock above",
    "In a nest on the ground",
    "Right behind you"
 ]

#Dictionary which was used to encode the possible bird locations into binary codes

codes = {
    '111':birdlocation[0],
    '110':birdlocation[1],
    '101':birdlocation[2],
    '100':birdlocation[3],
    '011':birdlocation[4],
    '010':birdlocation[5],
    '001':birdlocation[6],
    '000':'undefined'
}

#List used to store the actions that will reduce our options for us humans of being spotted when trying to photograph the birds

actions = [
    "Back Away",
    "Cover our Heads",
    "Take a Photograph"
]

#Print statement which tells the photographer whether the Giant Eagle bird is aggressive or not; the output is True or False

print(rarebirds["Giant Eagle"]["Aggressive"])


#This for-loop is used to either print or not print messages for different birds found in the rarebirds dictionary; the criteria for the messages
#are the Aggressiveness and Endangerment risk for each bird

for k,v in rarebirds.items():
    print('This bird is a/an' + ' ' + k)
    if (rarebirds[k]['Aggressive']):
        print('It is advised that we' + ' ' + actions[1] + ' ' + 'because they are aggressive')
    if (rarebirds[k]['Endangered']):
        print('It is advised that we' + ' ' + actions[0] + ' ' + 'because they are an endangered specie')

#This for-loop is used to print out what each binary code encoding refers to in terms of the birdslocation message list

for k,v in codes.items():
    print(k + ' ' + 'is the binary code encoding for the birdslocation message:', codes[k])

#This for-loop is used to add an extra attribute 'Seen' to the orginal rarebirds inner dictionary. The new attribute will be part of the
#existing keys found in the inner dictionary

for k,v in rarebirds.items():
    rarebirds[k]['Seen'] = 'False'
#print(rarebirds)


#This is a helper fucntion that is used to check if the user input from 'sighting' is in fact a bird contained
#in the rarebirdsList. The function takes a string and returns True if the input string is contained in the rarebirdslist, without taking 
#any account of the case sesnsitivity of the string

def sightbird(Bird):#, rarebirdsList):
    for i in range(len(rarebirdsList)):
        rarebirdsList[i] = rarebirdsList[i].casefold() #The casefold str.method() is used for making caseless comparisons between strings
        if (Bird.casefold() == rarebirdsList[i]): #This compares the input argument Bird to the ith iteration of elements in the rarebirdslist
            print('That is one of the rare birds haha!') #If Bird is in fact in the rarebirdslist and is equal to the ith iteration of question, we print a message and return True
            return True
       
    print(Bird.title() + ' ' + "is not one of the birds we're looking for!") #If Bird is not in the rarebirdslist we print a different message and return False
    return False

rarebirdsList = list(rarebirds.keys()) 
#print(rarebirdsList)
encounter = True #New variable encounter intialized with a boolean 'True' value

#Large while-loop which essentially checks whether we saw a rarebird in the rarebirds list. If we did see one, we see some messages in regards to the agrresiveness or endangered category of the bird. If we did not see one, we will be prompted to continue inputting a bird we see, until we get one that is in the rarebirdslist.
while encounter: 

    sighting = input('What do you see? ')#User input variable sighting, used for storing what type of bird the person sees
    sighting = sighting.lower()
    
    
    if sightbird(sighting):#if statement which is a fuction call of helper funtion sightbird, it should return True if the user input of sighting is a bird in the rarebirdslist

        code = input('Where do you see it? ')#User input variable code, used for storing where the person sees "what" they see.

        location = codes[code]#This is used to get bird location from the codes dictionary, 
        #which should be a binary code that matches some bird location in real-time

        #Print statement which summarizes what type of bird I saw and the location seen at based on user inputs
        print('Damn brother! You saw a', sighting.title(), location.lower() + ',' + ' ' + 'that must have been traumatising lol')
        
        #The split() and join() str.methods were needed because birds like the Gold-crested Toucan and Four-metre Hummingbird presented us with bugs.
        #The bug was that gold-crested toucan is defined as "Gold-crested Toucan" in the rarebirdsdict; the first and last words of the string are capital, while the middle word 
        #is lowercase. The sighting user inout varibale makes lowercase for the input on line 120 and would make our program to think that we actually do not see the correct bird 
        #because dictinaries are case sensitive. So to fix this, I needed to get the user-input into the correct format so the string can be located in the rarebirdslist
        #I had to split the strings first, for example splitting the Gold-crested toucan characters into a list with split being delimited by space.
        #After the split you join the new list string elements with the correct punctuation and you should be able to find the bugged user inputs of gold-crested toucan and
        #four-metre humminhbird in the rarebirdslist
        
        sighting = sighting.split(' ') #'gold-crested toucan'.split(' ') results in a list = ['gold-crested', 'toucan']
        sighting = ' '.join([sighting[0].capitalize(),sighting[1].capitalize()]) #' '.join([['gold-crested', 'toucan'][0].capitalize(),['gold-crested', 'toucan'][1].capitalize()])
        #results in 'Gold-crested Toucan'
        
        if rarebirds[sighting]['Aggressive'] == True:
            print('The' + ' ' + sighting.title() + ' ' + 'is an agggressive bird specie and we need to', actions[0].lower() + ' ' + 'and ' 
            + actions[1].lower() + '!'
            )
            print('We need to photograph the' + ' ' + sighting.title(), location.lower())
            break

        elif rarebirds[sighting]['Endangered'] == True:
            print('The' + ' ' + sighting.title() + ' ' + 'is an endangered bird specie and we need to', actions[0].lower() + '!')
            print('We need to photograph the' + ' ' + sighting.title(), location.lower())
            break

        else:
            print('We need to photograph the ultra-rare' + ' ' + sighting.title(), location.lower())
            break







