print('---------Basketball Team Stats tool---------')
print('\n')

runit = True

while runit:
    team = None


    print('---------MENU---------')
    choice = None
    choice = input('''
    What would you like to do?
    A. Display Stats
    B. Quit
    
    Submit your choice:   ''')
    if choice.lower() == 'b':
        runit = False
        break
    elif choice.lower() == 'a':
        print('''-----Choose your team-----
        A. Killers
        B. Stud Squad
        C. Unicorns
        ''')
        team = input('Make you selection:   ')
        if team.lower() == 'a':
            team = 'Killers'
        elif team.lower() == 'b':
            team = 'Stud Squad'
        elif team.lower() == 'c':
            team ='Unicorns'
