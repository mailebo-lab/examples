from typing import List
def detection(body: str, subject: str, sender: str, to: List[str], cc: List[str]):
    condition = "annul" in body.lower() and "commande" in body.lower()
    return condition
