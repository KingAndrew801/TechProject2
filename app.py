import sortin
import constants
import copy
from varname import nameof


def menu():
    data = sortin.clean_data(copy.deepcopy(constants.PLAYERS))
    trying = True
    runit = True
    print('---------Basketball Team Stats tool---------')
    print('\n')

    while runit:
        print('---------MENU---------')
        choice = None
        while trying:
            try:
                choice = input('''
What would you like to do?
A. Display Stats
B. Quit
        
Submit your choice:   ''')
                if choice.lower() == 'b':
                    runit = False
                    trying = False
                    break

                elif choice.lower() == 'a':
                    trying = False
                    print(f'''-----Choose your team-----
A. {constants.TEAMS[0.__name__]}
B. {nameof(constants.TEAMS[1])} 
C. {nameof(constants.TEAMS[2])}
            ''')
                else:
                    raise ValueError('You have to select either A or B')
            except ValueError as err:
                print(f'{err}')

        trying = True
        while trying:
            try:
                team = input('Select your team:   ')

                if team.lower() == 'a':
                    teamnum = 0
                    team = constants.TEAMS[0]
                    trying = False
                elif team.lower() == 'b':
                    teamnum = 1
                    team = constants.TEAMS[1]
                    trying = False
                elif team.lower() == 'c':
                    teamnum = 2
                    team = constants.Teams[2]
                    trying = False
                else:
                    raise ValueError("Thats not a valid selection. Select a, b, or c.")
            except ValueError as err:
                print(f"{err}")

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

        trying = True
        while trying:
            try:
                goodtogo = input('Do you want to keep this team? (Y/N)  ').lower()
                if goodtogo == 'y':
                    print("Then Let's Get it on!!!")
                    runit = False
                    trying = False
                elif goodtogo == 'n':
                    print('That sucks you have to start over now....\n')
                    trying = False
                else:
                    raise ValueError('You have to select either Y or N')
            except ValueError as err:
                print(f'{err}')

if __name__ == '__main__':
    menu()