
"""Task 1

Create a variable called fruits and one after another add the elements Apples, 
Cherries and Strawberries. Loop over the list fruits and print every element to the screen.
"""


# fruits =[]

# fruits.append('Apples')
# fruits.append('Cherries')
# fruits.append('Strawberries')

# for i in fruits:
#     print(i)


"""Task2
Create a variable cities which holds a list with the cities 
London, Paris, Berlin and Amsterdam. Print the sentence The capital city of Germany is: 
Berlin to the screen, using the string Berlin from the cities array."""


# cities = ['London', 'Paris', 'Berlin', 'Amsterdam']

# print(f'The capital city of Germany is: {cities[2]}')


"""Task3
Store the colors cyan, magenta, green, yellow, black and white in a list called colors. 
Remove the colors green and white. Print the remaining colors to the screen."""

# colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']

# colors.remove('green')
# colors.remove('white')

# for i in colors:
#     print(i)

#----------------------------------------------------------------------

# colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']

# del colors[3]
# del colors[-1]

# for i in colors:
#     print(i)

#----------------------------------------------------------------------

colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']

third_color = colors.pop(2)
last_color = colors.pop()


print(third_color)
print(last_color)
print('--------')
for i in colors:
    print(i)
    
    
    
"""Task 4

Store the letters p, e, n, g, u, i, n in a list. 
Combine those letters into a single string penguin. 
Capitalize that string and print it to the screen."""


# letters = ['p', 'e', 'n', 'g', 'u', 'i', 'n']


# letters = "".join(letters)

# print(letters.capitalize())