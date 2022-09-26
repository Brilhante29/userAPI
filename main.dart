import 'dart:convert';
import 'dart:io';

Future<void> main() async {
var client = HttpClient();
  try {
    HttpClientRequest request = await client.get('localhost', 8000, '/users/api/1');    
    // Optionally set up headers...
    // Optionally write to the request object...
    HttpClientResponse response = await request.close();
    // Process the response
    final stringData = await response.transform(utf8.decoder).join();
    print(stringData);
  } finally {
    client.close();
  }
}