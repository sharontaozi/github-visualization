import requests

language=['Python','C','C++','java','javascript','php','html','css','ruby','C#']
fout=open('language.txt','w')
for x in language:
    response=requests.get('https://api.github.com/search/repositories?q=+language:'+x).json()
    fout.write(x)
    fout.write(':')
    fout.write(str(response['total_count']))
    fout.write('\n')
fout.close()
