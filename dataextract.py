import facebook
import urllib3
import requests

token= ''#enter token
graph = facebook.GraphAPI(access_token=token, version=3.0)
likes = graph.request('/me/likes') #to extract the pages liked by me
likeList = likes['data']
likeid = likeList[1]['id']
l=[]
for i in range(0,len(likeList)): 
    x=likeList[i]['name']
    l.append(x)
for i in l:
    print (i)

feed=graph.request('/me/feed') #to extract my feed information
feedList = feed['data']
feedid = feedList[1]['id']

for i in range(0,len(feedList)): 
    x=feedList[i]['id']
    l.append(x)
for i in l:
    print (i)

personal = graph.request('me/?fields=first_name,birthday,id') #to extract personal information
print(personal)



