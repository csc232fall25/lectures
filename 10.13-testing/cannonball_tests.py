import unittest
import cannonball


class TestCannonball(unittest.TestCase):
    def test01_time_of_flight(self):
        time = cannonball.time_of_flight(50)
        self.assertAlmostEqual(time, 3.1927543)

    def test02_time_of_flight(self):
        time = cannonball.time_of_flight(0)
        self.assertAlmostEqual(time, 0)


if __name__ == "__main__":
    unittest.main()
