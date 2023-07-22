from matplotlib import pyplot as plt
import mains
import unittest

class TestLen(unittest.TestCase):
    def setUp(self):
        self.data_reader=mains.deliveries_reader
        self.top3=['Ck','Rk','Bk']
    def testRun(self):
        self.top3_op={}
        self.overs={}
        for delivery in self.data_reader:
            if delivery['bowler'] not in self.top3_op:
                self.top3_op[delivery['bowler']]=0
                self.overs[delivery['bowler']]=0
            self.top3_op[delivery['bowler']]+=int(delivery['total_runs'])
            self.overs[delivery['bowler']]+=1
        for over in self.overs:
            self.overs[over]/=6
            overs=round(self.overs[over],2)
            economy_rate=self.top3_op[over] / overs
            self.top3_op[over]=round(economy_rate,2)
            self.top_bowler=list(dict(sorted(self.top3_op.items(), key=lambda x:x[1])))[:3]
        
        self.assertEqual(self.top3,self.top_bowler)
    def plotting(self):
        plt.bar(self.top_bowler,list(self.top3_op.values()))
        plt.xlabel=("Bowlers")
        plt.ylabel=("economy rate")
        plt.show()
if __name__=='__main__':
    unittest.main()


