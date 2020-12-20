import codecs
import re
if __name__ == "__main__":
    file1 = codecs.open('TolstoyLevVoynaIMirTom2.txt', 'r', encoding='cp1251', errors='ignore')
    text = file1.read()
    file2 = codecs.open('auxiliarypartofspeech.txt', 'r', encoding='utf8', errors='ignore')
    text1 = [word.strip() for word in file2.readlines()]
    text1 = text1
    for word in text1:
        text = re.sub(rf"\b{word.lower()}\b", "", text)
        text = re.sub(rf"\b{word.upper()}\b", "", text)
 
    print(text)
    file3 = open('ClearTolstoyLevVoynaIMirTom2.txt', 'w')
    file3.write(text)
    file3.close()
