import constants

data = constants.PLAYERS.copy()

if __name__ == '__main__':
    def cleandata(iter):
            for i in iter:
                if i['experience'] == 'YES':
                    i['experience']  = True
                else:
                    i['experience']  = False

                i['height'] = i['height'].split()
                i['height'] = int(i['height'][0])

                i['guardians'] = i['guardians'].split(' and ')

cleandata(data)
print(data)