import hashlib


# sample encryption function showing condensed usage of SHA 256 encryption algorythm
def sha_256_encrypt(my_string):

    # encode() function used rather than update() function for lower-level string conversion to the byte-stream
    encoded_string = my_string.encode()

    # sha256() constructor selected to create SHA-256 hash object
    encrypted_string = hashlib.sha256(encoded_string)

    # hexdigest() function used rather than digest() function to assure safe hash transfer via non-binary environments
    safe_sha256 = encrypted_string.hexdigest()

    return safe_sha256


string_sample = input("Input text for SHA 256 encryption: ")
encrypted_input = sha_256_encrypt(string_sample)
print("Encrypted input: " + encrypted_input)
