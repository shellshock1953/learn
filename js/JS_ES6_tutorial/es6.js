window.onload = function() {

    <!-- 2 CONSTANTS -->
    const pi = 3.14;
    function calArea(r){
        console.log("The area is: " + pi * r * r);
    }
    calArea(5);

    <!-- 3 GLOBALS AND LOCALS -->
    <!-- global - var -->
    <!-- local - let -->
    var x = 10;
    if (x > 5) {
        let x = 5;
        console.log("insile x: " + x);
    }
    console.log("outside x: " + x);
    <!-- in this case x will be global -- will return 4 everytime
        var items = document.getElementsByTagName("li")
        for (var x = 0; x < items.length; x++) {
            items[x].onclick = function(){
                console.log(x)
            }
        }
        console.log(x)
    -->
    <!-- in this case x will be local and will works as expected -->
    var items = document.getElementsByTagName("li")
    for (let x = 0; x < items.length; x++) {
        items[x].onclick = function(){
            console.log(x)
        }
    }

    <!-- 4 DEFAULT PARAMS -->
    function log(num=10){
        console.log(num)
    }
    log();
    log(20);
    function logNinja(name="Ray", belt="red", age=20){
        console.log("My name is: " + name +
                    " and my belt is " + belt +
                    " and my age is " + age
                    );
    }
    logNinja();
    logNinja("Shaun", "black", 25);

    <!-- 5 SPREAD OPERATOR -->
    var meats = ["ham", "samali", "becon"]
    console.log(meats)
    console.log(...meats)
    var nums1 = [1, 2, 3]
    var nums2 = [nums1, 4, 5, 6]
    console.log(nums2);
    var nums2 = [...nums1, 4, 5, 6]
    console.log(nums2);

    var nums = [3, 5, 7]
    function addNums(a, b, c){
        console.log(a+b+c);
    }
    addNums(nums);
    addNums(...nums);

    <!--6 TEMPLATE STRINGS -->
    var temp = `hello
     my name is Ruy`; <!-- linebreak -->
    console.log(temp);
    function tempNingja(name, age){
        console.log(`my name is ${name} and next year I will be ${age + 1}`);
    }
    tempNingja("Ryu", 20);

    <!--7 STRING METHODS-->
    var str = "graaavy ";
    console.log(str + " repeat 5: " + str.repeat(5))
    console.log(str + " startWith gra: " + str.startsWith("gra"))
    console.log(str + " startWith not_gra: " + str.startsWith("not_gra"))
    console.log(str + " endsWith 'vy ': " + str.endsWith("vy "))
    console.log(str + " endsWith vy str.length-1: " + str.endsWith("vy", str.length - 1))
    console.log(str + " includes aaa: " + str.includes("aa"))
    console.log(str + " includes 111: " + str.includes("11"))

    <!-- 8 Obj Literal Enh -->
    var name = "Crystal";
    var belt = "Black";
    var ninja = {
        name, belt,
        chop: function(x){  console.log(`you chopped the enemy ${x} times`); }, // old method
        killed(y){          console.log(`you killed ${y} enemies`) } // new method
    };
    console.log(ninja.name + " " + ninja.belt);
    console.log(ninja.chop(5));
    console.log(ninja.killed(2));

    <!-- 9 Arrow Functions -->
    var ninjaGreetings = function(){
        console.log("hiiiiya") // old method
    };
    ninjaGreetings();

    var ninjaGreetings = name => console.log(`hiiiiya ${name}`); // new method
    var ninjaAnotherGreetings = (name, caller) => console.log(`hiiiiya ${name} from ${caller}`); // new method
    ninjaGreetings("Mark");
    ninjaAnotherGreetings("Mark", "Steeve");
    var ninja = {
        name: "Ryu",
        chop(x){
//       OLD
//            var _this = this;
//            window.setInterval(function(){ // this will be overriten here - need to store it to _this
//                if (x > 0){
//                    console.log(_this.name + " chopped the enemy"); //_this, because normal this in binden by inner functuin |
//                    x--;
//                }
//            }, 1000);
//      NEW
            window.setInterval(() => { // no inner func - arrow not calls function() so this will work and will not be overriten
                if (x > 0){
                    console.log(this.name + " chopped the enemy");
                    x--;
                }
            }, 1000);

        }
    };
    ninja.chop(5);

    <!-- 10 Sets -->
    var names = new Set();
    names.add("Ryu").add("Ryu").add("Crystal").add("Test"); // deletes duplicates
    console.log(names.size);
    console.log(names.delete("Test")); // cant names.delete().delete() like names.add().add()

    console.log(names.has("Crystal"))

    console.log(names.size);
    console.log(names);

    names.clear()
    console.log(names.size);

    var ninjas = ["shaun", "crystal", "yoshi", "ruy", "yoshi", "ruy"]
    var refindNinjas = new Set(ninjas);
    console.log(refindNinjas); // removes duplicates
    ninjas = [...refindNinjas];  // spread operator - converst into list
    console.log(ninjas);

    <!-- 11 Generators --> // great for async
    function* gen(){ // is no generator - returns iterator
        console.log("pear");
        console.log("banana");
        console.log("apple");
    }
    var myGen = gen();
    myGen.next();

    function* gen1(){
        yield console.log("pear"); // will call here, but not next on iter
        yield console.log("banana"); // will work without second yield
        yield console.log("apple");
        console.log("all done")
    }
    var myGen1 = gen1();
    myGen1.next(); // pear
    myGen1.next(); // banana
    myGen1.next(); // apple
    myGen1.next(); // all-done

    function* gen2(){
        yield "pear";
        yield "banana";
        yield "apple";
        return "all done";
    }
    var myGen2 = gen2();
    console.log(myGen2.next());
    console.log(myGen2.next());
    console.log(myGen2.next());
    console.log(myGen2.next());

    function* gen3(){
        var x = yield "pear";
        var y = yield "banana";
        var z = yield "apple";
        return x + y + z;
    }
    var myGen3 = gen3();
    console.log(myGen3.next());
    console.log(myGen3.next(10));
    console.log(myGen3.next(5));
    console.log(myGen3.next(3));


}