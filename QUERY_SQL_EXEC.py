import datetime
import logging
import mysql.connector
import sys

database = mysql.connector.connect(
    host = "localhost",#Host de la BD
    user = "username",#Nombre de quién se esta loggeando en la BD
    password = "password",#Contraseña para el acceso a la BD
    database = "database_name"#Nombre de la BD
)
#Loggeo en la Base de Datos
dbcursor = database.cursor()
#Cursores para indicar la BD
def select_in_db():
    dbcursor.execute("SELECT * FROM database_name WHERE column1 LIKE 'pattern_to_search_for' AND column2='" + sys.argv[1] + "';") #Busca según el argumento que tu le des en la ejecución.
    result = dbcursor.fetchall()
    for row in result:
        if result is None:
            return None
        else:
            return(row)
#Definición del loop de la BD. Primero el cursor es ejecutado con los parametros dentro del parentesis (siendo ftplog la tabla y 226 lo que debe buscar)
#Luego los recoge en result y finalmente lo devuelve, tanto en caso de que haya algo como en el caso de que no.
select_in_db()
dt = datetime.datetime.now()
#Variable del tiempo
exec_time = dt.strftime("%d/%m/%Y %H:%M")
#Variable del tiempo de ejecución
logging.basicConfig(filename="log.txt", level=logging.ERROR)
#Generación del log
logerror_msg = select_in_db()
#Mensaje en log

if select_in_db() is None:
    print ("Error.")
else:
    logging.error(logerror_msg)
#Ejecución del script. Si select_in_db esta vacio, ignorara y pasará. En caso de que haya algo, se mostrará y se guardará en el log.
