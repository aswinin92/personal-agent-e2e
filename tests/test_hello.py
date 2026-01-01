import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from hello import greet  # noqa: E402


class GreetTest(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_named(self):
        self.assertEqual(greet("agent"), "Hello, agent!")


if __name__ == "__main__":
    unittest.main()
