#coding=utf-8
import urllib
import urllib2
import re
import json

def most_star(key):
    response = urllib2.urlopen("https://api.github.com/search/repositories?q="+urllib.quote(key)+"&per_page=10&sort=stars")
    data=response.read()
    dic=json.loads(data)
    f=file("test.txt","w+")
    for i in range(0,10):
        print u"stars：",dic["items"][i]["stargazers_count"]
        print u"id：",dic["items"][i]["id"]
        print u"项目名：",dic["items"][i]["full_name"]
        print u"用户：",dic["items"][i]["owner"]["login"]
        print u"语言：",dic["items"][i]["language"]
        print u"forks：",dic["items"][i]["forks_count"]
        print u"watchers：",dic["items"][i]["watchers"]
        print u"评分：",dic["items"][i]["score"]
        print u"创建日期：",dic["items"][i]["created_at"]
        print u"更新日期：",dic["items"][i]["updated_at"]
        print '\n'      
        result=["stars："+str(dic["items"][i]["stargazers_count"])+'\n'+"id："+str(dic["items"][i]["id"])+'\n'+"项目名："+str(dic["items"][i]["full_name"])+'\n'"用户："+
                str(dic["items"][i]["owner"]["login"])+'\n'+"语言："+str(dic["items"][i]["language"])+'\n'+"forks："+str(dic["items"][i]["forks_count"])+'\n'+"watchers："+
                str(dic["items"][i]["watchers"])+'\n'+"评分："+str(dic["items"][i]["score"])+'\n'+"创建日期："+str(dic["items"][i]["created_at"])+'\n'+"更新日期："+
                str(dic["items"][i]["updated_at"])+'\n\n']
        
        f.writelines(result)
    f.close()

most_star("sql")

