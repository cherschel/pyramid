from pyramid.view import view_config

@view_config(name='one', renderer='string')
def one(request):
    return 'One!'


@view_config(name='two', renderer='string')
def two(request):
    return 'Two!'

def includeme(config):
    config.scan()
    
