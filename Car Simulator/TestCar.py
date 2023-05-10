import unittest
from unittest.mock import patch
from io import StringIO
from car import Car

class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_turnCarLeft(self):
        self.car.heading = "North"
        self.car.turnCarLeft()
        self.assertEqual(self.car.heading, "East")
        self.car.heading = "South"
        self.car.turnCarLeft()
        self.assertEqual(self.car.heading, "West")
        self.car.heading = "East"
        self.car.turnCarLeft()
        self.assertEqual(self.car.heading, "South")
        self.car.heading = "West"
        self.car.turnCarLeft()
        self.assertEqual(self.car.heading, "North")

    def test_turnCarRight(self):
        self.car.heading = "North"
        self.car.turnCarRight()
        self.assertEqual(self.car.heading, "West")
        self.car.heading = "South"
        self.car.turnCarRight()
        self.assertEqual(self.car.heading, "East")
        self.car.heading = "East"
        self.car.turnCarRight()
        self.assertEqual(self.car.heading, "North")
        self.car.heading = "West"
        self.car.turnCarRight()
        self.assertEqual(self.car.heading, "South")

    def test_travelDirection_left(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.car.travelDirection('left')
            self.assertIn("The Driver turned and drived left", fake_out.getvalue())

    def test_travelDirection_right(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.car.travelDirection('right')
            self.assertIn("The Driver turned and drived right", fake_out.getvalue())

    def test_travelDirection_forward(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.car.travelDirection('forward')
            self.assertIn("The Driver Drove Forwards", fake_out.getvalue())

    def test_travelDirection_backward(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.car.travelDirection('backward')
            self.assertIn("The Driver Reversed", fake_out.getvalue())

    def test_testGas_with_gas(self):
        self.car.gas = 1
        self.assertTrue(self.car.testGas())
        self.assertEqual(self.car.gas, 0)

    def test_testGas_without_gas(self):
        self.car.gas = 0
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(self.car.testGas())
            self.assertIn("YOU ARE OUT OF GAS", fake_out.getvalue())

    def test_testTiredness(self):
        self.car.tired = 9
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.car.testTiredness()
            self.assertIn("\n\nYou ARE BEGINNING TO MAX OUT YOUR TIREDNESS\n\n", fake_out.getvalue())
        self.assertEqual(self.car.tired, 10)

    def test_rest(self):
        self.car.tired = 5
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.car.rest()
            self.assertIn("You have rested yourself", fake_out.getvalue())
        self.assertEqual(self.car.tired, 0)

    def test_refill(self):
        self.car.gas = 5
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.car.refill()
            self.assertIn("Gas has been refilled", fake_out.getvalue())
        self.assertEqual(self.car.gas, 20)

if __name__ == '__main__':
    unittest.main()
