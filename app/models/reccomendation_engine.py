import os
import psycopg2
from dotenv import load_dotenv, find_dotenv 
load_dotenv(find_dotenv())

DATABASE_URL = os.environ.get('DATABASE_URL')


class ReccomendationEngine():
    @staticmethod
    def get_rec_list(barcode):
        print(DATABASE_URL)
        conn = psycopg2.connect(DATABASE_URL)
        with conn.cursor() as cur:
            cur.execute('SELECT label FROM products WHERE barcode = %s;', [barcode])
            result = cur.fetchall()
            cur.execute('SELECT * FROM products WHERE label = %s order by nutriscore DESC limit 3;', [result[0][0]])
            result = cur.fetchall()

        list_of_dicts = []
        columns = ['url', 'image_url', 'nutriscore_grade', 'label', 'barcode', 'category',
       'subcategory', 'nutriscore', 'name', 'brand', 'ingredients']
        for j in range(len(result)):
            res_dict = {}
            for i, col in enumerate(columns):
                res_dict[col] = result[j][i+1]
            list_of_dicts.append(res_dict)

        return list_of_dicts