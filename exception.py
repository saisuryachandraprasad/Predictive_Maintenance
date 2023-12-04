import sys


def get_error_detail(error, error_detail:sys):

    """
    Args: error-> return the error message 
    error detail take error message in sys format
    """
    _,_,exc_tab = error_detail.exc_info()
    filename = exc_tab.tb_frame.f_code.co_filename
    error_message = "Error occured in python script [{0}] at line number [{1}] and message is [{2}]".format(
        filename, exc_tab.tb_lineno, str(error)
    )
    return error_message



class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys) -> None:
        super().__init__(self,error_message)
        self.error_message = get_error_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message
