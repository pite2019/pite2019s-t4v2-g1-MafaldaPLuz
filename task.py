import time
from random import gauss
import logging 

class Plane:
    def __init__(self):
        self.angle = gauss(0,7)
        self.correction = 0  
        
    def ajust(self, how_much):
        self.correction = how_much
        if(self.angle-how_much < 0):
            self.angle += how_much
        else:
            self.angle -= how_much


class Environment:
    def __init__(self, plane):
        self.plane= plane
        
    def flight(self):
        degree = gauss(0, 3)
        disturbance = degree
        self.plane.angle += disturbance
        self.plane.ajust(degree*0.75)
        logging.info('The disturbance is ' + str(disturbance))
                    

def main():
    logging.basicConfig(filename = 'task.log',level = logging.DEBUG)
    plane = Plane()
    environment = Environment(plane)
    zero = False
    
    while(not zero):
        if(abs(plane.angle)==0):
            zero = True
            logging.info('The plane is stable')
            
        else:
            environment.flight()
            logging.info('The angle of the plane is ' + str(plane.angle))
            time.sleep(2)    
        

if __name__== '__main__':
	main()
		
