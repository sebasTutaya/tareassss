l1 = [("one",1),("two",2),("three",3),("four",4),("five",5)]
l2 = [("one",1),("two",2),("six",6)]

#crear conjuntos
s1 = set(l1)
s2 = set(l2)
#elementos comunes
s3 = s1.intersection(s2)
print("la interseccion es: ", s3)
#elementos unicos
s4 = s1.symmetric_difference(s2)
print("elementos unicos: ", s4)
#lista nueva
l3 = s3.union(s4)
print(sorted(l3))
