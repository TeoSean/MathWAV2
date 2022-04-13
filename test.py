import pyfirmata, time

class Verifier:
    def __init__(self, port):
        self.board=pyfirmata.Arduino(port)
        self.iterator=pyfirmata.util.Iterator(self.board)
        self.iterator.start()
        time.sleep(1)
        self.pin1=self.board.get_pin('d:2:i')
        self.pin2=self.board.get_pin('d:3:i')
        time.sleep(1)
        print('ready')
    def check(self):
        running=True
        winner=0
        while True:
            print((self.pin1.read(), self.pin2.read()))
            if self.pin2.read() == True:
                winner=2
                break
            elif self.pin1.read() == True:
                winner=1
                break
            time.sleep(0.1)
        return winner

vf=Verifier('COM3')

print(vf.check())
