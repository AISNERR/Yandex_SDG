sentence = ['this','is','a','sentence']
sent_str = ""
for i in sentence:
    sent_str += str(i)
sent_str = sent_str
print(sent_str)
tr = [[1, 2], [1, 2]]
print("\n".join(map(lambda y: ", ".join(y), tr)))