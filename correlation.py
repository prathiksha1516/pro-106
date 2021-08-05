import numpy as np
import csv

def getDataSource(data_path):
    Marks_In_Percentage=[]
    presentdays=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))
            presentdays.append(float(row["Days Present"]))
    return {"x":Marks_In_Percentage,"y":presentdays} 

def findCorrelation(datasorce):
    correlation=np.corrcoef(datasorce["x"],datasorce["y"])       
    print("correlation is :",correlation[0,1])

def setup():
    data_path="Student Marks vs Days Present.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
    
setup()    
        
