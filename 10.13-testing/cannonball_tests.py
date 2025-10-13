import unittest
import cannonball


class TestCannonball(unittest.TestCase):
    # NOTE: We should always write tests before writing code, since tests give
    #       us an objective measure of progress: as we implement a function, we
    #       ought to pass more and more tests. However, for any non-trivial
    #       problem, no finite number of tests can ever be enough tests.
    def test01_time_of_flight(self):
        time = cannonball.time_of_flight(50)
        self.assertAlmostEqual(time, 3.1927543)

    def test02_time_of_flight(self):
        time = cannonball.time_of_flight(0)
        self.assertAlmostEqual(time, 0)

    # NOTE: Here, we have only tested one function -- we cannot have any
    #       confidence in the correctness of any of the other functions. In
    #       particular, any time we find a bug, we should write a unit test
    #       illustrating that bug before fixing it.
    def test03_is_hit(self):
        was_hit = cannonball.is_hit(10, 5, 1)
        self.assertFalse(was_hit)


if __name__ == "__main__":
    unittest.main()
