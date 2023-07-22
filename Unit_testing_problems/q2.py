from matplotlib import pyplot as plt
import mains
import unittest

class TestLen(unittest.TestCase):
    def setUp(self):
        self.data_reader=list(mains.matches_reader)
        self.win_list=[[1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 1], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
    def testRun(self):
        self.teams=['Chennai Super Kings', 'Deccan Chargers','Delhi Daredevils', 'Kolkata Knight Riders',
                   'Kings XI Punjab', 'Mumbai Indians','Pune Warriors', 'Royal Challengers Bangalore',
                   'Rising Pune Supergiants']
        self.years=sorted([str(i) for i in range(2008,2018)])
        self.total_matches= {} 
        for team in self.teams:
            for year in self.years:
                if team not in self.total_matches.keys():
                    self.total_matches.update({team: {year:0}})
                else:
                    self.total_matches[team].update({year:0})

        for i in range(len(self.data_reader)):
            if self.data_reader[i]['winner']:
                self.total_matches[self.data_reader[i]['winner']][self.data_reader[i]['season']]+= 1

        self.won_l=[]
        for i in self.teams:
            won=[]
            for j in self.years:
                won.append(self.total_matches[i][j])
            self.won_l.append(won)
        
        self.assertEqual(self.win_list,self.won_l)
        
    def plotting(self):
        colour=['r','b','g','y','m','c','pink','purple','brown','grey']

        plt.bar(self.years,self.won_l[0],color='k')
        for i in range(1,len(self.won_l)):
            plt.bar(self.years,self.won_l[i],bottom=self.won_l[i-1],color=colour[i-1])

        plt.xlabel("Years")
        plt.ylabel("No: of matches won")
        plt.legend(self.teams)
        plt.show()


if __name__=='__main__':
    unittest.main()