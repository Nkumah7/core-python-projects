def get_permutations(sequence):
    '''
    Returns a list of all permutations using recursion    
    '''
   
    if len(sequence) <= 1:
        return [sequence]
    
    initial_l = sequence[0] # Store first letter - firstly 'a' and then 'b' and recursion
    final_lst = [] # Final list where strings will be stored
    
    # Recursively gets list from second index till last index
    # - from 'bc' to 'c' and return 'c' because length of 'c' is 1 - returns ['c']
    ps = get_permutations(sequence[1:]) 
    
    # First - Loop through ['c'] - this brings c out from list
    # Second - Loop through ['bc', 'cb']
    for p in ps: 
        # First
        # - From the last recursion, sequence is 'bc' - get range from 0 to the len of input (the string 'bc') - [0, 1]
        # Second
        # - From first recursion, sequence is 'abc' - get range from 0 to the len of input (the string 'abc') - [0, 1, 2]
        for i in range(len(sequence)): 
            # First
            # From the last recursion
            # Loop two times for 0 to 1.             
            # -----------------------------
            # 0 loop - Append p[:0] - "" + b + p[0:] - c to final_lst
            # 1 loop - Append p[:1] - c + b + p[1:] - "" to final_lst
            
            # Second
            # From first recursion
            # Loop three times from 0 to 2
            # -----------------------------
                # Loop 1 for 'bc'
                # 0 loop - Append p[:0] - "" + a + p[0:] - bc to final_lst
                # 1 loop - Append p[:1] - b + a + p[1:] - c to final_lst
                # 2 loop - Append p[:2] - bc + a + p[2:] - "" to final_lst
                
                # Loop 2 for 'cb'
                # 0 loop - Append p[:0] - "" + a + p[0:] - cb to final_lst
                # 1 loop - Append p[:1] - c + a + p[1:] - b to final_lst
                # 2 loop - Append p[:2] - cb + a + p[2:] - "" to final_lst
            final_lst.append(p[:i] + initial_l + p[i:])
            
    # Return final_lst after first loop of p
    # ps = ['bc', 'cb']
    # Go to Second
    # Return final_lst after second loop of p
    # ps = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    # All permutations done after ['c'] and ['bc', 'cb']
    return final_lst            
        

if __name__ == '__main__':   
   example_input1 = 'joe'  
   print('Input:', example_input1)
   print('Actual Output:', get_permutations(example_input1))
   
   example_input2 = 'ice'
   print('\nInput:', example_input2)
   print('Actual Output:', get_permutations(example_input2))
   
   example_input3 = 'oya'
   print('\nInput:', example_input3)
   print('Actual Output:', get_permutations(example_input3))    
