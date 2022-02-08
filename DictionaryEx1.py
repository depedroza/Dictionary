# This program creates a dictionary with a list of dictionaries listing information matched on a Course No key
# The program also has a searchable feature to search by Course No and display the course information stored in the dictionaries


def main():
    courseNo = {
        "CS101": {"roomNo": "3004", "instructor": "Haynes", "meet_time": "8:00 a.m."},
        "CS102": {"roomNo": "4501", "instructor": "Alvarado", "meet_time": "9:00 a.m."},
        "CS103": {"roomNo": "6755", "instructor": "Rich", "meet_time": "10:00 a.m."},
        "NT110": {"roomNo": "1244", "instructor": "Burke", "meet_time": "11:00 a.m."},
        "CM241": {"roomNo": "1411", "instructor": "Lee", "meet_time": "1:00 p.m."},
    }
    search = input("Enter a course number to search course information. ")
    if search in courseNo:
        print("Course Number: " + search)
        print("Room Number: " + courseNo[search]["roomNo"])
        print("Instructor: " + courseNo[search]["instructor"])
        print("Meeting Time: " + courseNo[search]["meet_time"])
    else:
        print(search + " not found.")


main()
