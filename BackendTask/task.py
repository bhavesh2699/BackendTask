import requests
URL = "https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences"
r = requests.get(url=URL)
data = r.json()
# print(data.keys())
s = ''
l = dupi = sameconfprintt = []
sameconf={}
di = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August',
      'Sep': 'September','Sept': 'September', 'Oct': 'October', 'Nov': 'November', 'Dec': 'December'}


# Printing the contents in a human readable format,
print('----------------------------------Task 1-------------------------------------------------')
print("All the data in human readable format : - >")
print()
#to print from 'free' key
for i in data['free']:
    a = str(i['searchTerms'])
    x = a.split(',')
    if len(i['city'])==0:
        i['city']=x[-1]
    s=s+'"'+i['city']+' '+i['confName']+'"'+', '

    a = str(i['confEndDate'])
    x = a.split(' ')
    dt=x[1][:-1]
    if dt in di.keys():
        s=s+di[dt]
    else:
        s=s+dt
    s=s+" "+x[0]+", "+x[-1]+", "+i['venue']+", "+i['entryType']+". "+i['confUrl']
    while s[1]==" ":            # to remove extraa space
        s=s[0]+s[2:]
    print(s)
    if s in l and s not in dupi:         #to reduce redundancy.
        dupi.append(s)
    l.append(s)
    if i['confName'] in sameconf.keys() and i['confName'] not in sameconfprintt :
        sameconfprintt.append(s)
    else:
        sameconf[i['confName']]=s

    print()
    s = ''


    # print('city  '+i['city'])
    # print('keywordSupport  ' +i['keywordSupport'])
    # print('country  '+i['country'])
    # # print('imageURL  '+i['imageURL'])
    # print('venue  '+i['venue'])
    # # print('searchTerms   '+i['searchTerms'])
    # # print()
    # # print('confName   '+i['confName'])
    # print('state   '+i['state'])
    # print('long  '+i['long'])

    # print('confEndDate    '+i['confEndDate'])
    # print('conference_id   '+str(i['conference_id']))
    # print('lat   '+str(i['lat']))
    # print('confUrl   '+i['confUrl'])
    # print('entryType    '+i['entryType'])
    # print('confRegUrl    '+i['confRegUrl'])



print()
#to print from 'paid' key
for i in data['paid']:
    a = str(i['searchTerms'])
    x = a.split(',')
    if len(i['city'])==0:
        i['city']=x[-1]
    s=s+'"'+i['city']+' '+i['confName']+'"'+', '

    a = str(i['confEndDate'])
    x = a.split(' ')
    dt=x[1][:-1]
    if dt in di.keys():
        s=s+di[dt]
    else:
        s=s+dt
    s=s+" "+x[0]+", "+x[-1]+", "+i['venue']+", "+i['entryType']+". "+i['confUrl']
    while s[1]==" ":            # to remove extraa space
        s=s[0]+s[2:]
    print(s)
    if s in l and s not in dupi:         #to reduce redundancy.
        dupi.append(s)
    l.append(s)
    if i['confName'] in sameconf.keys() and i['confName'] not in sameconfprintt :
        sameconfprintt.append(s)
    else:
        sameconf[i['confName']]=s
    print()
    s = ''


print('----------------------------------Task 2-------------------------------------------------')

# Identify exact duplicates (if any)
if len(dupi)!=0:
    print("printing duplicates:- >")
    print()
    for i in dupi:
        print(i)
else:
    print("No duplicates found")


print()

print('----------------------------------Task 3-------------------------------------------------')
# Identify semantic duplicates(i.e., the conferences are same but the details provided are slightly different)
if len(sameconfprintt)!=0:
    print("printing semantic duplicates:- >")
    print()
    for i in sameconfprintt:
        print(i)
        print()

else:
    print("No semantic duplicates found")

print()
