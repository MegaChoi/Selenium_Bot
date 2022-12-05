from Comment import Comment
import threading
import csv

# Attack = Comment("sonvuvu2020@gmail.com", "19001009Gbc%", targetURL)
# Attack.lauch()

# with open("src\\Targets.txt") as f:
#     lines = f.readlines()
# for line in lines:
#     print(line.strip())


f = open("src\\Credentials.csv", "a",newline="")
new = (2,3)
writer = csv.writer(f)
writer.writerow(new)