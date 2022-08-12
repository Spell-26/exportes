from sqlalchemy import create_engine
import pandas as pd

# datos de conexión a la base de datos TODO: hacer que cambie la tabla target cuando se seleccione un futuro checkbox
db = "exceltosql"
table = "usuarios"
#archivo target de excel, TODO: en el futuro hacer que el target sea desde la interfac grafica
path = "C:\\Users\\James\\Desktop\\reporte.xlsx"
url = "mysql+mysqlconnector://root:Gatonegro1+@localhost/"
#ejecuta conexion a la base de datos
engine = create_engine(url + db, echo = False)
#lee el archivo excel almacenado en la base de excel
df = pd.read_excel(path)
#mensaje de confirmacion cuando termina la lectura
print("read ok")
#añade los campos a la base de datos, si ya existe en la base de datos lo suma
df.to_sql(name = table, con = engine, if_exists='append', index = False)