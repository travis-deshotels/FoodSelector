import fileinput
import json
import os.path
import unittest
from csvconverter import process_csv_data


class MyTestCase(unittest.TestCase):
    expected_output = [
        {
            "name": "Applebees",
            "choices": [
                {
                    "person": "Bob",
                    "likes": [
                        "apples",
                        "bees"
                    ]
                },
                {
                    "person": "Jill",
                    "likes": [
                        "sandwich",
                        "fries"
                    ]
                }
            ]
        },
        {
            "name": "Wendy's",
            "choices": [
                {
                    "person": "Bob",
                    "likes": [
                        "baconator",
                        "spicy chicken",
                        "chili"
                    ]
                },
                {
                    "person": "Jill",
                    "likes": [
                        "baconator",
                        "salad"
                    ]
                }
            ]
        }
    ]

    test_data = \
        "Applebees,,,\n" + \
        "Bob,apples,bees,\n" + \
        "Jill,sandwich,fries,\n" + \
        ",,,\n" + \
        "Wendy's,,,\n" + \
        "Bob,baconator,spicy chicken,chili\n" + \
        "Jill,baconator,salad,\n"

    def test_process_csv(self):
        f = open('foo', 'w')
        f.write(self.test_data)
        f.close()
        out = process_csv_data(fileinput.input('foo'))
        self.assertEqual(json.dumps(self.expected_output), out)
        if os.path.exists('foo'):
            os.remove('foo')


if __name__ == '__main__':
    unittest.main()
