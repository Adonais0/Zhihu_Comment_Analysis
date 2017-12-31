# Zhihu Comment Analysis
----
## Question
If an answer has more comments than voteups, what does that potentially mean?

## Library
1. [Zhihu_oauth](https://github.com/7sDream/zhihu-oauth)
2. [Boson NLP](https://bosonnlp.com/)

## Process
1. Use zhihu-oauth to log in
2. Choose an interesting question with an amount of answers
3.  Pick out the answers with
 * more commets than voteups
 * voteup_counts is five times more than comments
4.  Use Boson NLP emotional module to analyze the emotional tendency of each comment of the picked answers


## CSV
Each csv file has three columns:  

 * VOTE/COMMENT: shows the rate of voteup/comments
 * GOOD SCORE: the number of comments that has higher good tendency than bad tendency [Explanation](http://docs.bosonnlp.com/getting_started.html)
 * BAD SCORE: the number of comments that has lower good tendency than bad tendency

## Discussion
* I chose a question with more than 2000 answers, but the amount of picked out answers is only around 40. The sample size is too small to make scientific analysis.
* Bonson NLP emotional analysis module is not so accurate because of the complexity of Chinese language.
