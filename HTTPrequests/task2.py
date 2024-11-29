# 2. Implement a way to manually extract query parameters from the URL in the GET request.
# Requirements:
# Write code that extracts a specific query parameter (e.g., email) from the URL string in self.path.
# Use string manipulation to split and parse the query string.
# Hints: Separate the URL by ? to get the query portion, then split by & and = to identify key-value pairs.

class MyRequestHandler:
    def __init__(self, path):
        self.path = path

    def extract_query(self, arg):
        if '?' in self.path:
            query_str = self.path.split('?', 1)[1]

        else:
            return None

        query_pairs = query_str.split('&')
        print(query_pairs)
        for pair in query_pairs:
            print(pair)
            key, value = pair.split('=')
            print(key, value)
            if key == arg:
                return value
        return None



if __name__ == '__main__':
    handler = MyRequestHandler('https://example.com/products?category=electronics&price=high&sort=date_desc')
    query = handler.extract_query('category')
    print(query)


