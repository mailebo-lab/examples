from typing import List
import uuid


def processing(body: str, subject: str, sender: str, to: List[str], cc: List[str], extraction: dict):
    order_id = extraction['order_id']
    product = extraction['product']
    is_shipped = extraction['is_shipped']
    first_name = extraction['first_name']
    
    if is_shipped == 0:
      
      ActionTools.reply(f"""Bonjour {first_name},
      
Nous avons bien pris en compte votre demande d'annulation de la commande N° {order_id}: {product!r}
      
Cordialement,
Service client""")
      query = f"""
INSERT INTO status (id, order_id, status, status_date )
VALUES ({str(uuid.uuid4())!r}, {order_id!r}, 'Canceled', DATE('now') ) ;"""
      ActionTools.sql_modify_data('achats_db', query)
    else :
      ActionTools.reply(f"""Bonjour {first_name},
      
Nous avons bien reçu votre demande, cependant votre colis est en cours d'acheminement, quand vous le recevez veuillez nous le renvoyer et on procedera au remboursement.

Service client""")
    return None
