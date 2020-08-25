import os
import psycopg2

# DATABASE_URL = os.environ['DATABASE_URL']
DATABASE_URL ='postgres://qcsfswwzpmpnoe:c79186b0b2d5cdb40b41ff40d914a4d2c0f8285529274f16fad2384fcb1a9465@ec2-54-247-103-43.eu-west-1.compute.amazonaws.com:5432/d9nkgr3sa7opsa'

class ReccomendationEngine():
    @staticmethod
    def get_rec_list(upc):
        conn = psycopg2.connect(DATABASE_URL)
        with conn.cursor() as cur:
            cur.execute('SELECT label FROM products WHERE barcode = %s;', [upc])
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