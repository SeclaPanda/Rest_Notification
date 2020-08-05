import time
from plyer import notification

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        timeout = 15
    )

while True:
    notifyMe('Time to Rest!', 'You need to timeout for good health! Enjoy it)')
    time.sleep(2700)