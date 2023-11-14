import processing_modules.get_data as GetData
from fuzzywuzzy import fuzz

import re
from typing import List
def parsing(body: str, subject: str, sender: str, to: List[str], cc: List[str]):
  query = f"""SELECT o.id, p.name, sum(CASE WHEN s.status = 'shipped' THEN 1 ELSE 0 END) is_delivered
  FROM client c 
  JOIN orders o on c.id = o.client_id
  JOIN status s on o.id = s.order_id
  JOIN product p on p.id = o.product_id
  WHERE c.email = 'alex.martin@email.com'
  GROUP BY o.id, p.name
  """
  products = GetData.sql("achats_db", query)
  products = [(fuzz.partial_ratio(body.lower(), p[1]),  *p ) for p in products ]
  order_id, product, is_shipped= max(products, key=lambda x:x[0])[1:]
  
  # Get sender name,
  query = f""" select first_name
  from client where email = {'alex.martin@email.com'!r}
  """
  first_name = GetData.sql("achats_db", query)[0][0]
  
  return {'order_id': order_id,
        'product': product,
        'is_shipped': is_shipped,
        'first_name': first_name}
