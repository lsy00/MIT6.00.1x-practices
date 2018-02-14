def pingpong(n):
    '''
    The sequence starts at 1 and it is initially in increasing order.
    If the element k includes 7 or can be divided by 7, the direction of the
    sequence will be changed.
    The first 30 elements of the sequence is shown below, the direction changed
    happen at 7th, 14th, 17th, 21th, 27th and 28th elements
    1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6

    乒乓序列从1开始计数，并且始终向上或向下计数。
    在元素k处，如果k是7的倍数或包含数字7，方向将切换。
    乒乓序列的前30个元素如下所示，方向交换在第7,14和17，21，第27和28个元素：
    1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6
    '''
    #The function will find the nth element in the sequence
    ans = 0
    times = 0
    turn_time = 0
    while True:
        
        for i in range(7):
            if turn_time%2 == 0:
                ans +=1
            elif turn_time%2 == 1:
                ans -=1
            times += 1
            if times == n:
                return ans
                break
            if (times-7)%10 == 0 and times>7 and times%7!=0:#个位数为7换
                turn_time +=1
            elif times/10 >= 7 and  times/10 <8 and times%7!=0:#十位数为7换
                turn_time+=1
        turn_time+=1#倍数为7换
        
    
    
    

