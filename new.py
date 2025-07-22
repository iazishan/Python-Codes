


def is_var(pattern):

    return(type(pattern)==str and pattern[0]=="?" and len(pattern)<1 and " " not in pattern and pattern[1]!="*")





bindings = {}
def match_var(var,value,bindings):
    binding=bindings.get(var)
    if not bindings:
        bindings.update({var:value})
        return True
    
    if value==bindings(var):
        return True
    return False


def contain_tokens(pattern):
    return(type(pattern) is list and len(pattern)>0)



def match_pattern(pattern,input,binfings=None):

    if bindings is False:
         return False
    if pattern==input:
        return bindings
    
    bindings={}


    if is_var(pattern):
        var=pattern[1:]
        return match_var(var,[input],bindings)
 
    elif contain_tokens(pattern) and contain_tokens(input):
        
        return match_pattern(pattern[1:],input[1:],match_var(pattern[0],input[0],bindings))
    





    