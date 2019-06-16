from random import  randint
from time import sleep

def user_guess():
  guess = int(raw_input('input guess user: '))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  third_roll = randint(1, number_of_sides)
  fouth_roll = randint(1, number_of_sides)
  maximum_value = number_of_sides * 4
  print 'maximum value available is %d' % maximum_value
  guess = user_guess()
  """here we difine maxmum_value valiable and sety it equal to number of sides times 4 because
we we use four sides in this project and also we use randint to random number which is between
1 and number of sides"""
  #total_roll = first_roll + second_roll + third_roll + fouth_roll
  if guess > maximum_value:
    print ' %d is too large campared to maximum value' % guess
  else:
    print 'rolling ......'
    sleep(3)
    print ' the first dice is %d' % first_roll
    sleep(1)
    print 'the second dice is %d' % second_roll
    sleep(1)
    
    print 'the third dice is %d ' % third_roll
    sleep(1)
    print ' the fouth dice is %d' % fouth_roll
    sleep(1)
    total_roll = first_roll + second_roll + third_roll + fouth_roll
    print ' the total of dice is %d' % total_roll
    print 'result ...'
    sleep(1)
    if guess > total_roll:
      print "hey! you won the game"
    else:
      print 'sorry, you lose the game'

roll_dice(6)
    
  
