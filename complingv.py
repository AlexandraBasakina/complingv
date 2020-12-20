
file1 = open('TolstoyLevVoynaIMirTom2.txt', 'r')
text = file1.readlines()
print(text)
file2 = open('auxiliarypartofspeech.txt', 'r')
text1 = file2.readlines()
for word in text1:
    word1 = word.decode('utf8')
    print(word1)
file3 = open('rom.txt', 'w')

file3.close()
