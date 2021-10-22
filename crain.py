def solution(board, moves):
    answer = 0
    pick_list = []
    switch = True
    
    while switch:
        if len(moves) == 0:
                switch = False
                break
        m = moves.pop(0)
        for i in range(len(board)):            
            if board[i][m-1] == 0:
                continue
            else:
                pick_list.append(board[i][m-1])
                board[i][m-1] = 0
                break
            
    print(pick_list)
    end_point = 0
    switch = True
    while switch:    
        if len(pick_list) == end_point+1:
            switch = False
            break         
        if len(pick_list) == 0:
            switch == False
            break
            
        for i in range(len(pick_list)-1):
            end_point = end_point + 1
            p = pick_list[i]
            pp = pick_list[i+1]    
            # print(p,pp)
            if p == pp:
                answer = answer + 2                
                a = pick_list.pop(i)
                b = pick_list.pop(i)       
                end_point = 0
                # print(pick_list)
                break
        
    return answer