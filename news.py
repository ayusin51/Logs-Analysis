#!/usr/bin/env python3

import psycopg2
dbname = "news"

# 1. Top three populor articles of all the time!
query1 = """SELECT articles.title, count(*) AS views FROM articles,
log WHERE SUBSTRING(log.path,10) = articles.slug AND
log.status LIKE '%200%' GROUP BY articles.title ORDER
BY views DESC LIMIT 3"""

# 2. The most popular article authors are!
query2 = """SELECT authors.name,count(*) AS total_views FROM articles,
authors,log WHERE authors.id = articles.author AND SUBSTRING
(log.path,10) = articles.slug AND log.status LIKE '%200%'
GROUP BY authors.name ORDER BY  total_views DESC"""

# 3. Days when the requests lead to an error more than 1%!
query3 = "SELECT * FROM percent_error_view  WHERE PercentError >= 1"

ques1 = dict()
ques2 = dict()
ques3 = dict()

ques1['title'] = "1. The most popular three articles of all time :"
ques2['title'] = "2. The most popular article authors of all time :"
ques3['title'] = "3. Days when the requests lead to an error more than 1% :"

def run_query(query):
	db = psycopg2.connect(database=dbname)
	c = db.cursor()
	c.execute(query)
	result = c.fetchall()
	db.close()
	return result

def print_res(ques):
	print('\n' + ques['title'] + '\n\n')
	for row in ques['result']:
		print(str(row[0]) + ' : ' + str(row[1]) + '\n')
	print('\n')

if __name__ == '__main__':
	# running the queries
	ques1['result'] = run_query(query1)
	ques2['result'] = run_query(query2)
	ques3['result'] = run_query(query3)
	
	# print result of queries
	print_res(ques1)
	print_res(ques2)
	print_res(ques3)
	
