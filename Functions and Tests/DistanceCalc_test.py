'''
    Test class for testing all possible aknowledged errors and instabilities of DistanceCalc.py
    
    Author: Mateo Battilana.
    Created: 16/03/2022
    Modified: 17/03/2020
'''

import unittest
import DistanceCalc

class TestDistanceCalc(unittest.TestCase):
    def test_result(self):
        # Checking correct values
        lat1 = 48.875303
        lat2 = 49.27595
        lon1 = 2.373335
        lon2 = 3.196064
        self.assertLessEqual(DistanceCalc.dist_calc(1, 1, -1, -1), 316)
        self.assertGreaterEqual(DistanceCalc.dist_calc(1, 1, -1, -1), 312)

        # Checking correct values
        distance = DistanceCalc.dist_calc(lat1, lon1, lat2, lon2)
        self.assertLessEqual(distance, 75)
        self.assertGreaterEqual(distance, 74.690)
        self.assertGreater(distance, 0)

        # Checking the function doesn't return a negative value
        for a in range(0, 50):
            lat1 = a
            for b in range(0, 50):
                lon1 = b
                for c in range(0, 50):
                    lat2 = c
                    for d in range(0, 50):
                        lon2 = d
                        distance = DistanceCalc.dist_calc(lat1, lon1, lat2, lon2)
                        self.assertGreaterEqual(distance, 0)

    def test_types(self):
        # Checking the function doesn't accept wrong typed arguments
        self.assertRaises(TypeError, DistanceCalc.dist_calc, "a", 2, 3, 4)
        self.assertRaises(TypeError, DistanceCalc.dist_calc, 1, True, 3, 4)
        self.assertRaises(TypeError, DistanceCalc.dist_calc, 1, 2, 3+5j, 2)
        self.assertRaises(TypeError, DistanceCalc.dist_calc, 1, 2, 3, "value")
    
    def test_values(self):
        #Checking the function doesn't accept wrong valued arguments
        values = [-91, 91]
        lat1 = 1
        lon1 = 1
        lat2 = 2
        lon2 = 2
        args = [lat1, lon1, lat2, lon2]
        for i in range(4):
            args[0] = 1
            args[1] = 1
            args[2] = 2
            args[3] = 2
            for v in values:
                args[i] = v
                self.assertRaises(ValueError, DistanceCalc.dist_calc, args[0], args[1], args[2], args[3])
                # print("Entered values are:", args[0], args[1], args[2], args[3])


if __name__ == '__main__':
    unittest.main()
