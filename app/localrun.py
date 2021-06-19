import main

if __name__ == '__main__':
    event = {'Records': [{'kinesis': {'kinesisSchemaVersion': '1.0',
                                      'partitionKey': '1',
                                      'sequenceNumber': '49617910691496523030396332104062025542374210616147574786',
                                      'data': 'eyJjaGFuZ2UiOiBbIl9zYV9pbnN0YW5jZV9zdGF0ZSIsICJ0aWVyXzNfb3B0X2luIiwgImxhc3RfbG9naW5fZGF0ZSIsICJpc19wYXNzd29yZF9leHBpcmVkIiwgInVzZXJuYW1lIiwgImVtYWlsIiwgImFjY291bnRfY3JlYXRpb25fZGF0ZSIsICJpc190ZW1wb3JhcnlfcGFzc3dvcmQiXSwgInR5cGUiOiAiUGVyc2lzdGVuY2VBUEkiLCAiY3JlYXRpb25fdGltZSI6ICIyMDIxLTA1LTE3IDEzOjUzOjA4LjM1MTQ3NiIsICJzb3VyY2UiOiAiU0xTIiwgIm1lc3NhZ2UiOiB7Il9zYV9pbnN0YW5jZV9zdGF0ZSI6ICI8c3FsYWxjaGVteS5vcm0uc3RhdGUuSW5zdGFuY2VTdGF0ZSBvYmplY3QgYXQgMHgxMGZkZTYwNTA+IiwgInRpZXJfM19vcHRfaW4iOiB0cnVlLCAiYmVuZWZpY2lhcnlfa2V5IjogIjk5OTk5MDA4MSIsICJsYXN0X2xvZ2luX2RhdGUiOiAiMjAyMS0xMi0zMSAwMDowMDowMCIsICJpc19wYXNzd29yZF9leHBpcmVkIjogdHJ1ZSwgInVzZXJuYW1lIjogIiIsICJlbWFpbCI6ICIiLCAiYWNjb3VudF9jcmVhdGlvbl9kYXRlIjogIjIwMjAtMTItMzEgMDA6MDA6MDAiLCAiaXNfdGVtcG9yYXJ5X3Bhc3N3b3JkIjogdHJ1ZX19',
                                      'approximateArrivalTimestamp': 1621259588.743},
                          'eventSource': 'aws:kinesis', 'eventVersion': '1.0',
                          'eventID': 'shardId-000000000000:49617910691496523030396332104062025542374210616147574786',
                          'eventName': 'aws:kinesis:record', 'invokeIdentityArn': 'arn:aws:iam::626512334475:role/LambdaVerticaUpdate',
                          'awsRegion': 'us-east-1', 'eventSourceARN': 'arn:aws:kinesis:us-east-1:626512334475:stream/bedap-dev_persistance'}]}
    context = {}
    main.lambda_handler(event,context)