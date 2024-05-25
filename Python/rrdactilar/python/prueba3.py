import ctypes

# Cargar la DLL de Digital Persona
dpfpddDll = ctypes.CDLL("./dpfpdd.dll")

# Inicializar la biblioteca
dpfpdd_init = dpfpddDll.dpfpdd_init
dpfpdd_init.restype = ctypes.c_int
result = dpfpdd_init()

# Abrir el dispositivo DigitalPersona 4500
device_name = "EB31330E-43BD-424F-B7FB-D454CCF90155"
dpfpdd_open = dpfpddDll.dpfpdd_open
dpfpdd_open.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_void_p)]
dpfpdd_open.restype = ctypes.c_int

device_handle = ctypes.c_void_p()
result = dpfpdd_open(device_name.encode('utf-8'), ctypes.byref(device_handle))