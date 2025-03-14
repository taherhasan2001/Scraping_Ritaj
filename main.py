import webbrowser
import time
import pyautogui
import clipboard
import json
import os

delay = 10  # In seconds
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
url = ''

def openEdge():
    pyautogui.press('win')
    time.sleep(0.1)

    pyautogui.typewrite('Microsoft Edge')

    # Add a small delay to ensure the typing is completed before pressing Enter
    time.sleep(0.1)

    # Press Enter
    pyautogui.press('enter')
    time.sleep(0.1)

    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.1)
    pyautogui.typewrite(url)
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('f11')
    time.sleep(0.1)
def write_to_json():
    with open(f'BZU.json','w', encoding='utf-8') as json_file:
        json.dump(sections, json_file, ensure_ascii=False, indent=4)

def get_data(delay=5):

    # Adjust the sleep time as needed to allow the page to fully load
    time.sleep(delay)
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()

    # Calculate the coordinates for the middle of the screen
    middle_x = screen_width // 2
    middle_y = screen_height // 2

    # Move the mouse to the middle of the screen
    pyautogui.moveTo(middle_x, middle_y)

    # Perform a mouse click (left-click) at the current mouse position (middle of the screen)
    pyautogui.click()


    # Use PyAutoGUI to simulate keyboard shortcuts for copying
    pyautogui.hotkey('ctrl', 'a')  # Select all
    pyautogui.hotkey('ctrl', 'c')  # Copy

    # Close the current tab (You need to implement this function)
    # close_current_tab()

    # Add a delay before attempting to paste from clipboard
    time.sleep(delay)

    # Retrieve the copied text from the clipboard
    copied_text = clipboard.paste()

    # Print the copied text (for debugging)

    # Add another delay before writing to a file
    time.sleep(delay)

    # Save the copied text to a file
    with open("BZU.txt", "w", encoding="utf-8") as file:
        file.write(copied_text)

    read_from_txt()
    close_current_tab()


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
        isLab = False
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
                isLab = True
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
                isLab = False
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
                    if isLab:
                        current_section['name of course'] = 'lab' + current_section['name of course'].replace('lab', '')

                    elif subCourseName:
                        current_section['name of course'] = 'sub'+current_section['name of course'].replace('sub', '')
                    sections.append(current_section.copy())

                jumpToNextLine = False

def close_current_tab():
    # Close the current tab using keyboard shortcuts (e.g., Ctrl+W)
    pyautogui.hotkey('ctrl', 'w')






# function that read from file "link_here.txt" and read the first line as link
def read_link():
    with open("link_here.txt", "r") as file:
        link = file.readline()
    return link

# function to delete file "BZU.txt"
def remove_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print(f"{filename} ERROR with removing this file 'contact with Taher Hasan'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    # "date": "2024-01-20",
    # "time": "11:45:00"
if __name__ == '__main__':
    url = read_link()
    openEdge()
    dateNow = time.strftime('%Y-%m-%d')
    timeNow = time.strftime('%H:%M:%S')

    get_data(delay= 1)

    write_to_json()
    remove_file("BZU.txt")
    # write the time and date in date.json in form : {"date": dateNow,"time": timeNow}
    with open("date.json", "w") as file:
        file.write(f'{{"date": "{dateNow}","time": "{timeNow}"}}')

    # input(f"Number of sections: {len(sections)}\nPress Enter to exit...")
