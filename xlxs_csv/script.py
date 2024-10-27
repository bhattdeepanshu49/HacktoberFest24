import openpyxl
import pandas as pd

# def remove_spaces_from_xlsx(file_path):
#     # Load the workbook and select the active worksheet
#     workbook = openpyxl.load_workbook(file_path)
#     sheet = workbook.active

#     # Iterate through all cells in the worksheet
#     for row in sheet.iter_rows():
#         for cell in row:
#             if isinstance(cell.value, str):
#                 # Remove spaces from the cell value
#                 cell.value = cell.value.replace(" ", "")

#     # Save the modified workbook
#     workbook.save(file_path)

# if __name__ == "__main__":
#     file_path = '/home/kalilinux/Downloads/workatlearn/sam/phrases.xlsx'
#     remove_spaces_from_xlsx(file_path)
#     print("Spaces removed successfully.")


data = pd.read_excel('phrases.xlsx')
dataset = pd.DataFrame(data)

cleaned_noun = dataset["noun"].replace(" ", "")
cleaned_adjectives = dataset["adjectives"].replace(" ", "")
cleaned_verbs = dataset["verbs"].replace(" ", "")
cleaned_adverbs = dataset["adverbs"].replace(" ", "")
cleaned_prepositiions = dataset["adverbs"].replace(" ", "")
cleaned_miscellaneous = dataset["miscellaneous"].replace(" ", "")

file = {
    "noun": cleaned_noun,
    "adjectives": cleaned_adjectives,
    "verbs": cleaned_verbs,
    "adverbs": cleaned_adverbs,
    "miscellaneous": cleaned_miscellaneous,
    "prepositions": cleaned_prepositiions
}

df = pd.DataFrame(file)
df.to_csv("cleaned_phrases.csv", index=False)