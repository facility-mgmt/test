import urllib.request

#urllist=["http://133.34.148.2"]
urllist=["http://133.34.148.%d"%i for i in range(2,99)]

for url in urllist:

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
        #print(body)
    except urllib.error.HTTPError as err:
        print(err.code)
    except urllib.error.URLError as err:
        print(err.reason)
