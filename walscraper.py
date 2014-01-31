import smtplib
import requests
from BeautifulSoup import BeautifulSoup
import time
import random
nogood=1
x=0
while nogood==1:
	time.sleep(random.randint(3, 20))
	r = requests.get('http://goo.gl/GdxkKC')
	soup=BeautifulSoup(r.text)
	y = soup.find(id='shelfDiv').find(id="border")
	new = str(y)
	newfile=open('new.txt', 'w+')
	newfile.write (new)
	newfile.close()
	reopen=open('new.txt', 'w+')
	new=reopen.read()
	reopen.close()
	f=open('baseline.txt', 'w+')
	old=f.read()
	if new==old:
		print "round:  " + str(x)
	else:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login('openhaijaz@gmail.com', 'ektelo9n')
		server.sendmail("me!!", "7032258785@messaging.sprintpcs.com", "http://goo.gl/GdxkKC")
		print 'noooooooooo'
		f.write(new)
		nogood=0
		break
	f.close()