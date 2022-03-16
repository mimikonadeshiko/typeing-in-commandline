import mimikodev
path = "問題.txt"
with open(path) as f:
    mondai = [s.strip() for s in f.readlines()]
mimikodev.dedenn(mondai)