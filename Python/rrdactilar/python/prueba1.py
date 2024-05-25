import pydigitalpersona as dp

# Inicializar el dispositivo
device = dp.UareU()

# Capturar la huella dactilar
fingerprint = device.capture()

# Verificar la huella dactilar
result = device.verify(fingerprint)

if result:
    print("Huella dactilar verificada con éxito")
else:
    print("La verificación de la huella dactilar falló")