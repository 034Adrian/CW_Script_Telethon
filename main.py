from distutils.log import error
from NombreAlt import client1, loop1


altNumeroUno = True
altNumerodos = False
altNumerotres = False

if __name__ == '__main__':
    try:
        if altNumeroUno:
            client1.satart()   
            loop1.run_forever()
    except error:
        print('Huvo un error pero todavia no se como manejarlo') 