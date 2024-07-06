void main() {
  final String s_one = "1";
  final String ss_one = "1.1";
  final upperString = "should be apper";
  var i_one = int.parse(s_one);
  var d_one = double.parse(ss_one);
  // another way
  // String oneAsString = 1.toString();
  // String piAsString = 3.14159.toStringAsFixed(2);
  assert(i_one == 1);
  print("int:$i_one, fload:$d_one. Expr:${upperString.toUpperCase()}\n" +
      "yes, + is working");

  var trueValue = 'exists';
  // This will NOT work -- string != bool
  // if (trueValue) {
  //   print('true');
  // };
  if (trueValue.isNotEmpty) {
    print("not empty");
  }

  var list = [1, 2, 3];
  print("List: $list");
  // print(addToList(list));
  assert(list[1] == 1, "here im fails");
  var map = {'one': 1};
  var newMap = Map();
  newMap["one"] = 1;
  print("map length: ${map.length}\nnewMap length: ${newMap.length}");

  funcWithNamed("first", "second");
  funcWithNamedDefaults(two: "override");
  funcWithOptional("one", "two");

  func2func();

  simpleIter(list);
  simpeForEach(list);
  simpeForIn(list);

  caseExample("APPROVED");
  caseExample("default value");
}

void funcWithNamed(String one, String two) {
  // Func with names args
  print("Named\t\t1:$one, 2:$two");
}

void funcWithNamedDefaults(
    {String one: "firstDefault", String two: "secondsDefault"}) {
  // Func with defaults
  print("Defaults\t1:$one, 2:$two");
}

String funcWithOptional(String one, [String two = "two"]) {
  // Func with optional
  print("Optional\t:$one, 2:$two");
  return one;
}

void func2func() {
  printElement(element) {
    print(element);
  }

  var list = [1, 2, 3];
  list.forEach(printElement);
}

void simpleIter(List list) {
  for (var i = 0; i < list.length; i++) print("List: $i");
}

void simpeForEach(List list) {
  list.forEach((i) => print("Each: $i"));
}

void simpeForIn(List list) {
  // only for List and Set
  for (var i in list) {
    print("ForIn: $i");
  }
}

void caseExample(String action) {
  final String dontTouchMe = "hands off!";
  switch (action) {
    case 'CLOSED':
      print("cls");
      break;
    case 'PENDING':
      print("pnd");
      break;
    case 'APPROVED':
      print("apprv");
      break;
    case 'DENIED':
      print("dnd");
      break;
    case 'OPEN':
      // continue label;
      print("opn");
      break;
    default:
      // throw new Exception("no defaults");
      // try {
      //   dontTouchMe = "hags";
      // } catch(e) {
      //   print("error: $e");
      // } finally {
      print("out");
    // }
  }
}

List addToList(List list) {
  List result = [];
  for (var i in list) {
    result.add(i + 1);
  }
  return result;
}
