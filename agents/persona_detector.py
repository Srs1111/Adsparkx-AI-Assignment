def detect_persona(message):
    msg = message.lower()

    if any(word in msg for word in [
        "api",
        "authentication",
        "logs",
        "configuration",
        "error code",
        "error"
    ]): 
        return "Technical Expert"
    elif any (word in msg for word in [
        "angry",
        "frustrated",
        "nothing works",
        "urgent",
        "immediately"
    ]):
        return "frustrated User"
    
    return "Bussiness Excutive"