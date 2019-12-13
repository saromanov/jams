def output(message, passed, **kwargs):
    '''
    output provides response for checker
    '''
    line = '[+]'
    details = ''
    if not passed:
        line = '[x]'
        details = kwargs.get('details')
    print('{0}: {1}\n{2}'.format(line, message, details))
