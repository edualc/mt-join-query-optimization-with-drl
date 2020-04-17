import psycopg2
from helper.paths import get_queries
from helper.database_connection import postgres_connection

conn = psycopg2.connect(**postgres_connection())
cursor = conn.cursor()

sql_query = list(open(get_queries('crossval_sens/job_queries_simple_crossval_0_test.txt')))

subquery = sql_query[3]

subquery = "SELECT * FROM company_name, movie_companies WHERE company_name.id = movie_companies.company_id LIMIT 10"

cursor.execute(subquery)


cursor.fetchone()

test = cursor.fetchall()

for row in test:
    print("Id = ", row[1], )