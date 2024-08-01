import re
from collections import Counter
import pandas as pd
import os

def split_into_sentences(text):
    # Define what a "sentence" will be classed as (Split based on sentence-ending punctuation, capital 'Y' not followed by a space, and full stops followed by numbers
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!|,|(?<!\.\d)(?=\s)Y(?!\s))(?!\d)', text)
    # Reattach the capital 'Y' to the beginning of the next sentence (For the words 'You' e.g. You are driving 10kph over the speed limit...)
    for i in range(len(sentences)):
        if sentences[i].startswith('Y'):
            sentences[i] = 'Y' + sentences[i][1:].strip()
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences

def process_participant(participant_number, condition, text, sentence_dict):
    sentences = split_into_sentences(text)
    sentence_counter = Counter(sentences)
    
    # Update sentence_dict with new sentences and their counts
    for sentence in sentence_dict.keys():
        sentence_dict[sentence] = sentence_counter.get(sentence, 0)
    
    for sentence in sentence_counter.keys():
        if sentence not in sentence_dict:
            sentence_dict[sentence] = 0
            sentence_dict[sentence] = sentence_counter[sentence]
    
    # Create a DataFrame for the current participant/session
    data = {'Participant': [participant_number], 'Condition': [condition]}
    data.update(sentence_dict)
    df = pd.DataFrame(data)
    
    return df, sentence_dict

def get_condition(participant_number):
    # Assign conditions based on the participant number (Change this as needed)
    if participant_number in range(1, 10) or participant_number in [12, 13]:
        return '0'  # Control
    else:
        return '1'  # Experimental

def main():
    all_data = []
    sentence_dict = {}
    participant_number = 1

    # Print the current working directory so you can check the files are in the right place
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")
    
    
#Search WD for file names with "PPT (ppt#) CONVO.txt" but this can be changed as needed, can even just list the files.
    while participant_number <= 18:
        filename = f"PPT{participant_number:03d} CONVO.txt"
        if not os.path.isfile(filename):
            print(f"File '{filename}' not found. Skipping to the next participant.")
            participant_number += 1
            continue

        with open(filename, 'r') as file:
            text = file.read()
        
        condition = get_condition(participant_number)

        df, sentence_dict = process_participant(participant_number, condition, text, sentence_dict)
        all_data.append(df)
        participant_number += 1
    
    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        # Export the DataFrame to a CSV, change name as needed
        final_df.to_csv('convo_condition.csv', index=False)
        print("The data has been exported to 'convo_condition.csv'")
    else:
        print("No data to export.")

if __name__ == "__main__":
    main()
