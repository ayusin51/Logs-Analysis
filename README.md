# LOG ANALYSIS

## About

This is the project of Full Stack NanoDegree. This project includes 3 tables 
- articles
- authors
- log
 with a number of rows by SQL queries. This database contains the data of articles read, authors of the articles and web server log for the newspaper site.

## Prerequisites

- Python3
- Vagrant
- VirtualBox

## Installing

- Install Vagrant and VirtualBox, or
- Clone this repository.

## Downloading

- Download the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file and load the data.


## Running the tests

- Launch Vagrant VM by running :
	`vagrant up`
- Log in with :
	`vagrant ssh`

- Load the data into database named news , use the command :
	`psql -d news -f newsdata.sql`

- Connect to databse, run the command :
	`psql -d news`.

- Create a view , use the command :
	`psql -d news`
and then run the SQL statement as mentioned below.

- SQL query for creating view: CREATE VIEW percent_error_view:
```
CREATE VIEW percent_error_view AS SELECT date(time),
round(100.00*sum(CASE WHEN status = '404 NOT FOUND'
THEN 1 ELSE 0 END) / count(log.status),2)
AS PercentError FROM log GROUP BY date(time) ORDER BY PercentError DESC;
```

- To execute the program, run the following command :
	`python3 news.py`

