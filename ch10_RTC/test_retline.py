# Test "return line"

from time import sleep
for i in range(61):
    print(f"\r{i}", end="")
    sleep(0.1)
print()