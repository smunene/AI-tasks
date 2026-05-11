% Simple family tree
parent(john, jane).   % John is a parent of Jane
parent(jane, ann).
parent(jane, jerry).

male(john).
male(jerry).
female(jane).
female(ann).

grandparent(GP, GC) :- 
    parent(GP, P), 
    parent(P, GC).

sibling(X, Y) :- 
    parent(P, X), 
    parent(P, Y), 
    X \= Y.

grandchild(GC, GP) :- 
    grandparent(GP, GC).


% Large family tree
parent(joe, mary).    
parent(joe, naf).    
parent(mary, fran).     
parent(mary, tom).     
parent(naf, saul).    

male(joe).
male(naf).
male(tom).
male(saul).
female(mary).
female(fran).

grandparent(GP, GC) :- 
    parent(GP, P), 
    parent(P, GC).

grandchild(GC, GP) :-
    grandparent(GP, GC).

sibling(X, Y) :- 
    parent(P, X), 
    parent(P, Y), 
    X \= Y.

uncle(U, C) :-
    parent(P, C),
    sibling(U, P),
    male(U).

aunt(A, C) :-
    parent(P, C),
    sibling(A, P),
    female(A).

cousin(CO, C) :-
    parent(P, C),
    sibling(S, P),
    parent(S, CO).