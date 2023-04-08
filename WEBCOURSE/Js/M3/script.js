// fn for add two numbers

function sum(a, b, c) {
  console.log("sum is", a + b + c);
}

sum(1, 2, 3);

function sumReturn(a, b) {
  return a + b;
}

let result = sumReturn(30, 40);

document.write(`<h2> result is ${result}</h2>`);
console.log(result);
