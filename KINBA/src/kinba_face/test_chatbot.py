#!/usr/bin/env python3
# test_chatbot.py - Unit testing chatbot code

class TestActions(unittest.TestCase):
    def setUp(self):
        self.ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    # Test small talk
    def test_hello(self):
        query = 'Hello'

        request = ai.text_request()
        request.query = query

        response = request.getresponse()
        responsestr = response.read().decode('utf-8')
        response_obj = json.loads(responsestr)

        result = response_obj['result']

        self.assertEqual(result['resolvedQuery'].lower(), query.lower())

        self.assertEqual(result['action'], 'greeting')
        self.assertEqual(result['fulfillment']['speech'], 'Hi! How are you?')

    # Test if Kinba can talk about himself
    def test_you_name(self):
        query = 'What is your name?'

		request = ai.text_request()
        request.query = query

        response = request.getresponse()
        responsestr = response.read().decode('utf-8')
        response_obj = json.loads(responsestr)

        result = response_obj['result']

        self.assertEqual(result['resolvedQuery'].lower(), query.lower())
        self.assertEqual(result['action'], 'name')
        self.assertTrue(len(result['contexts']) == 1)

        context = result['contexts'][0]

        self.assertEqual(context['name'], 'name_question')
        self.assertTrue(len(context['parameters']) == 4)

        parameters = context['parameters']
        param = parameters.get('param', None)

        self.assertTrue(param)
        self.assertEqual(parameters['param'], 'blabla')

        hello_with_context = self.load_text_request_with_quiery('hello', resetContexts=False)

        self.assertTrue(len(hello_with_context['result']['contexts']) == 1)
        self.assertEqual(hello_with_context['result']['contexts'][0]['name'], 'name_question')

        hello_without_context = self.load_text_request_with_quiery('hello', resetContexts=True)

        self.assertTrue(len(hello_without_context['result']['contexts']) == 0)


if __name__ == '__main__':
    unittest.main()