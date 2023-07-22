from matplotlib import pyplot as plt
import mains
import unittest

class TestLen(unittest.TestCase):
    def setUp(self):
        self.data_reader=mains.matches_reader
        self.years=[str(i) for i in range(2008,2018)]
        self.count=[1,1,1,1,1,1,1,1,1,1]
    def test_count(self):
        self.years_op=[]
        self.count_op=[]
        for match in self.data_reader:
            if match['season'] not in self.years_op:
                self.years_op.append(match['season'])
                self.count_op.append(1)
            else:
                self.count_op[self.years.index(match['season'])]+=1
        self.assertEqual((self.years,self.count),(self.years_op,self.count_op))
    def plotting(self):
        plt.bar(self.years_op,self.count_op)
        plt.xlabel=('Years')
        plt.ylabel=('No: of matches played')
        plt.show()
if __name__=='__main__':
    unittest.main()