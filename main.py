def check_health(request):
  return "OK"

def hello_pubsub(data, context):
    if 'data' in data:
        name = base64.b64decode(data['data']).decode('utf-8')
    else:
        name = 'world'
    print(f'Hello {name}')
