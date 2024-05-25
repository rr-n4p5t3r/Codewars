#!/usr/bin/python3

import os
import sys
import gi
import matplotlib.pyplot as plt
import numpy as np

# Directorios relevantes para acceder a la biblioteca
BUILDDIR='/home/pi/Desktop/INCICH/libfprint/bin'
LIBRARYPATH = BUILDDIR + '/libfprint/'
TYPELIBPATH = BUILDDIR + '/libfprint/'

# Truco para ejecutar el programa con las variables de entorno correctas
if 'RUNNING' not in os.environ:
	if 'LD_LIBRARY_PATH' not in os.environ:
		os.environ['LD_LIBRARY_PATH'] = LIBRARYPATH
	else:
		os.environ['LD_LIBRARY_PATH'] += ':' + LIBRARYPATH
	os.environ['GI_TYPELIB_PATH'] = TYPELIBPATH
	os.environ['FP_DEVICE_EMULATION'] = '1'
	os.environ['RUNNING'] = 'True'
	# Aquí el relanzamiento del programa
	os.execv(sys.argv[0], sys.argv)

# Levanta la interfaz GObject para la biblioteca libfprint
gi.require_version('FPrint', '2.0')
from gi.repository import FPrint

# Crea el contexto de la biblioteca y escanea por sensores
context = FPrint.Context()
context.enumerate()
devices = context.get_devices()

# Debe haber un solo sensor para este programa
if len(devices) > 1:
	raise ValueError('solo un dispositivo puede estar conectado')
if len(devices) == 0:
	raise ValueError('no hay dispositivo conectado')

# Recupera el sensor	
device = devices[0]

# Pruebas de capacidades del sensor
#assert device.has_feature(FPrint.DeviceFeature.CAPTURE)
#assert device.has_feature(FPrint.DeviceFeature.IDENTIFY)
#assert device.has_feature(FPrint.DeviceFeature.VERIFY)
#assert not device.has_feature(FPrint.DeviceFeature.DUPLICATES_CHECK)
#assert not device.has_feature(FPrint.DeviceFeature.STORAGE)
#assert not device.has_feature(FPrint.DeviceFeature.STORAGE_LIST)
#assert not device.has_feature(FPrint.DeviceFeature.STORAGE_DELETE)
#assert not device.has_feature(FPrint.DeviceFeature.STORAGE_CLEAR)

print(f'Número de pasos de enrollment: {device.get_nr_enroll_stages()}')
features = device.get_features()
print('Capacidades: ')
for feature in device.get_features().value_names:
	print(feature)
#print(device.enroll_sync())

# Lista para almacenar huellas
fingerprints = []

# # Captura n huellas
n = 5
for i in range(n):
	# Lanza la captura sincrónica (blocking) de una huella
	device.open_sync()
	print(f'Coloca tu dedo en el sensor ({i+1}/{n}) ...')
	capture = device.capture_sync(True)
	device.close_sync()
    # Recupera las dimensiones de la imagen
	width = capture.get_width()
	height = capture.get_height()
	# Crea un np.array con la imagen (8bpp)
	img = np.frombuffer(capture.get_data(), dtype=np.dtype('uint8'))
	img = img.reshape(height, width)
	# Almacena en la lista
	fingerprints.append(img)

# Despliega las huellas
fig, ax = plt.subplots(1, n, figsize=(16, 5), sharey=True)
for i in range(n):
	ax[i].imshow(fingerprints[i], cmap='gray')
	ax[i].axis('off')
fig.tight_layout()
plt.show()

# Cierra el dispositivo y el contexto de la biblioteca
del device
del context