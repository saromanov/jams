def check_ci(*args, **kwargs):
    """this method trying to parse README.md and find
    badge which is point to CI provider
    """
    result = len(list(filter(lambda x: content.find(
        '{0}/{1}'.format(x, repo)) != -1, ci))) > 0
    output('Checking Badge for CI', result)
    self.score.add_check('Checking Badge for CI', result)
    return result
