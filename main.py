import os
cant = raw_input('Cuantas personas desea registrar? ')
cant = int(cant)
while(cant > 0):
    os.system('/usr/bin/python modules/dataSetGenerator.py')
    cant = cant - 1

os.system('/usr/bin/python modules/trainer.py')

os.system('/usr/bin/python modules/recognizer.py')