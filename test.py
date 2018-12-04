import requests

#urllist = ["http://133.34.148.2"]
urllist=["http://133.34.148.%d"%i for i in range(2,99)]

for url in urllist:

    try:
        #body = requests.get(url)
        body = requests.post(url + "/cgi/csdcgi", {
            'strId': 'admin',
            'strPwd': 'ynu-mgmt'
        })
        print url, " OK"
        #
        #TODO: Get status from status page
        #
    except err:
        print url, " ERROR"
        print err.code
