from time import sleep

class car:
    def __init__(self,age, mpg, running):
        self.age = age
        self.mpg = mpg
        self.running = running

    def fillUp(self):
        x=0
        while x < 4:
            print("Filling up...")
            sleep(0.5)
            x = x+1
        print("The car has filled up and you will have aaround "+str(self.mpg)+" miles per gallon when youd drive")

car = car(12,35,False)
