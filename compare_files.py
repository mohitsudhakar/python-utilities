import sys
def func():
  same = True
  newfile = sys.argv[1]
  oldfile = sys.argv[2]
  with open(newfile, "r") as new:
    with open(oldfile, "r") as old:
      new_lines = list(new.readlines())
      old_lines = list(old.readlines())
      num_lines = min(len(new_lines), len(old_lines))
      for i in range(num_lines):
        if new_lines[i] != old_lines[i]:
          same = False
          break
        #if i < 20:
        #  print(new_lines[i], old_lines[i])
  print(same)

if __name__ == "__main__":
  func()
