
# Create dictionary out of sentence with values being length of each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
results = {k: len(k) for k in sentence.split()}
print(results)