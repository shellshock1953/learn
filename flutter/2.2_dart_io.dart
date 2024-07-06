import 'dart:io';

void main() {
  stdout.writeln('Hello someone');
  // String input = stdin.readLineSync(); // type error
  dynamic input = stdin.readLineSync();
  return helloDart(input);
}

void helloDart(String name) {
  print('Hello, $name');
}
