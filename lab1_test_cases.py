import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):
    def test_max_list_iter(self):
    #checks the expection ValueError being raised
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    
    #checks if the list only has one value
        self.assertEqual(max_list_iter([0]),0)
    #check if two values are the same
        self.assertEqual(max_list_iter([1,1,2]),2)
        self.assertEqual(max_list_iter([1,2,1]),2)
        self.assertEqual(max_list_iter([2,1,1]),2)
    #check if two values are the same and are the max values
        self.assertEqual(max_list_iter([1,2,2]),2)
        self.assertEqual(max_list_iter([2,2,1]),2)
        self.assertEqual(max_list_iter([1,2,2]),2)
    #check for normal list with max value in each position
        self.assertEqual(max_list_iter([1,2,3]),3)
        self.assertEqual(max_list_iter([1,3,2]),3)
        self.assertEqual(max_list_iter([3,2,1]),3)
    #check for if all the values are the same
        self.assertEqual(max_list_iter([1,1,1]),1)
    #check for floating values
        self.assertEqual(max_list_iter([1.3,1.5,1.7]),1.7)   
    #check if list is empty
        self.assertEqual(max_list_iter([None]),None)
    

    def test_reverse_rec(self):
        #check normal case
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,3,2]),[2,3,1])
        self.assertEqual(reverse_rec([3,1,2]),[2,1,3])
        #check if all values the same
        self.assertEqual(reverse_rec([1,1,1]),[1,1,1])
        self.assertEqual(reverse_rec([1.1,1.1,1.1]),[1.1,1.1,1.1])
        #checks with floating numbers
        self.assertEqual(reverse_rec([1.2,1.24,5.78]),[5.78,1.24,1.2])
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
    	#check if list is empty
        self.assertEqual(reverse_rec([]),[])
    
    def test_bin_search(self):
        #check when search value is in each index
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(0, 0, 10, list_val), 0 )
        self.assertEqual(bin_search(1, 0, 10, list_val), 1 )
        self.assertEqual(bin_search(2, 0, 10, list_val), 2 )
        self.assertEqual(bin_search(3, 0, 10, list_val), 3 )
        self.assertEqual(bin_search(4, 0, 10, list_val), 4 )
        self.assertEqual(bin_search(7, 0, 10, list_val), 5 )
        self.assertEqual(bin_search(8, 0, 10, list_val), 6 )
        self.assertEqual(bin_search(9, 0, 10, list_val), 7 )
        self.assertEqual(bin_search(10, 0, 10, list_val), 8 )

        list_val =[0,1,2,3,4,5,6,7,8]
        self.assertEqual(bin_search(8, 0, 8, list_val), 8 )
        
        #check for floating points
        list_val =[0.1,2.4,34.6,76.45,700,3000,200000]
        self.assertEqual(bin_search(0.1, 0, 6, list_val), 0 )

        #check if all values are the same
        list_val=[1,1,1,1,1,1]
        self.assertEqual(bin_search(1, 0, 5, list_val), 2 )

        #check if desired value appears twice
        list_val=[1,1,1,1,2,2]
        self.assertEqual(bin_search(2, 0, 5, list_val), 4 )

        #check if value is not in list
        list_val =[0,1,2,3,4,5,6,7,8]
        self.assertEqual(bin_search(20, 0, 8, list_val), None )

        #checks if value error is raised with none list
        list_val=None
        with self.assertRaises(ValueError):
             bin_search(1,0,10,list_val)

if __name__ == "__main__":
        unittest.main()

    
