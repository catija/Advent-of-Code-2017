


myfile = open("adventday4input.txt", mode='r')

count = 0
invalidcount = 0

for line in myfile.readlines():
    count += 1
    print(line.strip())

    wordcount = 0
    bucket = []
    for word in line.split():
        wordcount += 1
        if word in bucket:
            invalidcount += 1
            print("Dupe!")
            break
        else:
            bucket.append(word)

    print("Wordcount = {}, Bucket = {}".format(wordcount, bucket))
    print()
validcount = count - invalidcount
print("Out of {} total lines, {} were valid passphrases and {} were invalid passphrases.".format(count, validcount, invalidcount))
