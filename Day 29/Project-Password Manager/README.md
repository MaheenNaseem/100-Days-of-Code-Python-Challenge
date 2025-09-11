# Day 30 - Changes in Password Manager: 
This is a GUI-based Password Manager built with Python’s tkinter. <br>
It allows you to:
1. Generate secure passwords
2. Save them in a local JSON file
3. Search for saved credentials
4. Copy passwords directly to the clipboard
<br>
This project is based on Angela Yu’s 100 Days of Code – Day 30 project, but I extended it with additional features and improvements.

## Project Feature: 
1. Generates strong passwords using letters, numbers, and symbols
2. It stores the entered credentials (Website, email, password)
3. Allows you to search from your previously saved websites
4. Automatically copies the password when generated
5. Dropdown Website List (Combobox) for easy searching
6. Error Handling 
7. No Duplicate data as website names are (strip() + lower()) so the same site isn’t stored twice.

## Here are some changes that I implemented in the original Angela Yu's Version: 
1. Dropdown (Combobox) with auto-refresh
2. Duplicate Prevention by Lowercasing + strip the website
3. Error handling for FileNotFoundError + JSONDecodeError for when the file exists but is empty
4. Ask users to double-check their cresidential before saving
5. Better UI: Auto-clear, focus reset, better messages
6. Allow user to copies the password when they search the website

## Screen Shots:
### Saving Password 
<br>
<img width="722" height="678" alt="image" src="https://github.com/user-attachments/assets/ec7ad81e-35d1-4920-a97b-553e8e4f28ae" /> <br>
<img width="716" height="684" alt="image" src="https://github.com/user-attachments/assets/3e098e77-c0c3-4340-b182-0c3c382c2e58" /> <br>
<img width="475" height="278" alt="image" src="https://github.com/user-attachments/assets/0da17136-0c0a-456a-b6e6-df817d7fb14e" /> <br>
<img width="342" height="242" alt="image" src="https://github.com/user-attachments/assets/b7bc93d4-103b-48bc-ae2b-fb85d1797153" /> 

### Retrieving Password
<br>
<img width="717" height="681" alt="image" src="https://github.com/user-attachments/assets/870a0439-7f44-49e4-9e74-ed5d068fd574" /> <br>
<img width="944" height="677" alt="image" src="https://github.com/user-attachments/assets/6e130615-ea9a-4cec-8be7-c8f4b0d6dda1" /> 

### Json File: 
<br>
<img width="799" height="711" alt="image" src="https://github.com/user-attachments/assets/fb1c1b73-f0da-4d75-a23b-e02d378296a6" /> <br> 





