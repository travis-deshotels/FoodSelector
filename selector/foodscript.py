import json
import sys
import random


def choose_food(food_data):
    restaurant = random.choice(food_data)
    print(restaurant['name'])
    for person in restaurant['choices']:
        print(f"{person['person']}: {random.choice(person['likes'])}")


try:
    if len(sys.argv) == 1:
        print("Please supply a filename")
        sys.exit(1)
    data = json.loads(open(sys.argv[1]).read())
    choose_food(data)
except FileNotFoundError:
    print("Invalid filename")
    sys.exit(1)
except json.decoder.JSONDecodeError:
    print("File is invalid JSON. Assuming YAML format.")
    import yaml
    with open(sys.argv[1], 'r') as stream:
        data = yaml.safe_load(stream)
    choose_food(data)
sys.exit(0)
