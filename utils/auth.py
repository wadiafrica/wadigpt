def fetch_user(uid: str):
    try:
        return uid.replace("-", " ").capitalize()
    except Exception as e:
        return ""
