file1 = open('TolstoyLevVoynaIMirTom2.txt', 'r')
text = file1.readlines()
for word in text:
    print(word)

file2 = open('auxiliarypartofspeech.txt', 'r')
text1 = file2.readlines()
for word1 in text1:
    word2 = str(word1).encode('cp1251').decode('utf8')
    print(word2)

