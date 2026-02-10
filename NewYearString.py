from collections import deque
from typing import List

def checkThisYear(chars: deque[str]) -> bool:
  return "".join(chars) == "2026"

def checkNewYear(chars: deque[str]) -> bool:
  return "".join(chars) != "2025"
  
def checkTestcase(testcase: str, window: deque[str]) -> None:
  this_year_present = False
  last_year_present = checkNewYear(window)
  
  for i in range(4, len(testcase)):
    window.popleft()
    window.append(testcase[i])
    if checkThisYear(window):
      this_year_present = True
      break
    
    if checkNewYear(window):
      last_year_present = True
      
  if this_year_present:
    print(0)
  elif last_year_present:
    print(1)
  else:
    print(0)

def minSteps(testcases: List[str]) -> None:
  for testcase in testcases:
    if len(testcase) < 4:
      print(0)
      continue
    
    window = deque([testcase[i] for i in range(4)])
    if checkThisYear(window):
      print(0)
      continue
    elif not checkNewYear(window):
      print(1)
      continue
    
    checkTestcase(testcase, window)

if "__main__":
    no_of_tetscases = int(input())
    testcases = []

    for _ in range(no_of_tetscases):
      chars_length = int(input())
      chars = input()
      testcases.append(chars)
      
    minSteps(testcases)
