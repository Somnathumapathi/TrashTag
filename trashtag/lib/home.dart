import 'package:barcode_scan/barcode_scan.dart';
import 'package:flutter/material.dart';
import 'package:toast/toast.dart';
import 'package:trashtag/server.dart';

class Home extends StatefulWidget {
  const Home({Key key}) : super(key: key);

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String productKey;
  String garbageKey;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("TrashTag Home"),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Center(
            child: InkWell(
              onTap: () async {
                //Scan Product
                String pKey = await BarcodeScanner.scan(); //barcode scnner
                setState(() {
                  productKey = pKey;
                });
                //Scan Garbage
                String gKey = await BarcodeScanner.scan(); //barcode scnner
                setState(() {
                  garbageKey = gKey;
                });

                add2dustbin(productKey, garbageKey).then((x) {
                  print("You recieved $x Coins");
                  Toast.show("You recieved $x Coins", context,
                      duration: Toast.LENGTH_LONG, gravity: Toast.BOTTOM);
                });
              },
              child: CircleAvatar(
                  radius: 70,
                  child: Icon(
                    Icons.delete_outline,
                    size: 50,
                  )),
            ),
          ),
          SizedBox(height: 20.0),
          Text("$productKey\n$garbageKey")
        ],
      ),
    );
  }
}
