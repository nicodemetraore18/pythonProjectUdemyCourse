from hashlib import sha1
text = input ("password please:")
hash_of_text=sha1(text.encode())
print(hash_of_text.hexdigest())
