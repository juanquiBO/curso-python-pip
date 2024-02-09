import sys
print(sys.path)

import time
timestamp = time.time()
print(timestamp)
loction = time.localtime()
result = time.asctime(loction)
print(result)
print("Pruebas")