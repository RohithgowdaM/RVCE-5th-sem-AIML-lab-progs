def hill_climbing(func,start,step_size=0.01,max_itr=1000):
    curr=start
    cur_val=func(curr)
    for i in range(max_itr):
        next=curr+step_size
        next_val=func(next)
        prev=curr-step_size
        prev_val=func(prev)
        if next_val>cur_val and next_val>prev_val:
            cur_val=next_val
            curr=next
        elif prev_val>cur_val and prev_val>next_val:
            cur_val=prev_val
            curr=prev
        else:
            break
    return curr,cur_val

while True:
    funct=input("Enter the function value wrt to x: ")
    try:
        x=0
        eval(funct)
        break
    except Exception as e:
        print("Invalid function!!!")

func=lambda x: eval(funct)
while True:
    s=input("Enter the search value to begin")
    try:
        start=float(s)
        break
    except ValueError as e:
        print("Invalid number, use float values")

maxima,max_value=hill_climbing(func,start)
print("Maximum value",max_value," achieved at", maxima)