#ABCs
def getSum(A: int, B: int, C: int) -> int:
  return A+B+C
# 0(n)


#All Wrong
def getWrongAnswers(N: int, C: str) -> str:
    c = " "
    for i in C:
        if i == "A":
            c = c + "B"
        else:
            c = c + "A"
    return c
# O(n)


#Battleship
from typing import List
def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  a = 0
  for i in range(R):
    for j in range(C):
      if G[i][j] == 1:
        a+=1
  return a/(R*C)
# 0(n²) 