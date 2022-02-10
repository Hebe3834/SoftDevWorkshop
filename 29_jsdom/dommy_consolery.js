// Team HAMS :: Hebe Huang, Andrew Juang, Michelle Lo, Shadman Rakib
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-09t
// --------------------------------------------------
//

//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO"); //ayo

var i = "hello";
var j = 20;
console.log(i) //sends "hello" to console
console.log(j) //sends 20 to console

//assign an anonymous fxn to a var
var f = function(x) {
  var j=30; //j is 30 only in the scope of this function (otherwise, it would be 20).
  return j+x;
};
console.log(f(i)) //30hello
console.log(f(j)) //50


//instantiate an object
//similar to a dictionary!
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) { //alternative way of defining a function
            return x+30;
          }
        };
//console.log(o) //will print the object in the console

//can print specific aspects of an object (instance variables in java terms)
//using the syntax used to get the value of a key in a dictionary.
console.log(o.age) //15
console.log(o.items[1]) //20
console.log(o.morestuff.b) //ayo
console.log(o.func(j)) //50
console.log(o.func(i)) //hello30



var addItem = function(text) {
  var list = document.getElementById("thelist"); //corresponds to an element on the html file called "thelist"
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};
addItem("NEW ITEM") //adds a new item called "new item"
addItem(3) //also allows numbers


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};
removeItem(9) //removes previously added 3
//removeItem(10) //produces error


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};
red() //will turn the first and last elements red
//li elements whose class lists are either empty or have red at the end will be red.
//there seems to be an order of importance for colors as defined in the style sheet: red < green < blue.


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};
stripe()

//insert your implementations here for...
// FIB
let fib = function(n){
    if(n <= 1){
      return n;
    }
    return fib(n-1) + fib(n-2);
  };

// FAC
var fact = function(n){
    if(n == 0){
    return 1;
    }
    return fact(n-1) * n;
};

// GCD
let gcd = function (a, b) {
    if (a == 0) return b;
    if (b == 0) return a;
    while (1) {
        if (b > a) {
            b %= a;
        } else {
            a %= b;
        }
        if (a == 0) return b;
        if (b == 0) return a;
    }
}
console.log(gcd(12, 6));

//
// let fibEx = fib(10);
// addItem("The 10th fibonacci number is " + fibEx);
//
// let factEx = fact(10);
// addItem("10! = " + factEx);
//
// let gcdEx = gcd(990, 99);
// addItem("GCD of 990 and 99 is " + gcdEx);

let num1 = document.getElementById("num1").value;
let num2 = document.getElementById("num2").value;

const btn1 = document.getElementById("fibBtn");
btn1.addEventListener("click", (e) => {
  num1 = document.getElementById("num1").value;
  num2 = document.getElementById("num2").value;
  let fibEx = fib(num1);
  addItem("Fibonacci number " + num1 + ": " + fibEx);
  fibEx = fib(num2);
  addItem("Fibonacci number " + num2 + ": " + fibEx);
});

const btn2 = document.getElementById("factBtn");
btn2.addEventListener("click", (e) => {
  num1 = document.getElementById("num1").value;
  num2 = document.getElementById("num2").value;
  let factEx = fact(num1);
  addItem(num1 + "! = " + factEx);
  factEx = fact(num2);
  addItem(num2 + "! = " + factEx);
});

const btn3 = document.getElementById("gcdBtn");
btn3.addEventListener("click", (e) => {
  num1 = document.getElementById("num1").value;
  num2 = document.getElementById("num2").value;
  let gcdEx = gcd(num1, num2);
  addItem("GCD of " + num1 + " and " + num2 + " is " + gcdEx);
});
