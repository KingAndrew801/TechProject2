import constants

data = constants.PLAYERS.copy()
Panthers = []
Bandits = []
Warriors = []
teams = Panthers, Bandits, Warriors

if __name__ == '__main__':
    def clean_data(iter):
            for i in iter:
                if i['experience'] == 'YES':
                    i['experience']  = True
                else:
                    i['experience']  = False

                i['height'] = i['height'].split()
                i['height'] = int(i['height'][0])
                i['guardians'] = i['guardians'].split(' and ')


    def balance_teams(iter):
        exp_players = []
        newbs = []

        for i in iter:
            if i['experience'] == True:
                exp_players.append(i)
            else:
                newbs.append(i)

        while exp_players:
            for t in teams:
                print(t)
                t.append(exp_players)
                exp_players.remove(exp_players[0])

newnie = clean_data(data)
balance_teams(data)
print (teams)
