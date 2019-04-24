import pandas as pd
data = pd.read_csv('log.csv')

# pages by unique hits
pagesByHits = {}
# pages by number of users
pagesByUsers = {}
# users by unique page views
usersByPage = {}

def setPagesByHits(page):
    if page in pagesByHits:
        pagesByHits[page] = pagesByHits[page]+1
    else:
        pagesByHits[page] = 1

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
    
index = 0
while(index<data.shape[0]):
    setData(data.iloc[index])
    index = index+1

print('<<<<<<Pages by hits>>>>>')
pagesByHitsSorted = sorted(pagesByHits.items(), key=lambda x: x[1], reverse=True)
for page in pagesByHitsSorted:
    print(f'Page: {page[0]} has {page[1]} unique hits')
print()

print('<<<<<<Pages by users>>>>>')    
pagesByUsersSorted = sorted(pagesByUsers.items(), key=lambda x: len(x[1].keys()), reverse=True)
for page in pagesByUsersSorted:
   print(f'Page:{page[0]} has {len(page[1].keys())} unique viewers')
print()

print('<<<<<Users by page>>>>>>>>>>>')
usersByPageSorted = sorted(usersByPage.items(), key=lambda x: len(x[1].keys()), reverse=True)
for user in usersByPageSorted:
    print(f'User: {user[0]} has {len(user[1].keys())} unique page views')