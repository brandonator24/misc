import os
import re
import sys

# Gather info from user
dirname = input("Enter file directory: ")
bad_text = ""
bad_text_list = []
new_name_list = []
default = ["gaming", "sfx", "hd", "sound effect", "sound", "effect", "original", "clip", "high quality", "transparent", "image"]
print("(Type 'done' when finished, and 'default' to use default word list)\nEnter phrase/text to be removed...")
while(True):
    bad_text = input("text: ")
    need_append = True
    if(bad_text == "default"):
        need_append = False
        for word in default:
            bad_text_list.append(word)
    if(bad_text != "done" and need_append == True):
        bad_text_list.append(bad_text)
    if(bad_text == "done"):
        print("Beginning file scrub...")
        break

os.chdir(dirname)
print(f"current directory now: {os.getcwd()}")

for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    print(f"cur name: {file_name}")
    
    # Remove target word(s)
    for bad_text in bad_text_list:
        if(len(re.findall(bad_text, file_name, flags=re.IGNORECASE)) > 0):
            new_file_name = re.sub(bad_text, "", file_name, flags=re.IGNORECASE)
            print(f"removed bad text: {new_file_name}")
            file_name = new_file_name
    
    # Replace underscores and dashes with spaces if surrounded by other chars, not whitespace
    dash_score_pattern = "(\-|\_)(?=.)(?<=.)"
    dash_scores = re.findall(dash_score_pattern, file_name)
    if(len(dash_scores) > 0):
        space_subbed_name = re.sub(dash_score_pattern, " ", file_name)
        file_name = space_subbed_name
        print(f"Spaces Substituted: {file_name}")

    # Remove special chars
    # most special characters unnecessary in titles
    special_chars_pattern = "[\-\[\]\/\\\{\}\(\)\*\+\?\.\^\$\|\!%+&,;#=$\x22]+"
    special_chars = re.findall(special_chars_pattern, file_name)
    if(len(special_chars) > 0):
        no_special_chars = re.sub(special_chars_pattern, "", file_name)
        file_name = no_special_chars
        print(f"Removed special characters: {file_name}")

    # Remove straggler chars
    # targets singular characters surrounded by whitespace, or at the end of name if not number
    straggler_pattern = "((\s).(?=\s))+|(\s)(?!\d).$"
    stragglers = re.findall(straggler_pattern, file_name)
    if(len(stragglers) > 0):
        removed_stragglers = re.sub(straggler_pattern, "", file_name)
        file_name = removed_stragglers
        print(f"Removed stragglers {file_name}")

    # Remove extra spaces
    # finds any number of spaces more than 1
    ex_spaces = re.findall("[ ]{2,}", file_name)
    if(len(ex_spaces) > 0):
        fix_spaces = re.sub("[ ]{2,}", " ", file_name, flags=re.IGNORECASE)
        file_name = fix_spaces
        print(f"Removed extra spaces: {file_name}")
    if(file_name[-1] == " "):
        stripped_name = file_name[:-1]
        file_name = stripped_name
        print(f"Removed ending spaces: {file_name}")

    # Fix Caps lock titles
    # first letter remains upper, rest are lowered if more than 3 capitals found in word
    words = file_name.split()
    new_words = []
    for word in words:
        # Looks for words with more than 3 capital letters
        if(len(re.findall("([A-Z]{4,})+", word)) > 0):
            print(word)
            new_word = word[0]
            for i in range(1,len(word)):
                if(word[i].isupper()):
                    new_word += word[i].lower()
            new_words.append(new_word)      
            file_name = ' '.join(new_words)
    print(f"Lowered letters: {file_name}")

    # append all file names
    final_name = file_name + file_ext
    new_name_list.append(final_name)


# Actually change file names
for new_file in new_name_list:
    print(f"~{new_file}")
confirm = input("CONFIRM FILE NAMES (y/n): ")
if(confirm == "y" or confirm == "Y"):
    file_index = 0
    for file in os.listdir():
        try:
            os.rename(file, new_name_list[file_index])
        except FileExistsError as e:
            print("FILE EXISTS, RENAMING...")
            num_files = sum(1 for file_name in os.listdir() if os.path.isfile(file_name))
            next_num = num_files + 1
            duplicate_name = new_name_list[file_index] + "(" + str(next_num) + ")"
            os.rename(file, duplicate_name)
        file_index += 1
else:
    sys.exit()