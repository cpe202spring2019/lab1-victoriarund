import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
    	#checks if the print method works correctly
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc = Location("LA", 235.46, 2342.7)
        self.assertEqual(repr(loc),"Location('LA', 235.46, 2342.7)")
        loc2 = Location("SFO", -12.46, 0.7)
        self.assertEqual(repr(loc2),"Location('SFO', -12.46, 0.7)")
    def test_init(self):
    	#check if name, lat, and lon are assigned to object correctly
        loc=Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name,'SLO')
        self.assertEqual(loc.lat,35.3)
        self.assertEqual(loc.lon,-120.7)
        loc2 = Location("LA", 235.46, 2342.7)
        self.assertEqual(loc2.name,'LA')
        self.assertEqual(loc2.lat,235.46)
        self.assertEqual(loc2.lon,2342.7)
        loc2 = Location("SFO", -12.46, 0.7)
        self.assertEqual(loc2.name,'SFO')
        self.assertEqual(loc2.lat,-12.46)
        self.assertEqual(loc2.lon,0.7)
    def test_eq(self):
    	#check if equal when two objects have same values
        loc=Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc,loc2)
        loc = Location("LA", 235.46, 2342.7)
        loc2 = Location("LA", 235.46, 2342.7)
        self.assertEqual(loc,loc2)
        loc = Location("SFO", -12.46, 0.7)
        loc2 = Location("SFO", -12.46, 0.7)
        self.assertEqual(loc,loc2)
        #check if not equal when one part of location attribute changed
        loc=Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 36.3, -120.7)
        self.assertNotEqual(loc,loc2)
        loc=Location("SL", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc,loc2)
        loc=Location("SLO", 35.3, 120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc,loc2)
        #check if equal when alliasing
        loc=Location("SLO", 35.3, -120.7)
        loc2=loc
        self.assertEqual(loc,loc2)
        #check not equal when they arent the same type
        loc=Location("SLO", 35.3, -120.7)
        loc2 =("SLO", 35.3, -120.7)
        self.assertNotEqual(loc,loc2)
        loc = Location("SFO", -12.46, 0.7)
        loc2 = ("SFO", -12.46, 0.7)
        self.assertNotEqual(loc,loc2)
        loc = Location("LA", 235.46, 2342.7)
        loc2 = ("LA", 235.46, 2342.7)
        self.assertNotEqual(loc,loc2)


if __name__ == "__main__":
    unittest.main()
