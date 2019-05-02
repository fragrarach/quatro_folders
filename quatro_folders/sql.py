import psycopg2.extensions
from sigm import sql_query, tabular_data


# PostgreSQL DB connection configs
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


# Pull 'cli_id' record from 'order_header' table based on 'ord_no' record
def all_ord_nos(cursor):
    sql_exp = f'SELECT ord_no FROM order_header'
    result_set = sql_query(sql_exp, cursor)
    ord_nos = tabular_data(result_set)
    return ord_nos