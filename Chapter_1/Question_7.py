def custom_encoder(text):
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for char in text.lower():
        if char in reference_string:
            result.append(reference_string.index(char))
        else:
            result.append(-1)
    return result