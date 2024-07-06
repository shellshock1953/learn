import 'dart:io';

void main() {
  // twoone();
  files();
}

void helloDart(String name) {
  print('Hello $name');
}

void twoone() {
  List<String> greetings = ['World', 'Mars', 'Moon'];
  for (var name in greetings) {
    helloDart(name);
  }
  print("\nand now forEach\n");
  greetings.forEach((greeting) => helloDart(greeting));

  List<int> smallNums = [1, 2, 3];
  Iterable<int> biggerNums = smallNums.map((e) => e * 2);
  print('$biggerNums');
}

void files() {
  final String show = "SHOW";
  List<String> files = [];
  var systemTemp = Directory.systemTemp;
  systemTemp.list().listen((FileSystemEntity entity) {
    files.add(entity.path);
  });
  print("this is : $show");
}
