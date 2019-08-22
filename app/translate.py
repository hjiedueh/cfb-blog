import json, requests, os, uuid
from flask import current_app
from flask_babel import _


def translate(text, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
     return _('Error: the translation service is not configured.')

    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to={}'.format(dest_language)
    constructed_url = base_url + path + params
    body = [{'text' : text}]
    auth = {'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    r = requests.post(constructed_url, headers=auth, json=body)
    response = r.json()

    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
