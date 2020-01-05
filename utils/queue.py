import django_rq


def enqueue(func, *args, **kwargs):
    queue = django_rq.get_queue('default')
    queue.enqueue(func, *args, **kwargs)
