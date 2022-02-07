// Team HAM :: Hebe Huang, Andrew Juang, Michelle Lo
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


// var fact = function(n){
//   if(n == 0){
//     return 1;
//   }
//   return fact(n-1) * n;
// };

var fact = (n) => {
  if(n == 0){
    return 1;
  }
  return fact(n-1) * n;
};

var fib = function(n){
  if(n <= 1){
    return n;
  }
  return fib(n-1) + fib(n-2);
};

console.log(fact(0)); // 1
console.log(fact(1)); // 1
console.log(fact(2)); // 2
console.log(fact(5)); // 120

console.log(fib(0)); // 0
console.log(fib(1)); // 1
console.log(fib(2)); // 1
console.log(fib(5)); // 5


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
