#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Find the time complexity of the following pseudo-code
#write pseudo this code so it will run
# reference https://peteroupc.github.io/pseudocode.html

#1)
#a)
int a = 0 , b = 0;
for ( i = 0; i < N ; i ++) {
a = a + rand () ;
 }
#for i in a, if i < any real number, add 1 to i. else, a = a + a random number.  

#using the same two integers:
#b)
for ( j = 0; j < M ; j ++) {
b = b + rand () ;
}
#this for loop says for j=0, if j<M (M being?), then add 1 to j. else, b = b + random number


# In[7]:


#1)
#a) answer

a=0 #are these meant to just be 0? they are not iterable as just 0.
b=0
c={} #make an empty tuple
for i in a:
    if i<[num for num in range (n)]: #if i in a is less than a real number in range n, add 1 to i
        i=i+1
    else:
        i=i+random.randint() #else, add a random number to i  
c.append(i)
head(c)

#To generate a list of n numbers, the following syntax is used: [num for num in range (n)]. 
#This will create a list of numbers starting at 0 and going up to (n-1). start=1 end=10
    
#random.randint() function returns an integer value(random) 
#between the starting and ending point entered in the function. 
#This function is inclusive of both the endpoints entered.

#b) answer

for i in b:
    if i<[num for num in range (n)]:
        i=i+1
    else:
        i=i+random.randit()


# In[ ]:


#2)

int l , t , k = 0;   #three integers
for ( l = n / 2; l <= n ; l ++) {   #when l = n/2, if l is smaller than or equal to n, add 1 to l. 
for ( t = 2; t <= n ; t = t * 2) {  #when t =2, if t is smaller than or equal to 2, multiply t by 2.
k = k + n / 2;   #this is carried out after the above operations. 
}
 }


# In[15]:


#2) answer

l={}
t={}
k=0
n= range(1, 1000001) #represent a container with all integers from 1 to a million with range
1 in n
1000000 in n
0 in n

for i in l:
    i=n/2
    for i in l:
        if i<=n:
            i=i+1
            


# In[ ]:


#3)

int a = 0 , i = N ; #there are two integers a and i. i is any real number.  
while ( i > 0) {   #this says while i is larger than 0,
a += i ;#add the value to the right of the operator to the value on the left of the operator, the result replaces the value of the variable
i /= 2; #this just means divide i by 2    
}


# In[ ]:


#3) answer

a=0
n= range(1, 1000001) #represent a container with all integers from 1 to a million with range
1 in n
1000000 in n
0 in n

for i in n:
    while i>0: #while i in n =0,
        i=i+n #add a number in n to i #replace the variable with this new number?
        i/2 #then divide i by 2


# In[ ]:


Given an array of numbers, find the GCD of the array elements (Hint: Use the Euclidean algorithm
discussed in the lecture)
● Example Input
○ arr[] = {1, 2, 3}
● Output:
○ 1
● Example Explanation
○ The GCD of three or more numbers equals the product of the prime factors common to all the
numbers.

#pseudo code of gcd algorithm
function gcd(a, b)
    while b ≠ 0
       t := b
       b := a mod b
       a := t
    return a




#One trick for analyzing the time complexity of Euclid's algorithm 
#is to follow what happens over two iterations:

a', b' := a % b, b % (a % b)
    
#Now a and b will both decrease, instead of only one, which makes 
#the analysis easier. You can divide it into cases:

Tiny A: 2a <= b
Tiny B: 2b <= a
Small A: 2a > b but a < b
Small B: 2b > a but b < a
Equal: a == b

#Now we'll show that every single case decreases the total a+b by at 
#least a quarter:

Tiny A: b % (a % b) < a and 2a <= b, so b is decreased by at least half, so a+b decreased by at least 25%
Tiny B: a % b < b and 2b <= a, so a is decreased by at least half, so a+b decreased by at least 25%
Small A: b will become b-a, which is less than b/2, decreasing a+b by at least 25%.
Small B: a will become a-b, which is less than a/2, decreasing a+b by at least 25%.
Equal: a+b drops to 0, which is obviously decreasing a+b by at least 25%.
    
#Therefore, by case analysis, every double-step decreases a+b by at 
#least 25%. There's a maximum number of times this can happen 
#before a+b is forced to drop below 1. The total number of 
#steps (S) until we hit 0 must satisfy (4/3)^S <= A+B. Now just work it:

(4/3)^S <= A+B
S <= lg[4/3](A+B)
S is O(lg[4/3](A+B))
S is O(lg(A+B))
S is O(lg(A*B)) //because A*B asymptotically greater than A+B
S is O(lg(A)+lg(B))
(/Input, size, N, is, lg(A), +, lg(B))
S is O(N)

#So the number of iterations is linear in the number of input digits.
# For numbers that fit into cpu registers, it's reasonable to model 
#the iterations as taking constant time and pretend that the total 
#running time of the gcd is linear.

#Of course, if you're dealing with big integers, you must account 
#for the fact that the modulus operations within each iteration 
#don't have a constant cost. Roughly speaking, the total asymptotic 
#runtime is going to be n^2 times a polylogarithmic factor. 
#Something like n^2 lg(n) 2^O(log* n). The polylogarithmic factor 
#can be avoided by instead using a binary gcd.


