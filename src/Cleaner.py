from loader import Loader


class CleanData:
    def __init__(self, table):
        self.table = table.copy()
        self.relevant_columns = table[["Text", "Biased"]].copy()

    def cleaning_commas(self):
        self.relevant_columns.loc[:,"Text"] = self.relevant_columns["Text"].str.replace(',','',regex=False)

    def convert_to_lower(self):
        self.relevant_columns.loc[:, "Text"] = self.relevant_columns["Text"].str.lower()


    def remove_uncategorized_tweets(self):
        self.relevant_columns = self.relevant_columns[
            self.relevant_columns["Biased"].isin([0, 1])
        ]


