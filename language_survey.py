from survey import AnnymousSurvey

question="what language did you first learn to speak?"
my_survey=AnnymousSurvey(question)

my_survey.show_question()
print("enter 'q' at any time to quit.\n")
while True:
    response=input("language: ")
    if response=='q':
        break
    my_survey.store_responses(response)
print("\nthank you to everyone who participated in the survey!")
my_survey.show_results()