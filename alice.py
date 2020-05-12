filename='alice.txt'
try:
    with open(filename) as f_obj:
        contents=f_obj.read()
except FileNotFoundError:
    msg="sorry,the file " + filename + "dose not exist."
    print(msg)
else:
    words=contents.split()
    num_words=len(words)
    print("the file " + filename + "has about " + str(num_words) + "words.")