def canCompleteCircuit(gas, cost):
        gas_sort = gas.copy()
        cost_sort = cost.copy()
        gas_sort.sort()
        cost_sort.sort()
        arr =[]
        for i in range(len(cost)):
            if cost[i]== cost_sort[0]:
                if i+1 != len(gas):
                    if gas[i] < cost[i+1]:
                        continue
                    else:
                        start = i
                else:
                    if gas[i] < cost[0]:
                        continue
                    else:
                        start = i

        if sum(gas) < sum(cost):
            return -1
        else:
            return start 
            
        
print(canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))
