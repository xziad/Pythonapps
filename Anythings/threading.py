import threading


class ZiyadMassenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())


sender = ZiyadMassenger(name="Send out message")
receiver = ZiyadMassenger(name="Receive message")
sender.start()
receiver.start()
