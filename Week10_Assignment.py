name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"

fileHandler = open(name)


lstOfWords = list()
# for comprehension for "lstOfWords: List[String]"
for line in fileHandler:
    if not line.startswith("From "): continue
    words = line.split()
    lstOfWords.append(words[5])

    
counts = dict()
# for comprehension for counts.get() Python Dictionary function --> https://www.w3schools.com/python/ref_dictionary_get.asp
for word in lstOfWords:
    hour = word.split(':')
    counts[hour[0]] = counts.get(hour[0], 0) + 1
    
# for comprehension for sorting the key (in ascending order)
for key, val in sorted(counts.items()):
    print(key, val)
