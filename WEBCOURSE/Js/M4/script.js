// ordinary
function ordinary(variable) {
  console.log(variable);
}
ordinary(2);

// arrow fn with single argument
let myarrow = (a) => console.log(a);

myarrow(2);

// arrow fn with two arguments
let myArrowTwo = (a, b) => console.log(a, b);

myArrowTwo(1, 2);

// arrow fn no arguments
let myArrow = () => console.log("empty fn");

myArrow();

// arrow fn as expression
let mark = 10;
let checkFunction =
  mark > 40 ? () => console.log(pass) : () => console.log("fail");
checkFunction();

// muliline arrow fn

let sum = (a, b) => {
  let result = a + b;
  return result;
};

let result = sum(1, 2);
console.log(result);
