while(1) :
    str = input()
    
    if str =="." : 
        break
    
    stack = []
    for ch in str :
        if ch == "(" or ch == "[" :
            stack.append(ch)
        elif ch == ")" :
            if not stack or stack[-1] != "(" :
                stack.append(ch)
                break
            else :
                stack.pop()
        elif ch == "]" :
            if not stack or stack[-1] != "[" :
                stack.append(ch)
                break
            else :
                stack.pop()
    if len(stack) == 0 :
        print("yes")
    else :
        print("no")
