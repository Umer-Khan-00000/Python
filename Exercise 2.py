# Time Importing Solution :

import time
timestamp = time.strftime('%I:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

# Another Example Of Importing Time :

from datetime import *
current_time = datetime.now().strftime("%I:%M:%S %p")
print(current_time)


