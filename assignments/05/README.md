# Data Formats, Open Data, Tidy Data

In this exercise, you will be working with **Lord of the Rings** data. The dataset can be found on [Kaggle](https://www.kaggle.com/paultimothymooney/lord-of-the-rings-data). 

1. Download and obtain the following CSV file: [`lotr_scripts.csv`](https://www.kaggle.com/datasets/paultimothymooney/lord-of-the-rings-data?select=lotr_scripts.csv).

2. Document and describe the different data fields.
- `char`: Name des Charakters, der den Dialog spricht.
- `dialog`: Der Text des Dialogs.
- `movie`: Der Film, in dem der Dialog vorkommt.


3. Identify "dirty" data fields and clean them up. Use regex replace, spreadsheets, OpenRefine or whatever you like.

Entfernen von führenden und folgenden Leerzeichen:
import re
cleaned_character = re.sub(r'^\s+|\s+?$', '', character)

Ersetzen von unerwünschten Sonderzeichen im Dialog:
cleaned_dialogue = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', dialogue)


5. Document your working steps in a Markdown-formatted file. Export your dataset as a clean CSV file. Add both files to this repository (in this directory). 
6. Analyze the data set using shell scripts and/or regex. Document the commands in an additional section in your Markdown-formatted file. 
    * Find the total number of lines and unique words used in the dialogs. 
    * What is the distribution on the three different films? 
    * What are the top 5 characters in the char column?
    * What are the top 5 characters in the dialogues?





