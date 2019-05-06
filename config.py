import psycopg2.extensions
from sigm import sigm_connect, log_connect, dev_check


# PostgreSQL DB connection configs
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


class Config:
    LISTEN_CHANNEL = 'folders'

    SIGM_CONNECTION, SIGM_DB_CURSOR = sigm_connect(LISTEN_CHANNEL)
    LOG_CONNECTION, LOG_DB_CURSOR = log_connect()

    DOC_DIR = r'Z:\SIGMWIN.DTA\DEV\Documents' if dev_check() else r'E:\DATA\Fortune\SIGMWIN.DTA\QuatroAir\Documents'