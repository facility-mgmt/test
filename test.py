import requests
import re

#urllist = ["http://133.34.148.2"]
urllist=["http://133.34.148.%d"%i for i in range(2,99)]

for url in urllist:

    try:
        #body = requests.get(url)
        body = requests.post(url + "/cgi/csdcgi", {
            'strId': 'admin', # ID
            'strPwd': 'ynu-mgmt' #PASSWORD
        })
        print url, " OK"
        #
        #TODO: Get status from status page
        #
        #result=re.match("<body>",body)
    except err:
        print url, " ERROR"
        print err.code
