from matplotlib import pyplot as plt
import mains
import unittest

class TestLen(unittest.TestCase):
    def setUp(self):
        self.data_reader=mains.deliveries_reader
        self.teams=['SRH','CSK']
        self.extra_runs=[5,4]
    def testMatch(self):
        self.teams_op=[]
        self.extra_runs_op=[]
        for delivery in self.data_reader:
            if delivery['bowling_team'] not in self.teams_op:
                self.teams_op.append(delivery['bowling_team'])
                self.extra_runs_op.append(0)
            index=self.teams_op.index(delivery['bowling_team'])
            self.extra_runs_op[index]+=int(delivery['extra_runs'])
        self.assertEqual((self.teams,self.extra_runs),(self.teams_op,self.extra_runs_op))
    def plotting(self):
        plt.bar(self.teams_op,self.extra_runs_op)
        plt.xlabel=('Teams')
        plt.ylabel=('Extra_runs')
        plt.show()
    
if __name__=='__main__':
    unittest.main()
        
