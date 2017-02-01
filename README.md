# im-finished
Sometimes when you're finished, you wanna know. So, here's a dead simple decorator to send a text to you, your friends, your mom, or whomever when a function has completed processing. 

## Installation
`pip install im-finished`

## Requirements
1) Sign up for a Twilio account here: http://twilio.com/. You're going to have to create a number as well, but no reason why you shouldn't be able to stay on the free plan.

2) Add the following environment variables to either your `.bashrc`, `.zshrc`, or heck, do it with a plain old `export` in your session if you so choose:
  * `TWILIO_ACCOUNT_SID=<THE TWILIO ACCOUNT TOKEN>`
  * `TWILIO_AUTH_TOKEN=<THE TWILIO AUTHENTICATION TOKEN (SECRET KEY)>`
  * `TWILIO_FROM_NUM=<THE TWILIO NUMBER YOU WANT TEXTS TO ORIGINATE FROM>`
  * `TWILIO_TO_NUM=<OPTIONAL. IF SET, THIS IS THE DEFAULT NUMBER TO SEND TEXTS TO>`


## Basic Usage
You can finish in a basic "im-finished" way in one of two ways. Yes, that was confusing rhetoric. No, I won't change it:

```
###--- 1 ---###
from im_finished import send_text

@send_text()
def some_func():
  """ perform some work """
  lana = 'be careful'
  archer = '....no'
  
  return lana + archer
```

```
###--- 2 ---###
from im_finished import when_finished, send_text

@when_finished(send_text)
def some_func():
  """ perform some work """
  lana = 'be careful'
  archer = '....no'
  
  return lana + archer
```

both of these examples will yield the same result, a text to the number you defined as the `TWILIO_TO_NUM` environment variable to the effect of 'Hey Bozo, some_func just finished executing. The meaning of life is "be careful.....no"'. IMO, I like the `when_finished` variation more.

## Advanced Usage
In addition to the basic usage given above, there's also a few more advanced things you can do, both with the formatting of the message to be sent upon completion and dynamically controlling the recipient of THE FINISHER text. However, to use these advanced settings, you won't be able to use `when_finished` and must instead use `send_text` directly.

First, formatting can be controlled by passing a parameter `message_formatter` to the `send_text` decorator. A message formatter will receive as positional arguments both the name of the wrapped function as well as the execution result(s) of the function call. Here's an example for those learn-through-seeing folk:

```
from im_finished import send_text


def my_awesome_formatter(fn_name, fn_result):
  return 'well I'll be, {} executed no problem and got a result of {}. Today is a good day'.format(fn_name, fn_result)
  
  
@send_text(message_formatter=my_awesome_formatter)
def some_func():
  bob = 'jimmy pesto is the worst'
  return bob
  
some_func() # --> text will be sent having contents "well I'll be, some_func executed no problem and got a result of jimmy pesto is the worst. Today is a good day"
```

The other possible parameter passable to `send_text` is `to` which - shocker - controls who will receive the text, overriding the value of the `TWILIO_TO_NUM` environment variable if set. Here's a quick example:

```
from im_finished import send_text

  
@send_text(to='+1234567890)
def some_func():
  return 1 + 1
  
some_func() # --> text will be sent to +1234567890
```
