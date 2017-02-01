from functools import wraps
from im_finished.lib import sms
import os


def basic_formatter(fn_name, fn_result):
    return 'Hey Bozo, {} just finished executing. The answer to all lifes questions is {}'.format(fn_name, fn_result)


def send_text(to=os.environ.get('TWILIO_TO_NUM'), message_formatter=basic_formatter):
    """ send a text message to the recipient defined in the `to` parameter. Optionally, a message formatting functon may be passed
    which accepts as its two arguments the:

    1) result of the wrapped function execution
    2) the name of the wrapped function

    and returns a string to be used in the body of the text message.

    :param to: `str` phone number to send a text to
    :return: `func`
    """
    if to is None:
        raise ValueError("the thing with texting is, you have to specify a `to` (you're missing a phone number in the `to` param)")

    def _inner(fn):
        @wraps(fn)
        def _decorator(*args, **kwargs):
            fn_result = fn(*args, **kwargs)

            message = message_formatter(fn.__name__, fn_result)
            sms.send(to, message)

            return fn_result

        return _decorator

    return _inner