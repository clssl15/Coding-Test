def solution(n, money):
    answer = 0
    
    dp_list = [0] * (n+1)
    dp_list[0] = 1
    
    for coin in money:
        for i in range(1,n+1):
            if i < coin:
                continue
            dp_list[i] += dp_list[i-coin]
    
    answer = dp_list[n]

    return answer