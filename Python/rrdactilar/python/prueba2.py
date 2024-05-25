import pydigitalpersona as dp

# Inicializar el dispositivo
device = dp.UareU()

def register_user(username):
    # Capturar la huella dactilar
    fingerprint = device.capture()
    
    # Registrar al usuario con su huella dactilar
    device.register(username, fingerprint)
    
    print(f"Usuario {username} registrado con éxito")

# Capturar y verificar la huella dactilar
fingerprint = device.capture()
result = device.verify(fingerprint)

if result:
    print("Huella dactilar verificada con éxito")
else:
    print("La verificación de la huella dactilar falló")