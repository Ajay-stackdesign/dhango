# def breakingRecords(scores):
#     # Write your code here
#     max_record = 0
#     min_record = 0
#     max = scores[0]
#     min = scores[0]
#
#     for i in range(1, len(scores)):
#         if min < scores[i]:
#             min = scores[i]
#             min_record += 1
#         elif max > scores[i]:
#             max = scores[i]
#             max_record += 1
#         return max_record, min_record
def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    min_record = 0
    max_record = 0

    for i in range(1, len(scores)):
        if min > scores[i]:
            min = scores[i]
            min_record += 1
        elif max < scores[i]:
            max = scores[i]
            max_record += 1

    return  max_record, min_record

score = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    # [10, 5, 20, 20, 4, 5, 2, 25, 1],

# for arr in score:
result = breakingRecords(score)
print(result)
    # score = [

        # [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    # ]
    #
    # for arr in score:
    #     breakingRecords(arr)
    #     print(arr)
