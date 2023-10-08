from pyDatalog import pyDatalog 
pyDatalog.create_terms('father,brother,cousin,grandson,decendent,X,Y,Z,Z1,Z2')

+father('a','b')
+father('a','c')
+father('b','d')
+father('b','e')
+father('c','f')
brother(X,Y)<=father(Z,X) & father(Z,Y) & (X!=Y)
cousin(X,Y)<=father(Z1,X) & father(Z2,Y) & brother(Z1,Z2)
grandson(X,Y)<=father(Y,Z) & father(Z,X)
decendent(X,Y)<=father(Y,X)
decendent(X,Y)<=father(Z,X) & decendent(Z,Y)
print(brother(X,Y)) 
print(grandson(X,Y))