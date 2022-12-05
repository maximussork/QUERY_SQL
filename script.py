import datetime
import logging

arg0 = "> put"
arg1 = "Successfully"
dt = datetime.datetime.now()
exec_time = dt.strftime("%d/%m/%Y %H:%M")
logging.basicConfig(filename="log.txt", level=logging.ERROR)
logerror_msg = "Execution time: " + exec_time + " - Error en SalidaFTP.txt. Por favor vuelva a intentarlo."

with open('SalidaFTP.txt') as file:
    ftp = file.read()
    if arg0 in ftp and arg1 in ftp:
        print('Congrats.')
        print ("Execution time: " + exec_time)
    else:
        print ("Try again!")
        logging.error(logerror_msg)