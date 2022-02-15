import random
import datetime

def rndn():
	omegapy_code = ['01ox%s','02ox%s','03ox%s','04ox%s','05ox%s','06ox%s','07ox%s','08ox%s','09ox%s','10ox%s']
	omg=[]
	for i in omegapy_code:
		omg.append(i % str(random.randint(123456,987654)))
        
	return random.choice(omg)


def dateUtime():
	from time import time
	from datetime import datetime
	now = time()
	now = str(datetime.fromtimestamp(now))
	now = now[:now.find('.')]
	return now             

def zbotc():
	_Alf = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ_.'
	op = ''
	l = 26
	for i in range(l):
		flag = random.randint(0,3)
		if flag == 2:
			_flag = random.randint(0,2)
			if _flag == 2:
				op += str(random.randint(0,99))
			else:
				op += str(random.randint(0,10))
		else:
			op += random.choice(_Alf)
	return op

def zbotid():
	op = '0e%s'
	op = op % str(random.randint(123456,987654))
	return op


