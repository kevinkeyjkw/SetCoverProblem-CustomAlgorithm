Combinatorial Search
=========
This program solves the set cover problem in optimal time. The set cover problem
takes as input a collection S of m subsets of the universal set U={1,...,n}. The
goal is to find the smalled subset S' ∈ S such that the union of the subsets in S'
is U. So for example, if U = {1,2...,12} and S = {S1,S2,..,S6} where S1={1,2,3,4,5,6}
S2={5,6,8,9} S3={1,4,7,10} S4={2,5,7,8,11} S5 = {3,6,9,12} S6={10,11}
The minimum set cover for this set U would be S' = {S3,S4,S5}
This algorithm is written in Python. 
