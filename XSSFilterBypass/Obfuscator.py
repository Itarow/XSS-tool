


def to_char_code(payload):
    encoded = []
    for char in payload:
        encoded.append(ord(char))

    encoded = ','.join(str(i) for i in encoded)
    return f"</script>String.fromCharCode({encoded})</script>"


