from django.test import TestCase

class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.asssertEquals( 1+1, 3)
