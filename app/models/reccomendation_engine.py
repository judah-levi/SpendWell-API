import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

class ReccomendationEngine():

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    @staticmethod
    def get_rec_list(upc):
        rec_list = []

        julia = model(upc) #returns 3 objs

        rec_list.append(julia)
        return rec_list