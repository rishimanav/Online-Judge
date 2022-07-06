# from tkinter import CASCADE
from django.db import models
from django.forms import CharField
from django.utils import timezone


# 'user_id' serves as the primary key identifying a user
# 'score' field stores the cumulative score of a user (score increases by solving problems)
# 'rank' rank of the user
# 'subs' stores the number of submissions stored by the user
class User_Data(models.Model):
    user_id=models.CharField(max_length=30, primary_key=True)
    score = models.IntegerField()
    rank = models.IntegerField()
    subs = models.IntegerField()

tags=[
    ('Arrays', 'Array'), 
    ('Matrices', 'Matrices'), 
    ('Searching', 'Searching'),
    ('Sorting', 'Sorting'),
    ('Hashing', 'Hashing'),
    ('LinkedList', 'LinkedList'),
    ('Stacks', 'Stacks'),
    ('Queues', 'Queues'),
    ('Trees', 'Trees'),
    ('Graphs', 'Graphs'),
    ('Greedy', 'Greedy'),
    ('D&C', 'Divide&Conquer'),
    ('DP', 'Dynamic Programming'),
]

difficulty=[
    (1, 'Easy'),
    (2, 'Moderate'),
    (3, 'Hard')
]

# 'prob_id' serves as the primary key identifying a problem
# 'topic' field is used to insert tags. Multiple tags can be applied to a problem. 
# 'name' contains the title of the problem
# 'level' stores the difficulty level of the problem. 
# 'crr_sub' contains the number of correct submissions to the problem
# 'total_sub' conatins the total number of submissions to the problem
class Problem(models.Model):
    prob_id=models.IntegerField(primary_key=True) 
    topic = models.CharField(max_length=10, choices=tags)
    name = models.CharField(max_length=50)
    level = models.IntegerField(choices=difficulty, default=1)
    crr_sub= models.IntegerField()
    total_sub= models.IntegerField()
    
    
    
    # pub_date = models.DateTimeField('date published')

    # def __str__(self):
    #     return self.question_text
    
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

languages=[
    ('cpp', 'C++'),
    ('python', 'python')
]

result=[
    ('RTE', 'RunTimeError'), 
    ('CE', 'CompilationError'),
    ('Success', 'Success')
]

# (user_id, prob_id, sub_time) is the primary key
# 'user_id' and 'prob_id' are foreign keys
# 'code' takes the input code
# 'lang' stores the language the code is written in
# 'verdict' stores the result of each submission
# 'sub_time' records the timestamp of submission
class Submission_Log(models.Model):
    user_id = models.ForeignKey(User_Data, on_delete=models.CASCADE)
    prob_id = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    lang = models.CharField(max_length=6, choices=languages)
    verdict = models.CharField(max_length=7, choices=result)
    sub_time=models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.choice_text


# 'prob_id' acts as foreign key
# 'input' conatins the input values of the test case
# 'output' conatins the output values of a test case
class Test_Case(models.Model):
    prob_id=models.ForeignKey(Problem, on_delete=models.CASCADE)
    input=models.TextField()
    output=models.TextField()