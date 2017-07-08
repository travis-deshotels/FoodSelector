#Copyright 2017 Travis Deshotels

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software
#and associated documentation files (the "Software"), to deal in the Software without restriction,
#including without limitation the rights to use, copy, modify, merge, publish, distribute, 
#sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or 
#substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
#NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
#DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import json, sys
from random import randint

def chooseFood():
  #choose a restaurant
  x = randint(0,len(data)-1)
  restaurant = data[x]
  choices = restaurant['choices']

  #print random restaurant's name
  print (restaurant['name'])

  for person in choices:
    print(person['person'])
    likesCount = len(person['likes'])
    choice = randint(0, likesCount-1)
    print(person['likes'][choice])

try:
  if len(sys.argv) == 1:
    print("Please supply a filename")
    sys.exit(1)
  data = json.loads(open(sys.argv[1]).read())
  chooseFood()
except FileNotFoundError:
  print("Invalid filename")
  sys.exit(1)
except json.decoder.JSONDecodeError:
  print("Invalid JSON object")
sys.exit(0)
