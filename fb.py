import facebook

a = "EAAPOltciSiYBAJq1r4k5ZAXWnJuuFHED7SL8ZBYJi9v6AzlcTLT6EvDu23mQqTG400naAvPUP1kEgiio10JBhJZCF0ftfEWLkQZCGZBPbEsK5ELOvFgqBIsIvZCq51tV5TZC2hiyxOK9bfOkC05ODnzjZClG06JXpbZApZB5LsAodUdGojMmRrzNaJXtulcSVkmRGyzeGOczWmiztP8eoFNfkZBNeNoqoR4vQ79o0LZCX54tOgZDZD"


v = facebook.GraphAPI(a)
v.put_object(parent_object='me', connection_name='feed',
                  message='Hello, world')