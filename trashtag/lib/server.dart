import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:http_parser/http_parser.dart';

String currentUsername;

String serverURL = "https://73cd93dc9605.ngrok.io";

login(username, password) async {
  final response = await http.get('$serverURL/loginuser/$username/$password');
  if (response.statusCode == 200) {
    Map res = json.decode(response.body);
    if (res['status'] == 200) {
      currentUsername = res['username'];
      return true;
    }
  }
  print("Error");
  return false;
}

register(name, username, password) async {
  final response =
      await http.get('$serverURL/registeruser/$name/$username/$password');
  if (response.statusCode == 200) {
    Map res = json.decode(response.body);
    if (res['status'] == 200) {
      return true;
    }
  }
  print("Error");
  return false;
}

// register(username, password, email) async {
//   final response = await http.post(
//     '$serverURL/register',
//     headers: <String, String>{
//       'Content-Type': 'application/json; charset=UTF-8',
//     },
//     body: jsonEncode(<String, String>{
//       'username': username,
//       'password': password,
//       'email': email
//     }),
//   );
//   if (response.statusCode == 200) {
//     Map obj = json.decode(response.body);
//     if (obj['code'] == 'S1') return obj;
//   }
//   return {'code': 'ERR'};
// }
