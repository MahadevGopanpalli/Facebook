import facebook

a = "----------------------"


v = facebook.GraphAPI(a)
v.put_object(parent_object='me', connection_name='feed',
                  message='Hello, world')
