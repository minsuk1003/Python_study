# 220번
# 웹페이지 정답은 별로 좋지 않은 답안
# 음수도 고려하자
def print_max(a,b,c):
    # return max(a,b,c)
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c

    print(max_value)

print_max(-1,-8,-1)

# 234번
def pickup_even(num_list):

    # # 일반적 방법
    # new_list = []
    # for num in num_list:
    #     if num % 2 == 0:
    #         new_list.append(num)

    # List Comprehension
    return [num for num in num_list if num % 2 == 0]

print(pickup_even(range(22)))
