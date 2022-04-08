from collections import Counter


f = open("wordFile.txt", "r") #opens file for reading (Must manually change file name)
data = f.read() #reads file
words = data.split() #splits the data
counting = Counter(words) #counts each word
listWords = counting.most_common() #Finds most common word


print("Most Commonly used words in Text File: ","\n", counting.most_common()[0][0], "(", counting.most_common()[0][1], "times", ")"
,"\n", counting.most_common()[1][0], "(", counting.most_common()[1][1], "times", ")",
"\n", "and ", counting.most_common()[2][0], "(", counting.most_common()[2][1], "times", ")")
#print("Frequency of most commonly used word in Text File is => ", counting.most_common()[0][1])