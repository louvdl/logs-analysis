import psycopg2

#DBNAME = "news"

q1 = "What are the most popular three articles of all time?"
query1 = """create view artlog as select log.path, articles.slug, articles.title from log join articles on log.path ILIKE '%' || articles.slug; 
select title, count(*) as num from artlog group by title order by num desc limit 3;"""

q2 = "Who are the most popular article authors of all time?" 
query2 = """create view artlogauth as select articles.author, articles.slug, authors.id, authors.name, log.path from log join articles on log.path ILIKE '%' || articles.slug join authors on authors.id = articles.author;
select name, count(*) as numauth from artlogauth group by name order by numauth desc limit 3;"""

q3 = "On which days did more than 1% of requests lead to errors?"
query3 = """
with totalerrors as (select date(time) as day, count(*) as totalerrorsn from log where log.status='404 NOT FOUND' group by day
	), 
	totalperday as (select date(time) as day, count(*) as totalperdayn from log group by day
	)

select * from (
	select totalperday.day,
	round(cast((100*totalerrors.totalerrorsn) as numeric) / cast(totalperday.totalperdayn as numeric), 2) 
	as pcterrors
	from totalperday inner JOIN totalerrors ON totalperday.day = totalerrors.day)
as x where pcterrors > 1.0;"""

class Problem:
    def __init__(self):
        try:
            self.db = psycopg2.connect('dbname=news')
            self.cursor = self.db.cursor()
        except Exception as e:
            print e

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def solve(self, ques, query, suffix='views'):
        query = query.replace('\n', ' ')
        result = self.execute_query(query)
        print ques
        for i in range(len(result)):
            print '\t', i + 1, '.', result[i][0], '--', result[i][1], suffix
        # blank line
        print ''

    def exit(self):
        self.db.close()


if __name__ == '__main__':
    problem = Problem()
    problem.solve(q1, query1)
    problem.solve(q2, query2)
    problem.solve(q3, query3, '% error')
    problem.exit()