# In[ ]:


The biological challenge we will work on for this homework is Restriction Mapping. For a more detailed
explanation of the methods, please see this link: https://www.ncbi.nlm.nih.gov/books/NBK21116/#A6269
        
What we have: A collection of Sequences of varying lengths from different parts of, let’s say, a chromosome.
    
What we want to do: Determine which two sequences span the entire chromosome. We want the two
fragments to overlap a little but not too much because it would be a waste of resources.
Restriction enzymes can cut/digest at specific sites. In normal applications, multiple restriction enzymes are
used, separately and in combination, to cut DNA into smaller pieces. The pieces of DNA are then run on a gel
that separates the fragments based on size.
The figure below shows the result of running the fragments in the gel.
Develop an algorithm that will allow you to assemble the sequence based on the fragments provided so we
know how they are related ( how they overlap ). After determining the relationship of the sequences, determine
which two sequences span the entire chromosome

How to read this image: Sequence 1 has four DNA fragments, 150, 100, 75, and 60 bp long. If a fragment size
is shared between different sequences, it represents the same region from the chromosome.


# In[33]:


#assemble the sequence based on the fragments. we know where each fragment begins and ends. 
#this basically means we have a tuple of fragments. we need to see where the beginnings and ends of the fragments match up. 

#these are all the sequences and the length of their fragments. the fragments of equal length are in the same location
#on the chromosome, therefor match up with each other. 
#s we need to match up the fragments and then order them. 
import numpy as np

seq1=["150","100","75","60"]
seq2=["200","150","100","60"]
seq3=["150","100","75","60","50"]
seq4=["200","100","60"]
seq5=["200","100"]
seq6=["150","75","60","50"]

#https://theautomatic.net/2018/11/28/how-to-measure-dna-similarity-with-python-and-dynamic-programming/#:~:text=Add%201%20for%20each%20match%20between%20the%20sequences,gap%20i.e.%20insertion%20%2F%20deletion%20%28shown%20by%20%E2%80%9C-%E2%80%9C%29
#use a scoring method. Add 1 for each match between the sequences
#Subtract 1 for each mismatch
#Subtract 1 for each gap i.e. insertion / deletion (shown by “-“)

#we can shift nucleotides in a sequence as long as the 
#order of the nucelotides doesn’t change
#we will make a score matrix

#try this with just two strings first (seq1 and seq2)
 
# initialize score matrix

#calculate the score values for each cell in the matrix
# define each cell in the matrix by as the max score possible in that stage
        
#the next function figures out the alignment of the sequences
def GET_SCORE(n1, n2, penalty = -1, reward = 1):
     
    if n1 == n2:
        return reward
    else:
        return penalty
 
 
def global_alignment(X, Y, penalty = -1, reward = 1):
     
# initialize score matrix
    score_matrix = np.ndarray((len(seq1) + 1, len(seq2) + 1))
      
    for i in range(len(seq1) + 1):
        score_matrix[i, 0] = penalty * i
     
    for j in range(len(seq2) + 1):
        score_matrix[0, j] = penalty * j
         

    # define each cell in the matrix by as the max score possible in that stage
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            match = score_matrix[i - 1, j - 1] + GET_SCORE(seq1[i - 1], seq2[j - 1], penalty, reward)
            delete = score_matrix[i -1, j] + penalty
            insert = score_matrix[i, j - 1] + penalty
             
            score_matrix[i, j] = max([match, delete, insert])
             
     
    i = len(seq1)
    j = len(seq2)
     
    align_seq1 = ""
    align_seq2 = ""
     
    while i > 0 or j > 0:
         
        current_score = score_matrix[i, j]
        left_score = score_matrix[i - 1, j]
         
         
        if i > 0 and j > 0 and seq1[i - 1] == seq2[j - 1]:
            align_seq1 = seq1[i - 1] + align_seq1
            align_seq2 = seq2[j - 1] + align_seq2
            i = i - 1
            j = j - 1
         
        elif i > 0 and current_score == left_score + penalty:
            align_seq1 = seq1[i - 1] + align_seq1
            align_seq2 = "-" + align_seq2
            i = i - 1
             
        else:
            align_seq1 = "-" + align_seq1
            align_seq2 = seq2[j - 1] + align_seq2
            j = j - 1
    return align_seq1, align_seq2 

#call the function
global_alignment(seq1, seq2)


# In[34]:


#the output shows the alignment between the two lists, with a "-" for a blank space. 
#maybe just do this with all the sequences and then print them so they are stacked. (with a "\n")
print(global_alignment(seq1, seq2),"\n",global_alignment(seq3, seq4), "\n", global_alignment(seq5, seq6))


# seq1   -1501007560
# seq2 200150100 -60 
# 
# seq3 150-  100756050
# seq4 -  200100- 60- 
# 
# seq5 200-  100- - -
# seq6 -  150-  756050

# we can see in this above text how the sequences align with each other
# 
# so the order of the full sequence is:
# 
# 200, 150, 100, 75, 60, 50
# 
# there may be a mutation in seq3
