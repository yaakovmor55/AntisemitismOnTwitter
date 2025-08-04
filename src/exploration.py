
from loader import Loader


class Exploration:
    def __init__(self, table):
        self.table = table

    # Count all tweets for each category
    def total_tweets(self):
        antisemitic = self.table["Biased"].value_counts()[1]
        non_antisemitic =  self.table["Biased"].value_counts()[0]
        total = self.table["Biased"].count()
        unspecified = (total - antisemitic) - non_antisemitic

        #  Returns a dictionary with the results and converts the values to int
        return {"antisemitic": int(antisemitic),
                "non_antisemitic": int(non_antisemitic),
                "total": int(total),
                "unspecified": int(unspecified)}

    # Calculate average number of words for each category
    def average_length(self):
        antisemitic_words = (self.table["Text"][self.table["Biased"] == 1]).str.split()
        antisemitic = sum(antisemitic_words.str.len()) / antisemitic_words.shape[0]

        non_antisemitic_words = (self.table["Text"][self.table["Biased"] == 0]).str.split()
        non_antisemitic =  sum(non_antisemitic_words.str.len()) / non_antisemitic_words.shape[0]

        total_words = (self.table["Text"]).str.split()
        total = sum(total_words.str.len()) / total_words.shape[0]


        return {"antisemitic": antisemitic,
                "non_antisemitic": non_antisemitic,
                "total": total}

    # Returns the 3 longest tweets (currently only returns 1, needs to be fixed)
    def longest_3_tweets(self):
        longest_text_index = (self.table["Text"]).str.len().idxmax()
        longest_text = self.table["Text"][longest_text_index]
        return longest_text

    # Searching for the most common words (needs to finish)
    def common_words(self):
        all_words = self.table['Text'].astype(str).str.lower().str.findall(r'\b\w+\b').sum()

        return all_words

    # Returns a dictionary with the amount of uppercase letters for each category (still to be completed)
    def uppercase_words(self):
        return



# e = Exploration(l.table)

# k = (l.table["Text"][l.table["Biased"] == 1]).str.split()

# print(e.longest_3_tweets())
