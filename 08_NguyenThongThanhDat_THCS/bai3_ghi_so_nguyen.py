# Bài 3: Ghi số nguyên vào file
nums = [1, 2, 3, 4, 5]
with open("so_nguyen.txt", "w") as f:
    for n in nums:
        f.write(str(n) + "\n")
