import urllib2
import re
class project:
	url="http://www.shutterstock.com/?kw=websites%20for%20images&gclid=CNKn_aKOus8CFdCGaAodYFUAyQ"
	usock=urllib2.urlopen(url)
	data=usock.read()
	usock.close()
	pattern=re.compile("<img [\w\W]* src=[\"\'](.+)[\"\']>")
	f=re.findall(pattern,data)
    a=open("new.txt","w")
    a.close()
    for i in range(0,len(f)):
    	a=open("new.txt","w")
    	a.write(f[i]+'\n')
    a.close()



    

