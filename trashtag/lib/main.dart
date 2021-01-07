import 'package:flutter/material.dart';
import 'package:trashtag/login.dart';
import 'package:trashtag/register.dart';
import 'package:trashtag/scan.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'TrashTag',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: TrashTagApp(),
    );
  }
}

class TrashTagApp extends StatelessWidget {
  const TrashTagApp({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("TrashTag"),
      ),
      body: Center(
        child: Container(
          padding: EdgeInsets.all(20),
          child: Column(
            children: [
              RaisedButton(
                onPressed: () {
                  Navigator.of(context).push(
                      MaterialPageRoute(builder: (contet) => LoginScreen()));
                },
                child: Text("Login"),
              ),
              RaisedButton(
                onPressed: () {
                  Navigator.of(context).push(
                      MaterialPageRoute(builder: (contet) => RegisterScreen()));
                },
                child: Text("Register"),
              )
              // SizedBox(
              //   height: 20,
              // ),
              // RaisedButton(
              //   onPressed: () {
              //     Navigator.of(context)
              //         .push(MaterialPageRoute(builder: (contet) => ScanPage()));
              //   },
              //   child: Text("QR Test"),
              // )
            ],
          ),
        ),
      ),
    );
  }
}
