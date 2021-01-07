import 'package:flutter/material.dart';
import 'package:trashtag/server.dart';

import 'home.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key key}) : super(key: key);

  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  TextEditingController uc = new TextEditingController();
  TextEditingController pc = new TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Log In"),
      ),
      body: Center(
        child: Container(
          decoration: BoxDecoration(border: Border.all(color: Colors.black)),
          width: 300,
          height: 230,
          padding: EdgeInsets.all(20),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              TextField(
                controller: uc,
                decoration: InputDecoration(hintText: "Username"),
              ),
              TextField(
                controller: pc,
                decoration: InputDecoration(hintText: "Password"),
              ),
              SizedBox(
                height: 20,
              ),
              RaisedButton(
                child: Text("Login"),
                onPressed: () {
                  print(uc.text);
                  print(pc.text);
                  login(uc.text, pc.text).then((x) {
                    if (x){
                      Navigator.of(context).push(MaterialPageRoute(builder: (context)=>Home()));
                    }
                    else
                      print("Incorrect");
                  });
                },
              )
            ],
          ),
        ),
      ),
    );
  }
}
