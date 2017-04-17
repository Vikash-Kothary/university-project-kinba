#!/usr/bin/env python3
# apiai.py -


from apiai import ApiAI
import json


def main():
    CLIENT_ACCESS_TOKEN = '4a2eedad86774b08b5b63568e8d5a9fa'

    ai = ApiAI(CLIENT_ACCESS_TOKEN)

    while running():
        user_message = raw_input()

        if user_message == u"exit"
            break

        request = ai.text_request()
        request.query = user_message

        response = json.loads(request.getresponse().read())

        print(response)


def running():
    return True

if __name__ == '__main__':
    main()
