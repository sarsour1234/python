import urllib2
import json
import datetime
aa = int(input("Enter num1: "))
bb = int(input("Enter num2: "))
cc = int(input("Enter num3: "))
dd = int(input("Enter num4: "))
ee = int(input("Enter num5: "))
ff = int(input("Enter num6: "))
gg = int(input("Enter num7: "))
kk = int(input("Enter num8:"))
ll = int(input("Enter num9: "))
oo = int(input("Enter num10: "))

num_lists=[aa,bb,cc,dd,ee,ff,gg,kk,ll,oo]
print num_lists
def compare_lists(UserList=[], Results=[]):
        same_values = set(UserList) & set(Results)
        return len(same_values)

cur_date=datetime.datetime.now()

for i in range(len(num_lists)):
	if int(num_lists[i])<1 or int(num_lists[i])>80  :
                    aa = int(input("Enter num1: "))
                    bb = int(input("Enter num2: "))
                    cc = int(input("Enter num3: "))
                    dd = int(input("Enter num4: "))
                    ee = int(input("Enter num5: "))
                    ff = int(input("Enter num6: "))
                    gg = int(input("Enter num7: "))
                    kk = int(input("Enter num8:"))
                    ll = int(input("Enter num9: "))
                    oo = int(input("Enter num10: "))
        else:
            print "GOOD JOB"  

imerominies = []
sucs = []
for i in range(31):
	cur_date = cur_date - datetime.timedelta(days=1)
	date_str = cur_date.strftime("%d-%m-%Y")
	url ='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
	req = urllib2.Request(url)
	response = urllib2.urlopen(req) 
	data = response.read()
	dataDict = json.loads(data)
	response.close()
	klhrwseis = dataDict['draws']['draw']
	r = 0
	for k in klhrwseis:
		tmp = k["results"]
		if compare_lists(num_lists, tmp)>4:
			r= r+1
	print str(r) + " exis epitixi stis: " + date_str
	sucs.append(r)
	imerominies.append(date_str)
suc=sucs[0]
Date=imerominies[0]
for i in range(1,31):
	if sucs[i]>suc:
		suc=sucs[i]
		Date=imerominies[i]
print "\n\n\tThe best day for you is: " + Date
