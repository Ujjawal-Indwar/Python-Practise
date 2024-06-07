no_subj = int(input("Enter total no of subjects you have \n"))


subject = []
for subj in range(0,no_subj):
    print(f"Enter marks of {subj+1}")
    score = int(input())
    subject.append(score)

print(subject)

high_score = 0

for subj in subject:
    if subj>high_score:
        high_score=subj


print(high_score)

#sub_score = input("Enter the score of 10 subjects\n").split()


# for x in range (0,len(sub_score)):
#     sub_score[x] = int(sub_score[x])
#
# print(sub_score)
#
#
# high_score = 0
#
# for subj in sub_score:
#     if subj >= high_score:
#         high_score = subj
#
# print(high_score)