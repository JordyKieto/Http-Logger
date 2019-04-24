import pandas as pd
data = pd.read_csv('log.csv')

pagesByHits = {}
pagesByUsers = {}
usersByPage = {}
hitIndex = 0
setIndex = 0

def setPagesByHits(page):
        global hitIndex
        if page in pagesByHits:
            pagesByHits[page][hitIndex] = 1
        else:
            pagesByHits[page] = {hitIndex : 1}
        hitIndex = hitIndex+1

def setPagesByUsers(page, user):
    if page in pagesByUsers:
        if user not in pagesByUsers[page]:
            pagesByUsers[page][user] = 1
    else:
        pagesByUsers[page] = {user: 1}

def setUsersByPage(page, user):
    if user in usersByPage:
        usersByPage[user][page] = 1
    else:
        usersByPage[user] = {page: 1}

def setData(data):
    page = data['Path']
    user = data['User']

    setPagesByHits(page)
    setPagesByUsers(page, user)
    setUsersByPage(page, user)

# text param is tuple of values being compared
def printData(data, text):
    print(f'<<<<<<{text[0]}s by {text[1]}>>>>>')
    data = sorted(data.items(), key=lambda x: len(x[1].keys()), reverse=True)
    for obj in data:
        print(f'{text[0]}: {obj[0]} has {len(obj[1].keys())} unique {text[1]}(s)')
    print()

while(setIndex<data.shape[0]):
    setData(data.iloc[setIndex])
    setIndex = setIndex+1

printData(pagesByHits, ['page', 'hit'])
printData(pagesByUsers, ['page', 'users'])
printData(usersByPage, ['user', 'page-view'])
