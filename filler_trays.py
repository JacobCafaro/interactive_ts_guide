#Once user selects filler and filler trays
outie = 'Excellent, select "Exit" to return to the home page'

print('Ensure all trays are in the correct position.')
a_0 = input('\nHas the issue been resolved (Yes or No): ')
a_0 = a_0.title()
if a_0 == 'Yes':
    print(outie)
else:
    scope = input("Are all trays affected (Yes or No): ")
    scope = scope.title()
    if scope == 'Yes':
        print('Adjust vibrator amplitude as necessary.')
        a_1 = input('\nHas the problem been resolved (Yes or No): ')
        a_1 = a_1.title()
        if a_1 == "Yes":
            print(outie)
        else:
            print('Adjust gate height to control product flow as necessary.')
            a_2 = input('\nHas the issue been resolved (Yes or No): ')
            a_2 = a_2.title()
            if a_2 == 'Yes':
                print(outie)
            else:
                print('Call maintenance.')
    else:
        t_sus = input('Are all trays uniformly suspended (Yes or No): ')
        t_sus = t_sus.title()
        if t_sus == 'Yes':
            print('Call maintenance')
        else:
            print('Switch out trays with improper suspension.')
            a_3 = input('\nHas the issue been resolved (Yes or No): ')
            a_3 = a_3.title()
            if a_3 == 'Yes':
                print(outie)
            else:
                print('Call maintenance and return to home screen.')