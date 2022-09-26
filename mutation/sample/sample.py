def mutate_string(strin, position, character):
    l=list(strin)
    l[position]=character
    strin =''.join(l)
    return strin