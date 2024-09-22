def get_consonants(text):
    try:
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        # Ekstrak konsonan dari teks
        result = {char for char in text if char in consonants}
        return result
    except TypeError as e:
        raise Exception(f"Error: Invalid input type. {e}")