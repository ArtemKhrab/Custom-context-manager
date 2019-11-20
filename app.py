import sys


class ContextManager:
    def __init__(self, resource):
        self.resource = resource

    def __enter__(self):
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Exception: {exc_type}")
        print('left from context')


def my_with(manager, body):
    """
    Custom "with" function
    :param manager:
        our custom context manager
    :param body:
        function with our actions
    :return: exception parameters, if they exists
    """
    resource = manager.__enter__()
    error = exc_type = exc_val = exc_tb = None
    try:
        body(resource)
    except Exception as exc:
        exc_type, exc_val, exc_tb = sys.exc_info()
        error = exc
    finally:
        manager.__exit__(exc_type, exc_val, exc_tb)
        if error:
            raise error


def body(resource):
    """
    Do some actions with resource
    :param resource:
    """
    print(resource)

    # raise ValueError


if __name__ == '__main__':
    my_with(ContextManager(2), body)



