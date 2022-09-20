import sortin
import constants


data = sortin.clean_data(constants.PLAYERS.copy())
Panthers = []
Bandits = []
Warriors = []
teams = Panthers, Bandits, Warriors


def menu():
    runit = True
    print('---------Basketball Team Stats tool---------')
    print('\n')
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
            A. Panthers
            B. Bandits 
            C. Warriors
            ''')
            team = input('Make you selection:   ')
            if team.lower() == 'a':
                team = Panthers
            elif team.lower() == 'b':
                team = Bandits
            elif team.lower() == 'c':
                team = Warriors

print(constants.PLAYERS)
print(sortin.clean_data(constants.PLAYERS.copy()))
print(data)
# team = Panthers
# sortin.balance_teams(data)
# print(teams)
# print(f"----{team} Stats-----")
# print('''Average height = ''' + sortin.whipheight(teams[1]))