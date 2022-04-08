import json
import pyfiglet
import sys

def banner():
	ascii_banner = pyfiglet.figlet_format("ScriptKiddieHub")
	print(ascii_banner)


def picker():
	try: 
		arg = sys.argv[1]
		if sys.argv[1] == 'usernames':
			opener('username')
		elif sys.argv[1] == 'passwords':
			opener('password')
		elif sys.argv[1] == 'IP' or sys.argv[1] == 'ip':
			opener('src_ip')
		else:
			banner()
			print('Usage: {} <category> {}'.format(sys.argv[0],categories))
	except IndexError:
		banner()
		raise SystemExit('Usage: {} <category> {}'.format(sys.argv[0],categories))
	

def opener(category_option):
	'''opening the .json file to print out the whole category'''
	for line in f:
		data = json.loads(line)
		print()
		for i in data[category_option]:
			print(i,end='')
		

if __name__ == "__main__":
	global categories
	categories = ('usernames', 'passwords', 'IP')
	try:
		f = open('passwords.json')
	except:
		print('An error occured, does the file exist?')
	picker()
	f.close()