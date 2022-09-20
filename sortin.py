import constants

data = constants.PLAYERS.copy()
Panthers = []
Bandits = []
Warriors = []
teams = Panthers, Bandits, Warriors


def clean_data(itera):
        for i in itera:
            if i['experience'] == 'YES':
                i['experience']  = True
            else:
                i['experience']  = False

            i['height'] = i['height'].split()
            i['height'] = int(i['height'][0])
            i['guardians'] = i['guardians'].split(' and ')


def balance_teams(itera):
    exp_players = []
    newbs = []

    for i in itera:
        if i['experience'] == True:
            exp_players.append(i)
        else:
            newbs.append(i)

    while exp_players:
        for t in teams:
            t.append(exp_players[0])
            exp_players.remove(exp_players[0])

    while newbs:
        for t in teams:
            t.append(newbs[0])
            newbs.remove(newbs[0])


def whipheight(team):
    height_pool = []
    for i in team:
        height_pool.append(i['height'])
    return round(sum(height_pool)/len(height_pool))

if __name__ == '__main__':

    newnie = clean_data(data)
    balance_teams(data)

    print(whipheight(teams[0]))