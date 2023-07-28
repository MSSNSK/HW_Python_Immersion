from statistics import mean
import descriptors as des


class Student:
    first_name = des.CheckName()
    last_name = des.CheckName()
    middle_name = des.CheckName()
    subject = des.CheckSubject('students.csv')
    subject_score = des.CheckSubjectScore(min_sub_score=2, max_sub_score=5)
    test_score = des.CheckTesttScore(min_test_score=0, max_test_score=100)
    subjects = []

    def __init__(self, first_name, last_name, middle_name, subject, subject_score, test_score):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.subject = subject
        self.subject_score = subject_score
        self.test_score = test_score
        self._update_subjects()

    def add_subject(self, subject, subject_score, test_score):
        self.subject = subject
        self.subject_score = subject_score
        self.test_score = test_score
        self._update_subjects()

    def _update_subjects(self):
        self.subjects.append({
            'subject': self.subject,
            'subject_score': self.subject_score,
            'test_score': self.test_score,
        })

    def get_avg(self):
        avg_sub_score = mean(score['subject_score'] for score in self.subjects)
        avg_test_score = mean(score['test_score'] for score in self.subjects)
        return f"""Предметы студента: {', '.join([sub['subject'].title() for sub in self.subjects])}
Средний бал по урокам: {avg_sub_score}
Средний бал по тестам: {avg_test_score}\n"""
