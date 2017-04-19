import requests

location=['China','Canada','France','Italy','Japan','America','UK','Germany','Russia','Switzerland']
fout=open('location.txt','w')
for x in location:
    response=requests.get('https://api.github.com/search/users?q=+location:'+x).json()
    fout.write(x)
    fout.write(':')
    fout.write(str(response['total_count']))
    fout.write('\n')
fout.close()
