import pandas as pd

# Read the Excel file into a pandas DataFrame
data = pd.read_excel('phrases.xlsx')
dataset = pd.DataFrame(data)

# Clean spaces from each column
cleaned_noun = dataset["noun"].replace(" ", "")
cleaned_adjectives = dataset["adjectives"].replace(" ", "")
cleaned_verbs = dataset["verbs"].replace(" ", "")
cleaned_adverbs = dataset["adverbs"].replace(" ", "")
cleaned_prepositiions = dataset["prepositions"].replace(" ", "")
cleaned_miscellaneous = dataset["miscellaneous"].replace(" ", "")

# Create a dictionary with cleaned data
file = {
    "noun": cleaned_noun,
    "adjectives": cleaned_adjectives,
    "verbs": cleaned_verbs,
    "adverbs": cleaned_adverbs,
    "miscellaneous": cleaned_miscellaneous,
    "prepositions": cleaned_prepositiions
}

# Convert dictionary to DataFrame and export to CSV
df = pd.DataFrame(file)
df.to_csv("cleaned_phrases.csv", index=False)
