import unicodecsv
from datetime import datetime
def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        enrollments = list(reader)
    return enrollments

def parse_date(dateString):
    if dateString == '':
        return None
    else:
        return datetime.strptime(dateString, '%Y-%m-%d')

def parse_int(num):
    if num == '':
        return None
    else:
        return int(num)
def parse_float(num):
    if num == '':
        return None
    else:
        return float(num)

def get_unique_students(records):
    unique_students = set()
    for student in records:
        unique_students.add(student['account_key'])
    return unique_students

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
submissions = read_csv('project_submissions.csv')

for enrollment in enrollments:
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    if enrollment['is_udacity'] == 'True':
        enrollment['is_udacity'] = True
    else:
        enrollment['is_udacity'] = False
    if enrollment['is_canceled'] == 'True':
        enrollment['is_canceled'] = True
    else:
        enrollment['is_canceled'] = False
    enrollment['days_to_cancel'] = parse_int(enrollment['days_to_cancel'])
num_of_enrollments = len(enrollments)
unique_enrollments = get_unique_students(enrollments) 
print('total number of enrollments is: ' + str(num_of_enrollments))
print('unique number of enrollments is: ' + str(len(unique_enrollments)))

for en in daily_engagement:
    en['utc_date'] = parse_date(en['utc_date'])
    en['num_courses_visited'] = parse_float(en['num_courses_visited'])
    en['total_minutes_visited'] = parse_float(en['total_minutes_visited'])
    en['lessons_completed'] = parse_float(en['lessons_completed'])
    en['projects_completed'] = parse_float(en['projects_completed'])
    en['account_key'] = en['acct']
    del en['acct']

num_of_engagements = len(daily_engagement)
unique_engagements = get_unique_students(daily_engagement) 
print('total number of engagements is: ' + str(num_of_engagements))
print('unique number of engagements is: ' + str(len(unique_engagements)))

for submission in submissions:
    submission['creation_date'] = parse_date(submission['creation_date'])
    submission['completion_date'] = parse_date(submission['completion_date'])
    #print(submission)
num_of_submissions = len(submissions)
unique_submissions = get_unique_students(submissions) 
print('total number of submissions is: ' + str(num_of_submissions))
print('unique number of submissions is: ' + str(len(unique_submissions)))

