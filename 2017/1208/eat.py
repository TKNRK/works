import numpy as np


class Human:
  def __init__(self, pantry):
    self.satiety = 0
    self.pantry = pantry

  def eat(self):
    for food in self.pantry:
      self.satiety += food

  def checkSatiety(self):
    print("Satiety: "+str(self.satiety)+" / "+str(len(self.pantry)))


def fillPantry(N):
  return np.random.randint(0, 3, N)

def main():
  pantry = fillPantry(10000)
  human = Human(pantry)
  human.eat()
  human.checkSatiety()


if __name__ == '__main__':
  main()
