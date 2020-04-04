import re
class BaseMemoryRepo:
    def __init__(self, data):
        self.data = data
    
    def get_limit(self,filter):
        search = re.search("limit=\\d+",filter)
        if search:
            return int(search.group().split('=')[1])
        else:
            return 10
    def get_offset(self,filter):
        search = re.search("offset=\\d+",filter)
        if search:
            return int(search.group().split('=')[1])
        else:
            return 0
    
    def list(self, request_object=None):
        if request_object == None:
            return self.data
        if request_object['filters'] == "":
            return self.data
        limit = self.get_limit(request_object['filters'])
        offset = self.get_offset(request_object['filters'])
        end = offset  + limit
        return self.data[offset:end]