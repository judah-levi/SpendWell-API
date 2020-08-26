import os
import psycopg2
from dotenv import load_dotenv, find_dotenv 
load_dotenv(find_dotenv())

DATABASE_URL = os.environ.get('DATABASE_URL')

class ReccomendationEngine():
    @staticmethod
    def get_rec_list(barcode):
        conn = psycopg2.connect(DATABASE_URL)
        columns = ['url', 'image_url', 'nutriscore_grade', 'label', 'barcode', 'category',
                   'subcategory', 'nutriscore', 'name', 'brand', 'ingredients']

        with conn.cursor() as cur:
            cur.execute('SELECT * FROM products2 WHERE barcode = %s;', [barcode])
            prev_result = cur.fetchone()
        prev_prod = {}
        for i, col in enumerate(columns):
            prev_prod[col] = prev_result[i + 1]

        with conn.cursor() as cur:
            cur.execute('SELECT label FROM products2 WHERE barcode = %s;', [barcode])
            result = cur.fetchall()
            cur.execute('SELECT * FROM products2 WHERE label = %s order by nutriscore DESC limit 3;', [result[0][0]])
            result = cur.fetchall()

        list_of_dicts = []
        for j in range(len(result)):
            res_dict = {'before_nutriscore':prev_prod['nutriscore']}
            for i, col in enumerate(columns):
                res_dict[col] = result[j][i+1]
            list_of_dicts.append(res_dict)

        return list_of_dicts

