import unittest
import add_food

data = {
  'name': 'Orange Cassidy',
  'restaurant': 'Best Friends Cafe',
  'choices': 'orange punch'
}


class MyTestCase(unittest.TestCase):
    def test_upload_fail(self):
        response = add_food.main(data, None)
        self.assertNotEqual(response.get('Error'), None)


if __name__ == '__main__':
    unittest.main()
