import sys

print(type(sys.path)) # 是个list
print(sys.path)

for p in sys.path:
    print(p)