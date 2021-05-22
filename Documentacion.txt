Documentacion del programa
Pia ciberseguridad
Tareas de ciber seguridad
22/may/2021

Funcionamiento:
El script principal consiste de 7 funciones las cuales son el escaneo de paginas web mediante la API
de virus total, el webscrapping para obtencion de imagenes y pdfs, la obtencion de metadata, envio de correos, obtencion de claves hash,
escaneo de puertos y obtencion de ubicacion de un numero telefonico.
Estas son las funciones que pueden ser llamadas de los multiples scripts escritos como:
-HashAcquire.ps1
-main.py
-Scraping.py
-sendEmail.py
-Virus.py
-check_ports_socjets.py
-createBaseline.py
-extractDataFromImages.py

"Virus total[1]: py main.py -ch 1 -u [URL]"
Funcionamiento:
Todo esto va por opciones y argparse, para la opcion 1 tenemos virustotal, la api revisa si la url para esto se necesita una
clave que se genera al crear nuestra cuenta y debera ser escrita en el script para saber si tiene alertas de seguridad y nos genera
un archivo de texto.

"WebScrap[2]: 	py main.py -ch 2 -u [URL]"
Esta funcion toma los archivos pdf y las imagenes de una pagina y se almacenan en una direccion la cual puede ser determinada
mediante escritura cuando el programa este corriendo.

"Metadata[3]:	py main.py -ch 3 -target [Path]"
Para metadata podemos escanear una carpeta que determinemos nosotros donde se escanearan todas las imagenes y se nos mostraran los datos como
la ubicacion si es que esta disponible, el modelo con el que fue tomada entre otras cosas.

"Correo[4]:		py main.py -ch 4 -sender [Mail] -r [Mail] -sub [Subjetct] -m [Message]"
Con esta funcion podremos enviar correos con mensajes a otras personas o enviarlos a nuestro correo si es que lo necesitamos
todo se puede hacer de manera simple con los comandos que se muestran arriba seguido de la informacion nescesaria.

"Claves Hash[5]:	py main.py -ch 5 -target [Path] -t [Name]"
Aqui podemos cifrar con hash un archivo donde hay que determinar donde esta el archivo y dar un nombre al archivo que generara el 
script de powershell para que sean almacenadas las claves

"Puertos[6]:		py main.py -ch 6 -ports [IP] -target[IP]"
Se ingresa la ip que se quiere analizar y ademas se revisan los puertos seleccionados para luego crear un archivo en el cual se
almacenara toda la informacion de la ip y sus puertos

"Phone number[7]:py main.py -ch 7 -number [Num]"
La funcion de numero celular nos permite saber la ubicacion de un numero celular ingresado mediante el modulo geo y el reconocimiento de numero
pero es necesario la entrada de la extension.