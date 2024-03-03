import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    # Implementing vectors e,s as lists (arrays) of length 26
    # with p[0] being the probability of 'A' and so on
    e = [0]*26
    s = [0]*26

    with open('e.txt', encoding='utf-8') as f:
        for line in f:
            # strip: removes the newline character
            # split: split the string on space character
            char, prob = line.strip().split(" ")
            # ord('E') gives the ASCII (integer) value of character 'E'
            # we then subtract it from 'A' to give array index
            # This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')] = float(prob)
    f.close()

    with open('s.txt', encoding='utf-8') as f:
        for line in f:
            char, prob = line.strip().split(" ")
            s[ord(char)-ord('A')] = float(prob)
    f.close()

    return (e, s)


def shred(filename):
    # Using a dictionary here. You may change this to any data structure of
    # your choice such as lists (X=[]) etc. for the assignment
    X = dict()
    for ascii_value in range(65, 91):
        letter = chr(ascii_value)
        X[letter] = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            for char in line:
                if ord(char) >= 65 and ord(char)<= 90 or ord(char) >= 97 and ord(char)<= 122:
                    letter = char.upper()
                    X[letter] += 1
    return X

def printDic(Dicname):
    for key, value in Dicname.items():
        print(f"{key} {value}")

def getLog(input):
    return math.log(input)

def getF(P, input_list, prob_list):
    result = math.log(P)
    for i in range(26):
        result += input_list[chr(i + 65)] * getLog(prob_list[i])
    return result
        
# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!
def main():
    ENGLISH = 0.6
    SPANISH = 1 - ENGLISH
    (E, S) = get_parameter_vectors()

    #1
    print("Q1")
    dic_A = shred('letter.txt')
    printDic(dic_A)

    #2
    print("Q2")
    X1loge1 = round(dic_A["A"] * getLog(E[0]),4)
    X1logs1 = round(dic_A["A"] * getLog(S[0]),4)
    print(X1loge1)
    print(X1logs1)

    #3
    print("Q3")
    F_english = round(getF(ENGLISH, dic_A, E), 4)
    F_spanish = round(getF(SPANISH, dic_A, S), 4)
    print(F_english)
    print(F_spanish)

    #4
    print("Q4")
    if (F_spanish - F_english >= 100):
        Prob_E = 0
    elif(F_spanish - F_english <= -100):
        Prob_E = 1
    else:
        Prob_E = round(1/(1 + math.exp(F_spanish - F_english)),4)
    print(Prob_E)

main()
