def output(message, passed):
    '''
    output provides response for checker
    '''
    line = '[+]'
    if not passed: line = '[x]'
    print('{0}: {1}'.format(line, message))