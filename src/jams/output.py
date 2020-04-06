def output(message, passed, **kwargs):
    '''
    output provides response for checker
    '''
    line = '[+]'
    details = ''
    if not passed:
        line = '[x]'
        details = kwargs.get('details')
    result = '{0}: {1}\n{2}'.format(line, message, details)
    if not message:
        result = '{0}: \n{2}'.format(line, details)
    print(result)
