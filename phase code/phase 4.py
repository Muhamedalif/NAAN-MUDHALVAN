def main():
    # Read the number of integers
    N = int(input())
    
    # Read the list of integers
    numbers = list(map(int, input().split()))
    
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each number in the list
    for i in range(N):
        # Get the current number
        x = numbers[i]
        
        # Calculate the index from the end
        index_from_end = len(numbers) - x
        
        # Append the corresponding number to the result
        result.append(str(numbers[index_from_end]))
    
    # Print the result as a space-separated string
    print(' '.join(result))

if _name_ == "_main_":
    main()