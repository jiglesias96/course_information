def main():
    course_num = input("Enter your Course Number: ")

    room_number_dictionary = room_number()
    instructor_dictionary = instructor()
    meeting_time_dictionary = meeting_time()

    print("Your room number is: ", room_number_dictionary[course_num])
    print("Your instructor is: ", instructor_dictionary[course_num])
    print("Your meeting time is: ", meeting_time_dictionary[course_num])
def room_number():
    _room_number = {'CS101' : '3004', 'CIS102' : '4501', 'CS103' : '6755', 'NT110' : '1244', 'CM241' : '1411'}

    return _room_number
def instructor():
    _instructor = {'CS101': 'Haynes', 'CIS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}

    return _instructor
def meeting_time():
    _meeting_time = {'CS101': '8:00 a.m.', 'CIS102': '9:00 a.m.', 'CS103': '10:00 a.m.',
                     'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}
    return _meeting_time
main()