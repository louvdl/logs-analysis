README

Logs Analysis
A Udacity FSND project.

About
This is the solution for the Logs Analysis project in Udacity Full Stack Nanodegree course. In this, we have to execute complex queries on a large database (> 1000k rows) to extract intersting stats.

The database in question is a newspaper company database where we have 3 tables; articles, authors and log.

articles - Contains articles posted in the newspaper so far.
authors - Contains list of authors who have published their articles.
log - Stores log of every request sent to the newspaper server.
This project implements a single query solution for each of the question in hand. See solution.py for more details.

Running
Set up
You will need: Python2, Vagrant, VirtualBox
Make sure you have newsdata.sql, the SQL script file with all the data. It can be downloaded from the Udacity course page.
Install Vagrant And VirtualBox
To Run
Launch Vagrant VM by running vagrant up, you can the log in with vagrant ssh
To load the data, use the command psql -d news -f newsdata.sql to connect a database and run the necessary SQL statements.
To execute the program, run python2 solution.py from the command line.

PSQL command used to create views:

create view artlog as select log.path, articles.slug, articles.title from log join articles on log.path ILIKE '%' || articles.slug; 
select title, count(*) as num from artlog group by title order by num desc limit 3

create view artlogauth as select articles.author, articles.slug, authors.id, authors.name, log.path from log join articles on log.path ILIKE '%' || articles.slug join authors on authors.id = articles.author;


