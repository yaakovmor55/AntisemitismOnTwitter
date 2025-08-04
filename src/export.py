import json
from loader import Loader
from Cleaner import CleanData
from exploration import Exploration


class Export:
    def __init__(self, table, clean_table):
        self.table = table
        self.clean_table = clean_table

    def export_clean_table_to_csv(self):
        self.clean_table.to_csv("../results/tweets_dataset_cleaned.csv")

    def export_result_to_json(self,total_tweets, average_length, common_words, longest_3_tweets):
        data_dict = {"total tweets": total_tweets,
                     "average length": average_length,
                     "common words": common_words,
                     "longest 3 tweets": longest_3_tweets}
        with open('../results/results.json', 'w') as j:
            json.dump(data_dict, j)



l = Loader("../data/tweets_dataset.csv")
c = CleanData(l.table)
c.cleaning_commas()
c.convert_to_lower()
c.remove_uncategorized_tweets()
e = Export(l.table, c.table)
e.export_clean_table_to_csv()

a = Exploration(l.table)
e.export_result_to_json(a.total_tweets(), a.average_length(), a.common_words(), a.longest_3_tweets())