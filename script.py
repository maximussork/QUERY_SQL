from datetime import datetime
tiempo = 


with open(r'SalidaFTP.txt', 'r') as file:
    content = file.read()
    if '> put' in content:
        print('Si')
        print tiempo
    else:
        print('No')