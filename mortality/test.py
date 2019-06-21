# from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase  #, APIClient
from mortality.models import Cause

# NOTE: Normally I would have this nested in a directory called "tests" and possibly name this file something else like
# test_api or similar so that when you run the tests in the command line you know which file youre using and which
# app you are testing specifically.

class MortalityApiTestCase(APITestCase):
    def setUp(self, *args, **kwargs):
        # self.client = APIClient()
        # self.client.credentials(
        #     HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key
        # )
        #  something like this would be useful for multiple client testing (checking auth/non-auth requests)
        return super(MortalityApiTestCase, self).setUp(*args, **kwargs)

    def tearDown(self):
        super(MortalityApiTestCase, self).tearDown()

class CauseApiTestCase(MortalityApiTestCase):

    def setUp(self, *args, **kwargs):
        self.list_url = reverse('cause-list')
        return super(CauseApiTestCase, self).setUp(*args, **kwargs)

    def test_list(self):
        cause_obj = Cause.objects.create(
            state_code='48',
            state_name='Texas',
            county_code='15',
            county_name='Austin',
            strata_id='40',
            injury='11',
            cancer='22',
            homicide='33',
            suicide='44',
            hiv='55',
            time_span='1988-2099',
        )
        # to create a new object, I can also use a factory to simulate a new object instead of having to use the setup
        # object or creating more from scratch
        self.assertEqual(cause_obj.state_name, 'Texas')
        self.assertEqual(cause_obj.injury, '11')
        self.assertEqual(cause_obj.suicide, '44')

        res = self.client.get(self.list_url, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK, msg=res.data)
        count = len(res.data)
        self.assertEqual(count, 1)  # better way to do this is generate a "count" field
        self.assertEqual(res.data[0]['county_name'], cause_obj.county_name)
        self.assertEqual(res.data[0]['state_name'], cause_obj.state_name)
        self.assertEqual(res.data[0]['strata_id'], cause_obj.strata_id)

        # there is also a use case for sub tests here if you wanted to test all the fields
        # or if there were plenty of objects to test.
        # https://hackernoon.com/the-best-new-feature-in-unittest-you-didnt-know-you-need-e0d26c213dce
