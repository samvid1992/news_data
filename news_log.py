#!/usr/bin/env python3

import psycopg2


def show_popular_articles(conn):
	query = """SELECT t1.title, t2.views FROM articles AS t1,
	(SELECT replace(path, '/article/', '') AS slug, 
	count(*) AS views FROM log WHERE status = '200 OK' 
	AND path LIKE '/article/%' GROUP BY path ORDER BY views DESC) 
	AS t2 WHERE t1.slug = t2.slug LIMIT 3"""
	cur = conn.cursor()
	cur.execute(query)
	for row in cur.fetchall():
		print('  - "%s"  -- %d views' % (row[0], row[1]))
	cur.close()


def show_popular_authors(conn):
	query = """SELECT authors.name, t.total_views FROM authors,
	(SELECT t1.author, SUM(t2.views) AS total_views FROM articles AS t1,
	(SELECT replace(path, '/article/', '') AS slug, 
	count(*) AS views FROM log WHERE status = '200 OK' 
	AND path LIKE '/article/%' GROUP BY path) AS t2 
	WHERE t1.slug = t2.slug GROUP By author ORDER BY total_views DESC) 
	AS t WHERE authors.id = t.author"""
	cur = conn.cursor()
	cur.execute(query)
	for row in cur.fetchall():
		print("  - %s  -- %d views" % (row[0], row[1]))
	cur.close()


def show_days_with_errors(conn):
	query = """SELECT to_char(t3.date, 'Month dd, yyyy'),
	t3.err_rate FROM (SELECT t1.date, 
	round(((CAST(t1.c AS DECIMAL) * 100)/t2.c),2) 
	AS err_rate FROM (SELECT CAST(time AS DATE) AS date, 
	count(*) AS c FROM log WHERE status != '200 OK' GROUP BY date) AS t1,
	(SELECT CAST(time AS DATE) AS date, count(*) AS c FROM log GROUP BY date) 
	AS t2 WHERE t1.date = t2.date)
	AS t3 WHERE t3.err_rate > 1 ORDER BY t3.err_rate DESC;"""
	cur = conn.cursor()
	cur.execute(query)

	for row in cur.fetchall():
		print("  - %s   --  %.2f%% errors" % (row[0], row[1]))

	cur.close()




if __name__ == "__main__":
	with psycopg2.connect("dbname=news") as conn:
		print("Top 3 popular articles:")
		show_popular_articles(conn)

		print("\nPopular authors:")
		show_popular_authors(conn)

		print("\nDays with more than 1% error rate:")
		show_days_with_errors(conn)
