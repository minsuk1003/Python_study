# 1번 문제
# 풀이 1
# for, if
def multiple_sum(n):
    sum = 0
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum

print(multiple_sum(1000))

# 풀이 2
# list comprehension
print(sum(list([x for x in range(1000) if x%3==0 or x%5==0])))


# 2번 문제
# 풀이 1
# 너무 복잡하다
def num_count(start, end):
    num_count_list = []
    for num in range(start, end+1):
        str_num = str(num)
        num_count_list.append(list(str_num))
    result = [data for inner_list in num_count_list for data in inner_list]
    print(result)

    return [result.count(str(i)) for i in range(10)]
    
print(num_count(10,15))

# 풀이 2
# 딕셔너리를 활용
def num_count(start, end):
    count = {x:0 for x in range(0,10)}
    for x in range(start,end+1):
        for i in str(x):
            count[int(i)] += 1
    return count

print(num_count(10, 15))