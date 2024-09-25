import unittest
from app import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, Jenkins Pipeline!")

if __name__ == "__main__":
    unittest.main()
