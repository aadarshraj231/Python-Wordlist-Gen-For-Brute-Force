#!/usr/bin/python


import os
os.path.abspath(__file__)
import sys

print('******************Google Code In 2019 Python Based Wordlist Gen***************')
print()


try:
           
        #FN IS First Name ,
        #LN=Last Name ,
        #SN= Sur Name ,
        #AG= Age ,
        #BI= Bithday ,
        #NA=Nationality ,
        #PN=PN is Pet Name

	FN=input('Enter your first name: ' )
	FN=FN.lower()
	LN=input('Enter your last name: ')
	LN=LN.lower()
	SN=input('Enter your surname: ')
	SN=SN.lower()

	while True:
		try:
			AG=input('Enter your age: ')
			if not int(AG) or len(AG)>3:
				raise ValueError()
		except ValueError:
		    print ('invalide age. Please try again!')
		else:
			break

	while True:
		try:
			BI=input('Enter your birthday: ')
			if not int(BI) or len(BI)!=8:
				raise ValueError()
		except ValueError:
			print ('please, enter a valid bithday. example:DDMMYYYY')
		else:
			break

	NA=input('Enter your nationality: ')
	NA=NA.lower()
	PN=input('Enter your the name where u born: ')
	PN=PN.lower()

	Result1= str(FN+LN+SN+AG)

	pass1=FN
	pass2=LN
	pass3=SN
	pass4=AG
	pass5=BI
	pass6=NA
	pass7=PN
	pass8=FN+FN
	pass9=FN+LN
	pass10=FN+SN
	pass11=FN+AG
	pass12=FN+BI
	pass13=FN+NA
	pass14=FN+PN
	pass15=LN+LN
	pass16=LN+FN
	pass17=LN+SN
	pass18=LN+AG
	pass19=LN+BI
	pass20=LN+NA
	pass21=LN+PN
	pass22=SN+SN
	pass23=SN+FN
	pass24=SN+LN
	pass25=SN+AG
	pass26=SN+BI
	pass27=SN+NA
	pass28=SN+PN
	pass29=AG+AG
	pass30=AG+FN
	pass31=AG+LN
	pass32=AG+SN
	pass33=AG+BI
	pass34=AG+NA
	pass35=AG+PN
	pass36=BI+BI
	pass37=BI+FN
	pass38=BI+LN
	pass39=BI+SN
	pass40=BI+AG
	pass41=FN+FN+FN
	pass42=FN+FN+LN
	pass43=FN+FN+SN
	pass44=PN+BI[4:8]+SN+PN
	pass45=PN+BI[4:8]+AG+PN
	pass46=PN+BI[4:8]+BI[4:8]+PN
	pass47=PN+BI[4:8]+NA+PN
	pass48=PN+BI[4:8]+PN+PN
	pass49=PN+NA+BI[4:8]+PN
	pass50=FN+PN+LN
	

	print ()
	#Simple & .upper(), & .capitalize(),
	liste=[
                pass1,pass2,pass3,pass4,pass5,pass6,pass7,pass8,pass9,pass10,pass11,pass12,pass13,pass14,pass15,pass16,pass17,pass18,pass19,pass20,pass21,pass22,pass23,pass24,pass25,pass26,pass27,pass28,pass29,pass30,pass31,pass32,pass33,pass34,pass35,pass36,pass37,pass38,pass39,pass40,pass41,pass42,pass43,pass44,pass45,pass46,pass47,pass48,pass49,pass50,
                pass1.upper(),pass2.upper(),pass3.upper(),pass4.upper(),pass5.upper(),pass6.upper(),pass7.upper(),pass8.upper(),pass9.upper(),pass10.upper(),pass11.upper(),pass12.upper(),pass13.upper(),pass14.upper(),pass15.upper(),pass16.upper(),pass17.upper(),pass18.upper(),pass19.upper(),pass20.upper(),pass21.upper(),pass22.upper(),pass23.upper(),pass24.upper(),pass25.upper(),pass26.upper(),pass27.upper(),pass28.upper(),pass29.upper(),pass30.upper(),pass31.upper(),pass32.upper(),pass33.upper(),pass34.upper(),pass35.upper(),pass36.upper(),pass37.upper(),pass38.upper(),pass39.upper(),pass40.upper(),pass41.upper(),pass42.upper(),pass43.upper(),pass44.upper(),pass45.upper(),pass46.upper(),pass47.upper(),pass48.upper(),pass49.upper(),pass50.upper(),
                pass1.capitalize(),pass2.capitalize(),pass3.capitalize(),pass4.capitalize(),pass5.capitalize(),pass6.capitalize(),pass7.capitalize(),pass8.capitalize(),pass9.capitalize(),pass10.capitalize(),pass11.capitalize(),pass12.capitalize(),pass13.capitalize(),pass14.capitalize(),pass15.capitalize(),pass16.capitalize(),pass17.capitalize(),pass18.capitalize(),pass19.capitalize(),pass20.capitalize(),pass21.capitalize(),pass22.capitalize(),pass23.capitalize(),pass24.capitalize(),pass25.capitalize(),pass26.capitalize(),pass27.capitalize(),pass28.capitalize(),pass29.capitalize(),pass30.capitalize(),pass31.capitalize(),pass32.capitalize(),pass33.capitalize(),pass34.capitalize(),pass35.capitalize(),pass36.capitalize(),pass37.capitalize(),pass38.capitalize(),pass39.capitalize(),pass40.capitalize(),pass41.capitalize(),pass42.capitalize(),pass43.capitalize(),pass44.capitalize(),pass45.capitalize(),pass46.capitalize(),pass47.capitalize(),pass48.capitalize(),pass49.capitalize(),pass50.capitalize(),
	]
	#print ('\n'.join(liste))

	my_file = open('gci.txt', 'w')
	my_file.write(str('\n'.join(liste)))
	my_file.close()

	print ('All passwords are saved in gci.txt file!')



except (KeyboardInterrupt, SystemExit):
    print('\n\t\n[!] Session Cancelled')
