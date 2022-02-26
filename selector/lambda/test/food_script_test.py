import unittest
import food_script_lambda

data = [
    {
        "name": "Best Friends Cafe",
        "choices": [
            {
                "person": "Orange Cassidy",
                "likes": [
                    "orange punch"
                ]
            },
            {
                "person": "Kris Statlander",
                "likes": [
                    "popcorn"
                ]
            }
        ]
    }
]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        response = food_script_lambda.choose_food(data)
        print(response)


if __name__ == '__main__':
    unittest.main()
