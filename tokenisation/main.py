import tiktoken

enc= tiktoken.encoding_for_model("gpt-4")

text = "Hello, I am Sparsh Mahajan"

tokens = enc.encode(text)

print("Tokens:", tokens)
# Tokens: [9906, 11, 358, 1097, 70906,939, 16566, 97386]

decoded_text = enc.decode(tokens)
print("Decoded Text:", decoded_text)