import pandas as pd

class Analyse:
    def __init__(self, path = "dataset/bestsellers with categories.csv"):
        self.booklist = pd.read_csv(path)
        self.cleanData()

    def cleanData(self):
        self.booklist.set_index('Name', inplace=True)

    #def getCategories(self):
        #self.fic = self.booklist[self.booklist['Genre']=='Fiction']
        #self.fic_year = self.fic[['Genre', 'Year']].groupby('Year').count()
        #return self.fic_year
       
        #self.t_genre = self.booklist.groupby('Genre').count()
        #return self.t_genre['Total'] 

#____________________________________Fiction Vs Non Fiction______________________________

    def getFicVsNonFic(self):
        return self.booklist.groupby('Genre').count()['Price']
        #return self.t_genre['Price']

#___________________________________Fiction Book per year_____________________________

    def getFictionPerYear(self):
        fic = self.booklist[self.booklist['Genre']=='Fiction']
        return fic.groupby('Year').count()['Genre']

#__________________________________Non Fiction book Per Year________________________________

    def getNonFictionPerYear(self):
        self.n_fic = self.booklist[self.booklist['Genre']== 'Non Fiction']
        return self.n_fic.groupby('Year').count()['Genre']

#______________________________________NO oF BOOK PUBLISHED BY AN AUTHOR_____________________________

    def getBooksByAuth(self):
        self.auth = self.booklist.groupby('Author').count()['Price']
        return self.auth.head(20).sort_values(ascending = False)