def beforeMidterm(score, jitpisai, midterm):
    point = score + jitpisai + midterm
    return point


score = int(input("score = "))
jitpisai = int(input("jitpisai = "))
midterm = int(input("midterm = "))
print("คะแนนกลางภาค: %d" % beforeMidterm(score, jitpisai, midterm))
