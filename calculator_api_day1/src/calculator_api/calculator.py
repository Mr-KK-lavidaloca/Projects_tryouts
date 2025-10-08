"""
Core Calculator Logic- learn functions adn error handling
"""
def add(a:float,b:float)->float:  # type hints 
    return a+b

def subtract(a:float,b:float)->float:  # type hints 
    return a-b

def multiply(a:float,b:float)->float:  # type hints 
    return a*b

def divide(a:float,b:float)->float:  # type hints 
    """error handling zero exception"""
    if b==0:
        raise ValueError("cannot divide by zero")
    return a/b

OPERATIONS={
    "add":add,
    "subtract":subtract,
    "multiply":multiply,
    "divide":divide
}

def calculate(operation:str,a:float,b:float)->dict:
 """
  function compostion and error handling 

  Args:
    operation :math operation to perfom
    a:first number
    b:second number 
 
 Returns:
    dictionary with results or errors  

 """
 if operation not in OPERATIONS:
     return{
         "success": False,
         "error":f"Unknown operation:{operation}",
         "operation":operation 
     }
 try:
    operation_func=OPERATIONS[operation]
    result=operation_func(a,b)
    return{
     "success":True,
     "result":result,
     "operation": operation
        }
        
 except ValueError as e:
    return {
        "success": False, 
        "error": str(e),
            "operation": operation
        }
 except Exception as e:
     
     return {
            "success": False,
            "error": f"Calculation error: {str(e)}",
            "operation": operation
        }