// import 'dart:html';

import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Receive',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Resieve Start Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Material(
      type: MaterialType.transparency,
      child: Stack(
        children: <Widget>[
          Container(
            child: Image.asset(
              'assets/wallpaper.jpg',
              color: Color.fromRGBO(0, 0, 0, 0.5),
              colorBlendMode: BlendMode.srcATop,
              fit: BoxFit.cover,
              height: double.infinity,
              width: double.infinity,
              alignment: Alignment.center,
            ),
          ),
          Container(
            child: Align(
                alignment: Alignment(0.0, 0.25),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Container(
                      child: Image.asset(
                        'assets/scroll.png',
                        width: 75,
                        height: 75,
                        color: Color.fromRGBO(0, 200, 255, 0.65),
                        colorBlendMode: BlendMode.srcATop,
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.fromLTRB(0, 15, 0, 0),
                      child: Text(
                        'Resieve',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          fontSize: 45,
                          color: Color.fromRGBO(0, 200, 255, 1),
                          decorationStyle: TextDecorationStyle.double,
                        ),
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.fromLTRB(0, 10, 0, 0),
                      child: Text(
                        'Filtering texts\nBettering lives',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontWeight: FontWeight.normal,
                          fontSize: 22,
                          fontStyle: FontStyle.italic,
                          color: Color.fromRGBO(0, 200, 255, 1),
                          decorationStyle: TextDecorationStyle.double,
                        ),
                      ),
                    ),
                  ],
                )),
          ),
          Container(
            child: Align(
              alignment: Alignment(0.0, 0.70),
              child: FlatButton(
                onPressed: () {
                  showDialog(
                    context: context,
                    barrierDismissible: false,
                    child: Dialog(
                      backgroundColor: Colors.white.withOpacity(0.85),
                      shape: RoundedRectangleBorder(
                          side: BorderSide.none,
                          borderRadius: BorderRadius.circular(20.0)),
                      child: Container(
                        padding: EdgeInsets.all(20),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            CircularProgressIndicator(
                              backgroundColor: Colors.white,
                              strokeWidth: 5,
                            ),
                            Text(
                              "   Logging You In",
                              style: TextStyle(
                                  fontSize: 20,
                                  fontWeight: FontWeight.bold,
                                  fontStyle: FontStyle.italic,
                                  color: Colors.black),
                            ),
                          ],
                        ),
                      ),
                    ),
                  );

                  // toggleLogginState();
                  // Future.delayed(Duration(seconds: 2), () {
                  //   authService.googleSignIn();
                  //   navigate();
                  // });
                  // .timeout(new Duration(seconds: 3),
                  //     onTimeout: () {
                  //   Scaffold.of(context).showSnackBar(new SnackBar(
                  //       content: Text("Login Failed.")));
                  // });
                },
                child: Container(
                  padding: EdgeInsetsDirectional.only(top: 50),
                  child: Text(
                    'Sign in with Google',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontWeight: FontWeight.normal,
                      fontSize: 22,
                      // fontStyle: FontStyle.italic,
                      color: Color.fromRGBO(0, 200, 255, 1),
                    ),
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
