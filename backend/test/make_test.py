def prepare_to_test():
    import os
    from google.appengine.api import apiproxy_stub_map
    from google.appengine.api import datastore_file_stub
    from google.appengine.api import memcache
    from google.appengine.api.memcache import memcache_stub
    from google.appengine.api import taskqueue
    from google.appengine.api.taskqueue import taskqueue_stub
    from google.appengine.api import urlfetch_stub

    apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()
    ds_stub = datastore_file_stub.DatastoreFileStub('_', None)
    apiproxy_stub_map.apiproxy.RegisterStub('datastore_v3', ds_stub)
    mc_stub = memcache_stub.MemcacheServiceStub()
    apiproxy_stub_map.apiproxy.RegisterStub('memcache', mc_stub)
    tq_stub = taskqueue_stub.TaskQueueServiceStub()
    apiproxy_stub_map.apiproxy.RegisterStub('taskqueue', tq_stub)
    uf_stub = urlfetch_stub.URLFetchServiceStub()
    apiproxy_stub_map.apiproxy.RegisterStub('urlfetch', uf_stub)
    os.environ['APPLICATION_ID'] = '_'
