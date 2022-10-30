"""Functions for auto search of hidden number"""
"""Game: Guess the number (machine style)"""


def predict_number(number: int=1, start_value: int=1, end_value: int=100):
    """_summary_

    Args:
        number (int, optional): hidden number to be guessed. Defaults to 1.
        start_value (int, optional): the minimum value of the range that the number is in. Defaults to 1.
        end_value (int, optional): the maximum value of the range that the number is in. Defaults to 100.

    Raises:
        ValueError: start_value should be less than end_value
        ValueError: hidden number must be in range between start_value and end_value)

    Returns:
        _type_: function counts number of guessing tries and returns that value
    """
    count = 0
    
    if end_value <= start_value:
        raise ValueError("end_value must be less than start_value")
    if not start_value <= number <= end_value:
        raise ValueError("hidden number should be in range between start_value and end_value")    
     
    while True:
        predict_number = start_value + (end_value - start_value) // 2
        count += 1
        if number > predict_number:            
            start_value = predict_number        
        elif number < predict_number:            
            end_value = predict_number
        else:
            return count
        
