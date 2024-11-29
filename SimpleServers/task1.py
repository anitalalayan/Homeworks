from http.server import BaseHTTPRequestHandler, HTTPServer
import json


users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]


class CRUDHandler(BaseHTTPRequestHandler):
    """ Sets response headers """
    def __set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def __write_response(self, data, status=200):
        """Writes JSON response with a given status."""
        self.__set_headers(status)
        self.wfile.write(json.dumps(data).encode())

    def __path_parser(self):
        """ Parses the endpoints"""
        parsed_path = self.path.strip('/').split('/')
        return parsed_path

    def do_GET(self):
        """ Handles GET requests from the web client"""
        parsed_path = self.__path_parser()

        if len(parsed_path) == 1:
            resource = parsed_path[0]
            if resource == 'users':
                self.__set_headers()
                self.__write_response(users)

            elif resource == 'products':
                self.__set_headers()
                self.__write_response(products)
            else:

                self.__write_response({'error': f'{resource} not found'}, status=400)

        elif len(parsed_path) == 2:
            resource, resource_id = parsed_path

            try:
                resource_id = int(resource_id)

                if resource == 'users':
                    try:
                        result = next(user for user in users if user['id'] == resource_id)
                        self.__write_response(result)

                    except StopIteration:
                        self.__write_response({'error': f' ResourceID {resource_id} not found'}, status=400)

                elif resource == 'products':
                    try:
                        result = next(product for product in products if product['id'] == resource_id)
                        self.__write_response(result)

                    except StopIteration:
                        self.__write_response({'error': f' ResourceID {resource_id} not found'}, status=400)

                else:

                    self.__write_response({'error': f'Resource {resource} not found'}, status=400)

            except ValueError:
                self.__write_response({'error': f'Invalid format: {resource_id} '}, status=400)


        else:
            self.__write_response({'error': 'Invalid path'}, status=400)


    def do_POST(self):
        """ Handles POST requests to add a new user to the users list"""
        parsed_path = self.__path_parser()

        if len(parsed_path) == 1:
            self.__set_headers()

            try:
                content_length = int(self.headers['Content-length'])
                body = json.loads(self.rfile.read(content_length))

                resource = parsed_path[0]

                if resource == 'users':
                    new_id = max([u['id'] + 1 for u in users]) if users  else 1
                    body.update({'id': new_id})
                    users.append(body)
                    self.__write_response(users)

                else:
                    self.__write_response({'error': f'Data sent to a wrong resource'}, status=400)

            except (json.JSONDecodeError, ValueError) as e:
                self.__write_response({'error': f'Invalid data : {str(e)}'}, status=400)
        else:
            self.__write_response({'error': 'Invalid path'}, status=400)


    def do_PUT(self):
        """ Handles PUT requests to modify a user's and product's  properties """

        parsed_path = self.__path_parser()

        if len(parsed_path) == 2:
            resource, resource_id = parsed_path
            self.__set_headers()

            try:
                resource_id = int(resource_id)
                content_length = int(self.headers['Content-length'])
                body = json.loads(self.rfile.read(content_length))
                resource = parsed_path[0]

                if resource == 'users':

                    for user in users:
                        if user.get('id') == resource_id:
                            user.update({key: value for key, value in body.items() if key != 'id'})
                            self.__write_response(user)
                            return

                    self.__write_response({'error': f'User with ID {resource_id} not found'}, status=404)



                elif resource == 'products':

                    for product in products:
                        if product.get('id') == resource_id:
                            product.update({key: value for key, value in body.items() if key != 'id'})
                            self.__write_response(product)
                            return

                    self.__write_response({'error': f'Product with ID {resource_id} not found'}, status=404)


                else:
                    self.__write_response({'error': f'Data sent to a wrong resource'}, status=400)

            except (json.JSONDecodeError, ValueError) as e:
                self.__write_response({'error': f'Invalid data : {str(e)}'}, status=400)

        else:
            self.__write_response({'error': 'Invalid path'}, status=400)












def run(server_class=HTTPServer, server_handler=CRUDHandler, port=8000):
    server_address = ('', port)

    httpd = server_class(server_address, server_handler)

    print(f"Server runing on port: {port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()