#V1.0
import mimikodev
path = "問題.txt"
with open(path) as f:
    mondai = [s.strip() for s in f.readlines()]
print("何回遊ぶの?")
kaisuu = input()
print("へぇー" + kaisuu + "回遊ぶんだー")
for i in range(int (kaisuu)):
    mimikodev.dedenn(mondai)