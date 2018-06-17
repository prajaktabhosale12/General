# -*- coding: utf-8 -*-
"""
Created on Thu May 18 12:09:06 2017

@author: prjkt

"""

import math
import random
from operator import itemgetter
from abc import ABC, abstractmethod      
    
class Vector(object):
    """
    This class defines a vector in 2d and vector operations
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    def get_distance(self, other):
        '''
        returns distance between two positions
        '''
        return self.magnitude(other.x - self.x, other.y - self.y)
        
    def magnitude(self, x, y):
        '''
        returns distance between two positions
        '''
        return math.sqrt(x**2 + y**2)
    
    def is_inside(self, w, h):
        '''
        return True if the vector coordinates lie within given dimensions
        '''
        return (self.x > 0 and self.x < w and 
                self.y > 0 and self.y < h )
    

        
class Particle(object):
    """
    Particle with a position in 2-dimensions, which has its own speed and velocity 
    """
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.speed = vel.magnitude(vel.x, vel.y)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed > 1: 
            raise Exception("Intitial speed should be less than 1") 
        self._speed = speed
     
     
    def move(self):
        '''
        moves particle position by its velocity components 
        '''
        self.pos.x = self.pos.x + self.vel.x
        self.pos.y = self.pos.y + self.vel.y
     

class Deflector(ABC):
    '''
    Abstract Deflector class, is super class for different types of Deflectors
    '''   
    def __init__(self, pos, activation_range=0):
        self.pos = pos
        self.activation_range = activation_range
    
    @abstractmethod
    def act_on(self, particle):
        '''
        Deflector takes some action on a particle.
        '''
        pass
        
        
class LeftDeflector(Deflector):
    """
    Deflector causing left deflection
    """
    def __init__(self, pos, activation_range=1):
        Deflector.__init__(self, pos, activation_range)
    
    def act_on(self, particle):
        """
        Left deflector deflects the direction of the particle to left by changing its velocity,
        if within activation range
        """
        within_activation_range = self.pos.get_distance(particle.pos) <= self.activation_range        
        if within_activation_range:
            particle.vel.x = -particle.speed
            particle.vel.y = 0
        
        
class RightDeflector(Deflector):
    """
    Deflector causing right deflection
    """
    
    def __init__(self, pos):
        Deflector.__init__(self, pos, activation_range=2)
    
    def act_on(self, particle):
        """
        Right deflector deflects the direction of the particle to right by changing its velocity,
        if within activation range
        """
        within_activation_range = self.pos.get_distance(particle.pos) <= self.activation_range        
        if within_activation_range:
            particle.vel.x = particle.speed
            particle.vel.y = 0
        
        
class UpDeflector(Deflector):
    """
    Deflector causing upward deflection
    """
    
    def __init__(self, pos):
        Deflector.__init__(self, pos, activation_range=3)
    
    def act_on(self, particle):
        """
        Up deflector deflects the direction of the particle upwards by changing its velocity,
        if within activation range
        """
        within_activation_range = self.pos.get_distance(particle.pos) <= self.activation_range        
        if within_activation_range:
            particle.vel.x = 0
            particle.vel.y = particle.speed


class DownDeflector(Deflector):
    """
    Deflector causing downward deflection
    """
    def __init__(self, pos):
        Deflector.__init__(self, pos, activation_range=4)
    
    def act_on(self, particle):
        """
        Down deflector deflects the direction of the particle downwards by changing its velocity,
        if within activation range
        """
        within_activation_range = self.pos.get_distance(particle.pos) <= self.activation_range        
        if within_activation_range:
            particle.vel.x = 0
            particle.vel.y = -particle.speed


class ReverseDeflector(Deflector):
    """
    Deflector causing reverese deflection
    """
    def __init__(self, pos, activation_range=5):
        Deflector.__init__(self, pos, activation_range)
    
    def act_on(self, particle):
        """
        Reverese deflector revereses the direction of the particle by changing its velocity,
        if within activation range
        """
        within_activation_range = self.pos.get_distance(particle.pos) <= self.activation_range        
        if within_activation_range:
            particle.vel.x = -particle.vel.x
            particle.vel.y = -particle.vel.y
        
        
class DeflectorList(object):
    """
    Maintains a collection of Deflectors
    """
    def __init__(self, deflectors):
        self.deflectors = deflectors

    @classmethod
    def random_state(cls, n, width, height):
         '''
         class level method that generates a Deflectorlist object with random unique deflectors
         '''
         i = 0
         deflectors = dict()
         deflector_subclasses = [cls for cls in Deflector.__subclasses__()]
         while i < n:
             x = random.uniform(0, width - 1)
             y = random.uniform(0, height - 1)
             try:
                 if (x, y) not in deflectors:
                     deflectors[(x, y)] = random.choice(deflector_subclasses)(Vector(x, y))
                     i = i + 1
             except:
                 pass
    
         return cls(list(deflectors.values()))
   
    def nearest_if_present(self, pos):
        '''
        returns nearest deflector to the given position 
        '''
        if not self.deflectors:
            return None
        
        nearest_deflector = min([[d, pos.get_distance(d.pos)] for d in self.deflectors], key=itemgetter(1))[0]

        return nearest_deflector


class Timer(object):
    """
    This class keeps track of time/epochs 
    """
    
    def __init__(self, threshold):
        self.time = 0
        self.threshold = threshold
    
    @property
    def time_out(self):
        #returns True when time crosses given threshold
        return self.time > self.threshold
    
    def tick(self):
        """
        tick time, in increments of single epoch
        """
        self.time = self.time + 1

          
class Observable(object):
    '''
    notifies all the observers for any change in the observable
    '''
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """
        attach all the given observers to the observable
        """
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        detach given observer from the observable
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify_observers(self):
        """
        notify all obervers when observable changes its state
        """
        for observer in self._observers:
            observer.notify(self)

class Universe(Observable):
    '''
    2d universe of finite width and height, universe lies in the positive quadrant
    all positions in the universe are positive
    '''
    def __init__(self, w, h, particle, deflectors, threshold=10000):
        Observable.__init__(self)
        self.width = w
        self.height = h
        self.particle = particle
        self.deflector_list = deflectors
        self.timer = Timer(threshold)
        self.attach(Observer())
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, w):
        if w <= 0 :
            raise Exception("Width of the universe should be finite")
        self._width = w
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, h):
        if h <= 0 :
            raise Exception("Height of the universe should be finite")
        self._height = h
        
    @property
    def particle(self):
        return self._particle
    
    @particle.setter
    def particle(self, p):
        if not self.contains(p):
            raise Exception("Particle position should lie within the bounds of the universe")
        self._particle = p      
    
    @property 
    def deflector_list(self):
        return self._deflector_list
    
    @deflector_list.setter
    def deflector_list(self, deflector_list):
        for d in deflector_list.deflectors:
            if not self.contains(d):    
                raise Exception(" Deflector position should lie within bounds of universe")
                    
        self._deflector_list = deflector_list

    @classmethod
    def random_state(cls):
         '''
         class level method that returns randomly generated universe object
         '''
         width = random.uniform(10, 100)
         height = random.uniform(10, 100)
         x = random.uniform(0, width - 1)
         y = random.uniform(0, height - 1)
         pos = Vector(x, y)
         vx = random.uniform(0, 1)
         vy = random.uniform(0, 1)
         vel = Vector(vx, vy)
         particle = Particle(pos, vel)         
         deflectors = DeflectorList.random_state(20, width, height)
         return cls(width, height, particle, deflectors)
    
    def contains(self, obj):
        """
        returns True if universe contains the given object within its bounds
        """
        return obj.pos.is_inside(self.width - 1, self.height - 1)
        
        
    def run(self):
        '''
        runs the simualation
        '''
        particle = self.particle         # The particle whose movement we are simulating
        timer = self.timer               # Counts epochs
        deflectors = self.deflector_list # Contains all deflectors and knows how to find the nearest one to the particle.   
        
        while (self.contains(particle) and not timer.time_out):
            timer.tick()
            
            deflector = deflectors.nearest_if_present(particle.pos)
            if deflector:
                deflector.act_on(particle)
                
            particle.move()
                            
        self.notify_observers()


class Observer(object):
    '''
    observer of the Universe
    '''
    def notify(self, observer):
        '''
        displays number of epochs elapsed when particle hits the boundary of universe or
        when there is a time out
        '''
        if observer.timer.time_out:
            print("TIME OUT...")
        else:
            print("TIME:",observer.timer.time)

            
            
          
# 