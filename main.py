import webbrowser
import time
import pyautogui
import clipboard
import os
import json

directory_path = r'C:\Users\Eagle\Desktop\Beirzeit-University-generate-optimal-table-of-courses-main\coursesTXT\save'
dec={
    "PUBA": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=266&study_lang=",
    "ANTH": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=367&study_lang=",
    "ACCT": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=268&study_lang=",
    "ACFI": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=11419&study_lang=",
    "ARAB": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=269&study_lang=",
    "ARCH": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=347&study_lang=",
    "ARTS": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=370&study_lang=",
    "BIOC": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=298&study_lang=",
    "BIOL": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=270&study_lang=",
    "BUSA": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=324&study_lang=",
    "CHEM": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=272&study_lang=",
    "CHIN": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=9715&study_lang=",
    "COMM": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=15969&study_lang=",
    "COMP": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=273&study_lang=",
    "CSEC": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=15968&study_lang=",
    "CULS": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=329&study_lang=",
    "COVA": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=10276&study_lang=",
    "DSGN": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=11699&study_lang=",
    "DSIN": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=15279&study_lang=",
    "ECON": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=275&study_lang=",
    "EDUC": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=2787&study_lang=",
    "ENAR": "https://ritaj.birzeit.edu/hemis/courses?term=1231&bu=276&lang=ar&mode=CB",
    "ENBE": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=16002&study_lang=",
    "ENCE": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=277&study_lang=",
    "ENCS": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=331&study_lang=",
    "ENEE": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=278&study_lang=",
    "ENEV": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=11860&study_lang=",
    "ENGC": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=333&study_lang=",
    "ENGL": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=280&study_lang=",
    "ENMC": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=2225&study_lang=",
    "ENME": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=281&study_lang=",
    "ENPL": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=8295&study_lang=",
    "FINN": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=325&study_lang=",
    "FREN": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=279&study_lang=",
    "FRSC": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=16602&study_lang=",
    "GEOG": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=282&study_lang=",
    "GEOI": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=14899&study_lang=",
    "GERM": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=7993&study_lang=",
    "HEBR": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=337&study_lang=",
    "HIST": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=348&study_lang=",
    "INED": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=14945&study_lang=",
    "ITAL": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=338&study_lang=",
    "JURI": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=267&study_lang=",
    "LRNJ": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=10516&study_lang=",
    "MAEC": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=213&study_lang=",
    "MATH": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=284&study_lang=",
    "MDIA": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=356&study_lang=",
    "MDJO": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=9094&study_lang=",
    "MKET": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=662&study_lang=",
    "MUSI": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=9193&study_lang=",
    "NURS": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=842&study_lang=",
    "NUTD": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=841&study_lang=",
    "PHAR": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=3029&study_lang=",
    "PHED": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=7992&study_lang=",
    "PHIL": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=330&study_lang=",
    "PHRB": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=16622&study_lang=",
    "PHYS": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=286&study_lang=",
    "POLS": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=289&study_lang=",
    "PSYC": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=2788&study_lang=",
    "PUBH": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=266&study_lang=",
    "SOCI": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=288&study_lang=",
    "SOCW": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=369&study_lang=",
    "SPAN": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=1621&study_lang=",
    "SPAU": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=4269&study_lang=",
    "STAT": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=352&study_lang=",
    "TIFR": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=339&study_lang=",
    "TRAN": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=13880&study_lang=",
    "TURK": "https://ritaj.birzeit.edu/hemis/courses?mode=CB&term=1231&lang=en&bu=7653&study_lang=",





}
delay = 3  # In seconds




def startJson(preName):
    sections = []
    current_section = {}
    jumpToNextLine = False
    flagError = False
    with open(fr'C:\Users\Eagle\Desktop\Beirzeit-University-generate-optimal-table-of-courses-main\coursesTXT\toUse/{preName}.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        read_course_name = False

        for line in lines:
            line = line.strip()

            if not line:
                continue
            # print(line)
            # Check if the line contains a course name
            if flagError and line.split('\t')[0].isalpha():
                sections[len(sections) - 1]['days'] += ', ' + line.split('\t')[0]
            elif flagError and line.split('\t')[0][0].isnumeric():
                sections[len(sections) - 1]['time'] = line.split('\t')[0]
                sections[len(sections) - 1]['place'] = "N/A"
                flagError = False
            if line.startswith(preName):
                current_section['name of course'] = line.split()[0]
                # print(current_section['name of course'])
                read_course_name = True
                continue

            # Skip unneeded data lines
            if read_course_name:
                read_course_name = False
                continue

            # Check if the line contains section information

            # print(match)
            if line.split('\t')[0] == 'Lecture':
                current_section['sec'] = int(line.split('\t')[1])
                # print(match.group(1))
                current_section['name of instructor'] = line.split('\t')[2]
                current_section['number of students'] = line.split('\t')[3]
                jumpToNextLine = True
                continue

            # Check if the line contains days, time, and place
            if jumpToNextLine:
                current_section['days'] = line.split('\t')[0]
                try:
                    current_section['time'] = line.split('\t')[1]
                except:
                    flagError = True
                    sections.append(current_section.copy())
                if not flagError:
                    current_section['place'] = line.split('\t')[2]
                    sections.append(current_section.copy())
                    # print(sections)
                jumpToNextLine = False

    # Save the sections data as a JSON file
    with open(fr'C:\Users\Eagle\Desktop\Beirzeit-University-generate-optimal-table-of-courses-main\coursesJSON/{preName}.json', 'w', encoding='utf-8') as json_file:
        json.dump(sections, json_file, ensure_ascii=False, indent=4)

    print(f"Data has been extracted and saved to '{preName}.json'.")

def close_current_tab():
    # Close the current tab using keyboard shortcuts (e.g., Ctrl+W)
    pyautogui.hotkey('ctrl', 'w')



def get_data(file_name, url):
    webbrowser.open(url)
    time.sleep(5)  # Adjust the sleep time as needed to allow the page to fully load
    page_height = pyautogui.size().height
    scroll_height = 0

    while scroll_height < page_height:
        # Scroll down by a portion of the screen height
        pyautogui.scroll(100)  # Adjust the scroll amount as needed
        time.sleep(1)  # Adjust the sleep time as needed
        scroll_height += 100  # Adjust the scroll amount as needed

    pyautogui.hotkey('ctrl', 'a')  # Select all
    pyautogui.hotkey('ctrl', 'c')  # Copy
    time.sleep(0.5)
    copied_text = clipboard.paste()

    with open(
            fr"C:\Users\Eagle\Desktop\Beirzeit-University-generate-optimal-table-of-courses-main\coursesTXT\toUse\{file_name}.txt",
            "w", encoding="utf-8") as file:
        file.write(copied_text)

    startJson(file_name)
    close_current_tab()
def read_files_names():
    file_list = [f for f in os.listdir(directory_path) if f.endswith('.txt')]
    return file_list

def start():
    file_list = read_files_names()

    for filename in file_list:
        get_data(filename.split('.')[0], dec[filename.split('.')[0]])

start()