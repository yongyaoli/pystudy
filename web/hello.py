#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #return [b'<h1>Hello world!</h1>']
    print(environ['PATH_INFO'])
    body = '<h1>hello, %s</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
