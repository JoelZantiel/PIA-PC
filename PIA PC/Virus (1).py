import requests
import json
import argparse
import getpass



def virusT(page, api_key):
    virusto = "https://www.virustotal.com/vtapi/v2/url/report"

    params = {"apikey": api_key, "resource": page}
    response = requests.get(virusto, params = params)
    response_json = json.loads(response.content)

    ### Lo que sucede en los siguientes condicionales es que en el diccionario
    ### response_json contiene una etiqueta llamada positives en la que muestra en
    ### cuantos antivirus dio positivo la pagina web
        
    if response_json["positives"]<= 0:
        with open("result.txt", "a") as vr:
            vr.write(page) and vr.write(" -\tnot dangerous\n")
            print('File with results created')
    elif response_json["positives"] >=1:
        with open("results.txt", "a") as vr:
            vr.write(page) and da.write(" -\tWarning dangerous\n")
            print('File created')

    else:
        print("url not found")

 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help="Specify the url")
    params = parser.parse_args()
    url = params.url
    
    api_key = getpass.getpass("Type your apikey from Virus Total: ")
    virusT(url, api_key)
