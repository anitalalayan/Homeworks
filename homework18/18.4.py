def process_data(data, *, operation='sum'):
    if not data:
        return 0      
    if operation == 'sum':
        total = 0        
        for number in data:  
            total += number
        result = total
    
    elif operation == 'average':
        if len(data) == 1:
            return data[0]         
            
        total = 0
        for number in data:
            total += number
        result = total / len(data)
    
    elif operation == 'max':
        if len(data) == 0:
            return "Cannot determine max of an empty list"
        
        result = data[0]  
        for number in data[1:]:  
            if number > result:
                result = number
    
    elif operation == 'min':
        if len(data) == 0:
            return "Cannot determine min of an empty list"
        
        result = data[0]  
        for number in data[1:]: 
            if number < result:
                result = number
    
    else:
        return f"Unsupported operation: {operation}"
    
    return result


ls  = [10, 20, 30, 40, 50]


print(process_data(ls))

# Using different operations

print(process_data(ls, operation='average'))  
print(process_data(ls, operation='max'))  
print(process_data(ls, operation='min'))      

