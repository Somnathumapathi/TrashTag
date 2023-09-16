import 'dart:convert';
import 'package:http/http.dart' as http;

String? currentUsername;

String serverURL =
    "https://b81d-2405-201-d036-284f-7c18-5161-ab9-979f.ngrok-free.app";

login(username, password) async {
  final uri = Uri.parse('$serverURL/loginuser/$username/$password');
  final response = await http.get(uri);
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
  final uri = Uri.parse('$serverURL/registeruser/$name/$username/$password');
  final response = await http.get(uri);
  if (response.statusCode == 200) {
    Map res = json.decode(response.body);
    if (res['status'] == 200) {
      return true;
    }
  }
  print("Error");
  return false;
}

add2dustbin(productKey, garbageKey) async {
  final uri = Uri.parse(
      '$serverURL/add2dustbin/$currentUsername/$productKey/$garbageKey');
  final response = await http.get(uri);
  print(json.decode(response.body));
  if (response.statusCode == 200) {
    Map res = json.decode(response.body);
    if (res['status'] == 200) {
      return res['coins'];
    }
  }
  print("Error");
  return false;
}
