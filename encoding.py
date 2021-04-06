a="chiragjuneja"

byte_form = b'chiragjuneja'

byte_encoded_form = a.encode('ASCII')

if byte_encoded_form == byte_form:
    print("encoding success")
else:
    print("encoding failed")

