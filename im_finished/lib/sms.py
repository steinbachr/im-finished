from twilio.rest import TwilioRestClient
import os


def send(to, message):
    """ send an SMS to the given recipient

    :param to: `str` the number of the peoples receiving text
    :param message: `str` the message to be sent
    :return: `bool` True if message sending success, False o/w
    """
    # put your own credentials here
    try:
        ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
        AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
        FROM_NUMBER = os.environ['TWILIO_FROM_NUM']
    except KeyError:
        # make our messaging friendlier
        raise ValueError("friend, a TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_FROM_NUM must be in the environment to continue")

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
        to=to,
        from_=FROM_NUMBER,
        body=message,
    )

    return True