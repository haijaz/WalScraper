import smtplib
import requests
from BeautifulSoup import BeautifulSoup
import time
import random

def main():
	nogood=1
	x=0
	while nogood==1:
		bitly = "http://goo.gl/WNOecx"
		time.sleep(random.randint(12, 15))
		r = requests.get(bitly)
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
			x+=1
		else:
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.starttls()
			server.login('XXXXXXXXXXXXXXXXXXX@gmail.com', 'XXXXX')
			server.sendmail("me!!", "XXXXXXXXXXXXX@messaging.sprintpcs.com", bitly)
			print 'noooooooooo'
			f.write(new)
			nogood=0
			break
		f.close()
		
if __name__ == "__main__":
    main()
