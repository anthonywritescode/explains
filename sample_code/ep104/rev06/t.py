import queue


def get_queue() -> 'queue.Queue[int]':
    return queue.Queue()


reveal_type(get_queue())
