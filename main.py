import webbrowser
import time
import pyautogui
import clipboard
import json

links = [103,113,138,174,212,664,2186,7253,10568]
delay = 5  # In seconds
sections = []
courses_names = ["PUBA","ANTH",
"ACCT","ACFI","ARAB","ARCH","ARTS","BIOC","BIOL","BUSA",
"CHEM","CHIN","COMM","COMP","CSEC","CULS","COVA","DSGN",
"DSIN","ECON","EDUC","ENAR","ENBE","ENCE","ENCS","ENEE",
"ENEV","ENGC","ENGL","ENMC","ENME","ENPL","FINN","FREN",
"FRSC","GEOG","GEOI","GERM","HEBR","HIST","INED","ITAL",
"JURI","LRNJ","MAEC","MATH","MDIA","MDJO","MKET","MUSI",
"NURS","NUTD","PHAR","PHED","PHIL","PHRB","PHYS","POLS",
"PSYC","PUBH","SOCI","SOCW","SPAN","SPAU","STAT","TIFR",
"TRAN","TURK","GENS","MCLS","MIPT","WOHE","PHED","ENEE",
"GENG","JMEE","MSCE","SWEN","DSGN","DSIN","MUSI","MCLS",
"NURS","NUTD","SPAU","WOHE","GOVS","INRE","JURI","LECO",
"CHEM","GENS","PHYS","STAT","ASDS","CODE","DMHR","PHSS",
"GADS","HAIC","HLTH","IMRS","INST","ISST","LAIT","RENE",
"WEEN","WESC","ACCA","FINN","ARSK","ARST","CCST","CPSY",
"PASP","TOUR","TRAN","WOMS",

]

def write_to_json():
    with open(f'BZU.json','w', encoding='utf-8') as json_file:
        json.dump(sections, json_file, ensure_ascii=False, indent=4)


def read_from_txt():
    """
    Read the data from the BZU.txt file and store it in a list of sections
    this function used after getting data from each link after it added to BZU.txt
    this reads from the file and store it in sections list
    :return:
    """
    current_section = {}
    jumpToNextLine = False
    flagError = False
    with open(f'BZU.txt','r', encoding='utf-8') as file:
        lines = file.readlines()
        read_course_name = False
        subCourseName = ''
        for line in lines:
            line = line.strip()

            if not line:
                continue

            # Check if the line contains a course name
            if flagError and line.split('\t')[0].isalpha():

                sections[len(sections) - 1]['days'] += ', ' + line.split('\t')[0]
            elif flagError and line.split('\t')[0][0].isalpha():

                for day in line.split("\t")[0].replace(" ","").split(','):
                    sections[len(sections) - 1]['days'] += ', ' + day
            elif flagError and line.split('\t')[0][0].isnumeric():
                sections[len(sections) - 1]['time'] = line.split('\t')[0]
                sections[len(sections) - 1]['place'] = "N/A"
                flagError = False
            if any(line.startswith(course_name) for course_name in courses_names):
                current_section['name of course'] = line.split()[0]
                subCourseName = line.split()[0]
                read_course_name = True
                continue

            # Skip unneeded data lines
            if read_course_name:
                read_course_name = False
                continue

            # Check if the line contains section information

            if line.split('\t')[0] == 'Lab':
                subCourseName = True
                current_section['sec'] = int(line.split('\t')[1])

                current_section['name of instructor'] = line.split('\t')[2]
                current_section['number of students'] = line.split('\t')[3]
                jumpToNextLine = True
                continue
            if line.split('\t')[0] == 'Discussion':
                subCourseName = True
                current_section['sec'] = int(line.split('\t')[1])

                current_section['name of instructor'] = line.split('\t')[2]
                current_section['number of students'] = line.split('\t')[3]
                jumpToNextLine = True
                continue
            if line.split('\t')[0] == 'Lecture':
                subCourseName = False
                current_section['sec'] = int(line.split('\t')[1])

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
                    if subCourseName:
                        current_section['name of course'] = 'sub'+current_section['name of course'].replace('sub', '')
                    sections.append(current_section.copy())

                jumpToNextLine = False

def close_current_tab():
    # Close the current tab using keyboard shortcuts (e.g., Ctrl+W)
    pyautogui.hotkey('ctrl', 'w')


def get_data(url):
    webbrowser.open(url)
    time.sleep(delay)  # Adjust the sleep time as needed to allow the page to fully load
    pyautogui.hotkey('ctrl', 'a')  # Select all
    pyautogui.hotkey('ctrl', 'c')  # Copy
    time.sleep(2)
    copied_text = clipboard.paste()
    with open(f"BZU.txt", "w", encoding="utf-8") as file:
        file.write(copied_text)
    time.sleep(2)
    close_current_tab()
    read_from_txt()


if __name__ == '__main__':

    get_data( "https://ritaj.birzeit.edu/hemis/courses?term=1231&bu=182&lang=en&mode=CB")

    write_to_json()
    input(f"Number of sections: {len(sections)}\nPress Enter to exit...")
