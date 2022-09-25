import sortin
import constants
import copy


def menu():
    data = sortin.clean_data(copy.deepcopy(constants.PLAYERS))
    trying = True
    runit = True
    print('--------------------------')
    print('Basketball Team Stats Tool')
    print('--------------------------')

    while runit:
        print('-----------MENU-----------')
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

                else:
                    raise ValueError('You have to select either A or B')
            except ValueError as err:
             print(f'{err}')

        teams = sortin.balance_teams(data, constants.TEAMS)
        team = []
        for i in teams:
            team.append(i)

        print(f'''-----Choose your team-----
A. {team[0]}
B. {team[1]} 
C. {team[2]}
            ''')
        trying = True
        while trying:
            try:
                pick = input('Select your team:   ')

                if pick.lower() == 'a':
                    teamnum = 0
                    team = team[0]
                    trying = False
                elif pick.lower() == 'b':
                    teamnum = 1
                    team = team[1]
                    trying = False
                elif pick.lower() == 'c':
                    teamnum = 2
                    team = team[2]
                    trying = False
                else:
                    raise ValueError("Thats not a valid selection. Select a, b, or c.")
            except ValueError as err:
                print(f"{err}")

        print(f"---------{team} Stats----------")
        print(f'''
Number of players = {str(len([i for i in teams[team]]))}
Number of experienced players = {len([i for i in teams[team] if i['experience'] == True])}
Number of noob players = {len([i for i in teams[team] if i['experience'] == False])}
Average height = {str(sortin.whipheight(teams[team]))}
        
Player list:
{sortin.plist(teams[team])}
        
Call in case of emergency:
{sortin.guardlist(teams[team])}
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