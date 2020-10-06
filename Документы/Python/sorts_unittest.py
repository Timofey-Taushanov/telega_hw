import unittest
from sorts import bubble
from sorts import qsort
from sorts import merge

class Bubble_Test(unittest.TestCase):

    def test_one_element_in_list(self):
        bruh = [1]
        bubble(bruh)
        self.assertEqual(bruh, [1])
    
    def test_empty_list(self):
        bruh = []
        bubble(bruh)
        self.assertEqual(bruh, [])
    
    def test_incorrect_type_of_incoming_element(self):
        bruh = 'Bruh'
        bubble(bruh)
        self.assertEqual(bruh, 'Bruh')

    def test_incorrect_type_of_elements_in_list(self):
        bruh = [[2, 2, 8], [1, 4, 8, 8], 'fonk']
        bubble(bruh)
        self.assertEqual(bruh, [[2, 2, 8], [1, 4, 8, 8], 'fonk'])
    
    def test_normal_work(self):
        bruh = [7, 2, 1, 8, 6, 3, 5, 4]
        bubble(bruh)
        self.assertEqual(bruh, [1, 2, 3, 4, 5, 6, 7, 8])

class Qsort_Test(unittest.TestCase):
    
    def test_one_element_in_list(self):
        bruh = [1]
        qsort(bruh)
        self.assertEqual(bruh, [1])
    
    def test_empty_list(self):
        bruh = []
        qsort(bruh)
        self.assertEqual(bruh, [])
    
    def test_incorrect_type_of_incoming_element(self):
        bruh = 'Bruh'
        qsort(bruh)
        self.assertEqual(bruh, 'Bruh')

    def test_incorrect_type_of_elements_in_list(self):
        bruh = [[2, 2, 8], [1, 4, 8, 8], 'fonk']
        qsort(bruh)
        self.assertEqual(bruh, [[2, 2, 8], [1, 4, 8, 8], 'fonk'])
    
    def test_normal_work(self):
        bruh = [7, 2, 1, 8, 6, 3, 5, 4]
        qsort(bruh)
        self.assertEqual(bruh, [1, 2, 3, 4, 5, 6, 7, 8])

class Merge_Test(unittest.TestCase):
    
    def test_one_element_in_list(self):
        bruh = [1]
        merge(bruh)
        self.assertEqual(bruh, [1])
    
    def test_empty_list(self):
        bruh = []
        merge(bruh)
        self.assertEqual(bruh, [])
    
    def test_incorrect_type_of_incoming_element(self):
        bruh = 'Bruh'
        merge(bruh)
        self.assertEqual(bruh, 'Bruh')

    def test_incorrect_type_of_elements_in_list(self):
        bruh = [[2, 2, 8], [1, 4, 8, 8], 'fonk']
        merge(bruh)
        self.assertEqual(bruh, [[2, 2, 8], [1, 4, 8, 8], 'fonk'])
    
    def test_normal_work(self):
        bruh = [7, 2, 1, 8, 6, 3, 5, 4]
        merge(bruh)
        self.assertEqual(bruh, [1, 2, 3, 4, 5, 6, 7, 8])
    

unittest.main()