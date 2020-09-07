from django.test import TestCase
import guestbook.models as guestbookModel


def list():
    results = guestbookModel.list()

    return results


print(list())