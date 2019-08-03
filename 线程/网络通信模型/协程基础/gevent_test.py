import gevent


def foo():
    print('Running in foo')

def bar():
    print('Running in bar')

f = gevent.spawn(foo)
b = gevent.spawn(bar)

# gevent.joinall([f,b])
gevent.sleep(1)