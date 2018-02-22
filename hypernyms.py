from nltk.corpus import wordnet



ar1 = wordnet.synsets('mom')
ar2 = wordnet.synsets('parents')
ar3 = wordnet.synsets('father')


#Hypernyms


#print(ar1)
#print(ar2)
#print(ar3)

ammu = ar1[0]
parent = ar2[0]
abbu = ar3[0]

print(ammu.hypernyms())
print(abbu.hypernyms())
print(parent.hypernyms())


reference_node = ammu.hypernyms()[0]

print(ammu.shortest_path_distance(reference_node))
      


