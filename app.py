import sortin
import constants
import copy


def menu():
    data = sortin.clean_data(copy.deepcopy(constants.PLAYERS))
    runit = True
    print('---------Basketball Team Stats tool---------')
    print('\n')

    while runit:
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
                teamnum = 0
                team = "Panthers"
            elif team.lower() == 'b':
                teamnum = 1
                team = "Bandits"
            elif team.lower() == 'c':
                teamnum = 2
                team = "Warriors"

        teams = sortin.balance_teams(data)

        print(f"---------{team} Stats----------")
        print(f'''
Number of players = {str(len(teams[teamnum]))}
Number of experienced players = {len([i for i in teams[teamnum] if i['experience'] == True])}
Number of noob players = {len([i for i in teams[teamnum] if i['experience'] == False])}
Average height = {str(sortin.whipheight(teams[teamnum]))}
        
Player list:
{sortin.plist(teams[teamnum])}
        
Call in case of emergency:
{sortin.guardlist(teams[teamnum])}
''')

        goodtogo = input('Do you want to keep this team? (Y/N)  ').lower()
        if goodtogo == 'y':
            print("Then Let's Get it on!!!")
            runit = False
        else:
            print('That sucks you have to start over now....\n')

if __name__ == '__main__':
    menu()