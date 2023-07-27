import 'package:flutter/material.dart';
import 'package:trashtag/login.dart';
import 'package:trashtag/server.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});

  @override
  _RegisterScreenState createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  TextEditingController nc = new TextEditingController();
  TextEditingController uc = new TextEditingController();
  TextEditingController pc = new TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Register"),
      ),
      body: Center(
        child: Container(
          decoration: BoxDecoration(border: Border.all(color: Colors.black)),
          width: 300,
          height: 290,
          padding: EdgeInsets.all(20),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              TextField(
                controller: nc,
                decoration: InputDecoration(hintText: "Name"),
              ),
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
              ElevatedButton(
                child: Text("Register"),
                onPressed: () {
                  print(uc.text);
                  print(pc.text);
                  print(nc.text);
                  register(nc.text, uc.text, pc.text).then((x) {
                    if (x) {
                      Navigator.of(context).push(MaterialPageRoute(
                          builder: (context) => LoginScreen()));
                    } else
                      print("Not Done");
                    //Go to Login
                  });
                },
              ),
            ],
          ),
        ),
      ),
    );
  }
}
