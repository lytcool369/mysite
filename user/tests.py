from django.test import TestCase
import user.models as userModels



def test_userModel_insert(name, email, password, gender):
    userModels.insert(name, email, password, gender)


def test_userModel_login(email, password):
    userModels.fetchone(email, password)


# test_userModel_insert('마이콜', 'michol@gmail.com', '2345', 'male')
# test_userModel_login('dooly@gmail.com', '1234')