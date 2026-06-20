def should_escalate(query, docs):

    if len(docs) == 0:
        return True 
    
    sensitive = [
        "billing",
        "legal",
        "refund",
        "account",
        "payment"
    ]
    

    if any(word in query.lower() 
           for word in sensitive):
        return True 
    
    return False