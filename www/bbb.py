def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'] or 'web')
    print(environ["PATH_INFO"])
    return [body.encode('utf-8')]