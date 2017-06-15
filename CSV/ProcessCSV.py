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
    print(enrollment)


for en in daily_engagement:
    en['utc_date'] = parse_date(en['utc_date'])
    en['num_courses_visited'] = parse_float(en['num_courses_visited'])
    en['total_minutes_visited'] = parse_float(en['total_minutes_visited'])
    en['lessons_completed'] = parse_float(en['lessons_completed'])
    en['projects_completed'] = parse_float(en['projects_completed'])
    print(en)

for submission in submissions:
    submission['creation_date'] = parse_date(submission['creation_date'])
    submission['completion_date'] = parse_date(submission['completion_date'])
    print(submission)

    
