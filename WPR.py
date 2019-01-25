import os
from optparse import OptionParser

def clear():
	os.system('cls')

print()
print("██╗    ██╗██╗███████╗██╗")
print("██║    ██║██║██╔════╝██║")
print("██║ █╗ ██║██║█████╗  ██║")
print("██║███╗██║██║██╔══╝  ██║")
print("╚███╔███╔╝██║██║     ██║")
print(" ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝\n")
print("\t██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ ")
print("\t██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗")
print("\t██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║")
print("\t██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║")
print("\t██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝")
print("\t╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ \n")
print("\t\t██████╗ ███████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██████╗ ██╗   ██╗")
print("\t\t██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝")
print("\t\t██████╔╝█████╗  ██║     ██║   ██║██║   ██║█████╗  ██████╔╝ ╚████╔╝ ")
print("\t\t██╔══██╗██╔══╝  ██║     ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗  ╚██╔╝  ")
print("\t\t██║  ██║███████╗╚██████╗╚██████╔╝ ╚████╔╝ ███████╗██║  ██║   ██║   ")
print("\t\t╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ")
print("\n\nAuthor: Priyam Harsh")

parser = OptionParser(usage="Usage: %prog [options] filename",version="%prog 1.0")
parser.add_option("-o", "--output",dest="outfilename", default='', help="Output File Name", type="str")
(options, args) = parser.parse_args()

fp = open('temp.txt','w')
fp.write(os.popen('netsh wlan show profiles').read())
fp.close()
fp = open('temp.txt','r')
profiles = [i.strip()[23:] for i in fp.readlines() if "All User Profile     :" in i.strip()]
fp.close()
print()

if options.outfilename:
	outfile = open(options.outfilename,'w')
	for ap in profiles:
		fp = open('temp.txt','w')
		fp.write(os.popen('netsh wlan show profiles name='+ap+' key=clear').read())
		fp.close()
		fp = open('temp.txt','r')
		password = ''
		for i in fp.readlines():
			if "Key Content            :" in i.strip():
				password = i.strip()[25:]
				break
		if password:
			outfile.write(ap+" => "+password+"\n")
		else:
			outfile.write(ap+" => <Open WiFi>\n")
		fp.close()
	os.remove('temp.txt')

else:
	while True:
		fp = open('temp.txt','w')
		print("Access Points:\n")
		for i in range(len(profiles)):
			print("["+str(i+1)+"]",profiles[i])
		ch = int(input("\nSelect the AP: "))
		fp.write(os.popen('netsh wlan show profiles name='+profiles[ch-1]+' key=clear').read())
		fp.close()
		fp = open('temp.txt','r')
		password = ''
		for i in fp.readlines():
			if "Key Content            :" in i.strip():
				password = i.strip()[25:]
				print("\n[+] Password:",password)
				break
		if password:
			pass
		else:
			print("\n[+] It is an open WiFi")
		fp.close()
		ch = input("\nExit ? (Y/n)")
		if ch=='Y' or ch=='y' or ch=='':
			os.remove('temp.txt')
			break
		else:
			clear()
