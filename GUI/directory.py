def getDirectory():
    import os
    ruta = os.getcwd()
    rutaArray = ruta.split("\\")
    rutaArrayCount = len(rutaArray)
    if rutaArray[rutaArrayCount-1] == "GUI":
        ruta+="\icon.ico"
    if rutaArray[rutaArrayCount-1] == "excel_to_sql":
        ruta+="\GUI\icon.ico"
    return ruta