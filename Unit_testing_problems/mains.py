import csv

matches_file=open('mock_matches.csv','r',encoding='utf-8')
matches_reader=csv.DictReader(matches_file)

deliveries_file=open('mock_deliveries.csv','r',encoding='utf-8')
deliveries_reader=csv.DictReader(deliveries_file)
