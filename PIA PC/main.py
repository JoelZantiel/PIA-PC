import argparse
from Virus import virusT # Del script Virus importa la funcion virusT
import getpass # para contraseñas y claves APi
from extractDataFromImages import ValidatePath, printMeta # Importa las funciones del script extractDataFromImages
from Scraping import Scraping # Importa la clase Scraping
from sendEmail import sendMail
import CreateBaseline as hassh
import check_ports_socket
import phonenumbers
from phonenumbers import geocoder

if __name__ == '__main__':

	description = '''Modo de uso:
    Virus total[1]: py main.py -ch 1 -u [URL]
    WebScrap[2]: 	py main.py -ch 2 -u [URL]
	Metadata[3]:	py main.py -ch 3 -target [Path]
	Correo[4]:		py main.py -ch 4 -sender [Mail] -r [Mail] -sub [Subjetct] -m [Message]
	Claves Hash[5]:	py main.py -ch 5 -target [Path] -t [Name]
	Puertos[6]:		py main.py -ch 6 -ports [IP] -target[IP]
	Phone number[7]:py main.py -ch 7 -number [Num]
     '''



	parser = argparse.ArgumentParser()
	
	parser.add_argument('-ch', '--choice', required=True, help="Choose the function you want to do")
	parser.add_argument('-n', '--baseline',help="Specify the resulting baseline file", type=ValidatePath)
	parser.add_argument('-p', '--Path',help="Specify the target folder to baseline")
	parser.add_argument('-t', '--tmp',help="Specify a temporary result file for the PowerShell Script")
	parser.add_argument('-u', '--url', help="Specify the url")
	parser.add_argument('-s', '--sender', help="Specify the sender email")
	parser.add_argument('-r','--receiver', help="Specify the receiver email")
	parser.add_argument('-sub', '--subject', help="Specify the subject")
	parser.add_argument('-m', '--message', help="Specify the message")
	parser.add_argument("-target", metavar='TARGET', dest="target", help="target to scan")
	parser.add_argument("-ports", dest="ports", 
							help="Please, specify the target port(s) separated by comma[80,8080 by default]",
							default = "80,8080")  
	parser.add_argument('-nu', '--number', help='Type your phone number') 
	params = parser.parse_args()
	choice = int(params.choice)
	
	if (choice == 1): # VirustTotal
		api_key = getpass.getpass("Type your VT Api key: ") # Ingresa la api_key
		if not params.url: # Si el usuario no ingreso parametro al inicio del script se lo pedira por input y hace llamado a la funcion
			print ('No url.')
			url = input ('Type the url you want to scan:')
		else: # Si el usuario si ingreso parametro simplemente se le asigna a la variable url y se hace llamado a la funcion
			url = params.url
		try:
			virusT(url, api_key)
		except Exception as e:
			print('One data is incorrect')

	elif (choice == 2): # WebScrap
		if not params.url: # Sino se ingreso el parametro lo pedira por medio de input y hara llamado a las funciones
			url = input ('Type the url:')
		else: # De lo contrario se asignara el prametro a url y se hara llamado a las funciones
			url = params.url
		try:
			scraping = Scraping()
			scraping.scrapingImages(url)
			scraping.scrapingPDF(url)
			scraping.scrapingLinks(url)
			scraping.scrapingBeautifulSoup(url)
		except Exception as e:
			print ('The script could not be executed:', e)

	elif (choice == 3): # Metadata
		if not params.Path:
			targetPath = input ('Type the adress: ')
		else:
			targetPath = params.Path
		try:
			printMeta(targetPath)
		except OSError as e:
			print("Cant access to the adress.")

	elif (choice == 4): # Correo
		if not params.sender:
			user = input('Type sender email: ')
		else:
			user = params.sender

		pwd = getpass.getpass('Type password from sender: ')
	
		if not params.receiver:
			to = input('Type the mail from reciver: ')
		else:
			to = params.receiver
		
		if not params.subject:
			subject = input('Type email subject: ')
		else:
			subject = params.subject
		
		if not params.message:
			message = input('Type the message: ')
		else:
			message = params.message
		sendMail(user, pwd, to, subject, message)
		
	elif (choice == 5): # Claves Hash
		if not params.Path:
			targetPath = input('Type the path for hash the file: ')
		else:
			targetPath = params.Path
		
		if not params.tmp:
			tmpFile = input('Type the name of the file with the hash: ')
		else:
			tmpFile = params.tmpFile
		

		baselineFil = tmpFile
		txt = ".txt"
		for x in range(len(txt)):
			baselineFil = baselineFil.replace(txt[x],"")
		baselineFil = baselineFil + '.init'
		print(baselineFil)
		try:	
			hassh.printHash(baselineFil, targetPath, tmpFile)
		except OSError as e:
			print('Error')

	elif (choice == 6): # Puertos
		portlist = params.ports.split(',')
		for i in range(len(portlist)):
			portlist[i] = int(portlist[i])
		if not params.target:
			target = input('Type the ip you want to scan: ')
		else:
			target = params.target
		check_ports_socket.checkPortsSocket(target,portlist)
	
	elif (choice == 7): # Numero celular
		if not params.number:
			number = input("Type your phone number")
		else:
			number = params.number

		ch_nnmber = phonenumbers.parse(number, "CH")
		try:
			print(geocoder.description_for_number(ch_nnmber, "en"))
		except Exception :
			print('Phone Error')


