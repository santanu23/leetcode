import uuid

class Codec:
    
    def __init__(self):
        self.url_length = 5
        self.map = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        new_url = "http://tinyurl.com/" + str(uuid.uuid4())[0:self.url_length]
        self.map[new_url] = longUrl
        return new_url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.map[shortUrl]
