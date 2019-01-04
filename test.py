import requests
import re

id = 'admin'
password = 'ynu-mgmt'

#Yokohama national univ.
#http://133.34.148.101

urllist = ["http://133.34.148.2"]
#urllist=["http://133.34.148.%d"%i for i in range(2,99)]

for url in urllist:
    try:
        #body = requests.get(url)
        body = requests.post(url + "/cgi/csdcgi", {
            'strId': id,
            'strPwd': password
        })
        print url, " OK"
    #
    #TODO: Get status from status page
    #
    #result=re.match("<body>",body)
    except err:
        print url, " ERROR"
        print err.code
