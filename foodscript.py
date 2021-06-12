import json
import sys
import random


def choose_food():
    restaurant = random.choice(data)
    print(restaurant['name'])
    for person in restaurant['choices']:
        print(f"{person['person']}: {random.choice(person['likes'])}")


try:
    if len(sys.argv) == 1:
        print("Please supply a filename")
        sys.exit(1)
    data = json.loads(open(sys.argv[1]).read())
    choose_food()
except FileNotFoundError:
    print("Invalid filename")
    sys.exit(1)
except json.decoder.JSONDecodeError:
    print("Invalid JSON object")
sys.exit(0)
