import unittest
from survey import AnnymousSurvey

class TestAnnymousSurvey(unittest.TestCase):
    # def test_store_single_response(self):
        # question="what  language did you first learn to speak?"
        # my_survey=AnnymousSurvey(question)
        # my_survey.store_responses('English')

        # self.assertIn('English',my_survey.responses)
    def setUp(self):
        question="what language did you first learn to speak?"
        self.my_survey=AnnymousSurvey(question)
        self.responses=['English','Spanish','Mandarin']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_single_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)      

unittest.main()