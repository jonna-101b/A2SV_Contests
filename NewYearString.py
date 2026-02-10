from collections import deque

def checkThisYear(chars: deque[str]) -> bool:
  return "".join(chars) == "2026"

def checkNewYear(chars: deque[str]) -> bool:
  return "".join(chars) != "2025"
  
def checkTestcase(testcase: str, window: deque[str]) -> None:
  if checkThisYear(window):
    print(0)
    return 

  this_year_present = False
  last_year_present = not checkNewYear(window)
  
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

if "__main__":
    no_of_tetscases = int(input())

    for _ in range(no_of_tetscases):
      chars_length = int(input())
      chars = input()
      checkTestcase(chars, deque([chars[i] for i in range(4)]))