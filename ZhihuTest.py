# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function
import os
from zhihu_oauth import ZhihuClient
from bosonnlp import BosonNLP
import csv
import requests

# 注意：在测试时请更换为您的API Token
HEADERS = {'X-Token': 'OTuvKfuf.21693.XmTG0VoB_QPA'}
RATE_LIMIT_URL = 'http://api.bosonnlp.com/application/rate_limit_status.json'
result = requests.get(RATE_LIMIT_URL, headers=HEADERS).json()
print(result)
nlp = BosonNLP('OTuvKfuf.21693.XmTG0VoB_QPA')
TOKEN_FILE = 'token.pkl'

client = ZhihuClient()
#--------LOG IN------------#
if os.path.isfile(TOKEN_FILE):
    client.load_token(TOKEN_FILE)
else:
    client.login_in_terminal()
    client.save_token(TOKEN_FILE)
#----------------------------
me = client.me()
print('name', me.name)
questions = me.following_questions
i = 0
bad_list = []
bad_dict = {}
good_list = []
good_dict = {}
# for question n questions:
#48348438
question = client.question(48348438)
print(question.title)
answers = question.answers
for answer in answers:
    if answer.thanks_count == 0 or answer.comment_count == 0:
        pass
    else:
        if answer.voteup_count/answer.comment_count < 1:
            bad_list.append(answer)
            good_comments = 0
            bad_comments = 0
            comments = answer.comments
            for comment in answer.comments:
                print(comment.content)
                result = nlp.sentiment(comment.content)
                print(result)
                try:
                    if result[0][0]<result[0][1]:
                        print('maybe a bad comment')
                        bad_comments += 1
                    else:
                        print('maybe a good comment')
                        good_comments += 1
                except:
                    pass
            bad_dict[answer.voteup_count/answer.comment_count] = [good_comments,bad_comments]
        elif answer.voteup_count/answer.comment_count > 5:
            good_list.append(answer)
            good_comments = 0
            bad_comments = 0
            comments = answer.comments
            for comment in answer.comments:
                print(comment.content)
                result = nlp.sentiment(comment.content)
                try:
                    if result[0][0]<result[0][1]:
                        print('maybe a bad comment')
                        bad_comments += 1
                    else:
                        print('maybe a good comment')
                        good_comments += 1
                except:
                    pass
            good_dict[answer.voteup_count/answer.comment_count] = [good_comments,bad_comments]

badf = open('bad.csv','w')
badf.write("VOTE/COMMENT, GOOD SCORE, BAD SCORE")
for score in bad_dict.keys():
    badf.write('"{}","{}","{}"\n'.format(score,bad_dict[score][0],bad_dict[score][1]))

goodf = open('good.csv','w')
goodf.write("VOTE/COMMENT, GOOD SCORE, BAD SCORE")
for score in good_dict.keys():
    goodf.write('"{}","{}","{}"\n'.format(score,good_dict[score][0],good_dict[score][1]))
