user_data = {'height': "5'\"6", 'color': 'teal', 'author': 'Henry Miller'}
print(user_data)

# The interactive part
height = input("What is your height?")
color = input("What is your favorite color?")
author = input("What is your favorite author?")
location = input("What is your location?")


user_data = {'height': height, 'color': color, 'author': author, 'location': location}
print(user_data)

# Musicians
musicians = {
                'Alessia Cara': ['Scars to Your Beautiful', 'Wild Things', 'Stay'],
                'Sia': ['Chandelier', 'Alive', 'Elastic Heart'],
                'Bob Mould': ['See a Little Light', 'Makes No Sense at All', 'Hoover Dam'],
                'Demi Lovato': ['Heart Attack', 'Cool for the Summer', 'Sorry Not Sorry'],
                'Drake': ['One Dance', 'God\'s Plan', 'Hotline Bling']
            }

print(musicians)
