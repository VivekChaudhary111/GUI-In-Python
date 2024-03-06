def generate_pattern(n):
    # Loop through the range of numbers from 0 to 10*n, with a step of 3*n
    for i in range(0, 10*n, 3*n):
        # Create a string of n consecutive numbers starting from i
        num_str = ''.join(str(j) for j in range(i, i+3*n, n))
        # Print the string of numbers, followed by a newline character
        print(num_str)
        # Create a string of n consecutive 9's
        nine_str = '9' * n
        # Print the string of 9's, followed by a newline character
        print(nine_str)
        # If n is greater than 1, create a string of n-1 consecutive 0's
        # followed by a string of n consecutive numbers starting from 1
        if n > 1:
            zero_str = '0' * (n-1) + '123'
            # Print the string of 0's and 123, followed by a newline character
            print(zero_str)
            # Create a string of n-1 consecutive 9's followed by a string of n consecutive numbers
            # starting from 6
            nine_six_str = '9' * (n-1) + '6789'
            # Print the string of 9's and 6789, followed by a newline character
            print(nine_six_str)
        else:
            # If n is 1, just print 0 and 123 on separate lines
            print(0)
            print(123)