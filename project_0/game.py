"""Function for hidden number auto search"""
"""Game: Guess the number (all by machines)"""
"""Python 3.10.8"""

def predict_number(number: int=1, start_value: int=1, end_value: int=101) -> int:
    """This function tries to predict the random number that is in [start_value, end_value)
        The algorythm uses the simple idea of dividing searching area by half for each iteration
        The complexity of algorythm is O(log(n, 2))
        
    Args:
        number (int, optional): hidden number to be guessed. Defaults to 1.
        start_value (int, optional): the minimum value of the range that the number is in. Defaults to 1.
        end_value (int, optional): the maximum value of the range that the number is in. Defaults to 101.

    Raises:
        ValueError: start_value should be less than end_value
        ValueError: hidden number must be in range between start_value (inclusive) and end_value (exclusive))

    Returns:
        int: function counts number of guessing tries and returns that value
    """
    
    count = 0    
    if end_value <= start_value:
        raise ValueError("end_value must be less than start_value")
    if not start_value <= number < end_value:
        raise ValueError("Hidden number should be in range between start_value and end_value (exclusive)")    
     
    while True:
        predict_number = start_value + (end_value - start_value) // 2
        count += 1
        if number > predict_number:            
            start_value = predict_number
        elif number < predict_number:            
            end_value = predict_number
        else:
            return count    




