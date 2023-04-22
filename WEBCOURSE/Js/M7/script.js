let a = 10;
switch (a) {
  case 1:
    a = "one";
    document.write("<h2>one</h2>");
    break;
  case 2:
    a = "two";
    document.write("<h2>two</h2>");
    break;
  default:
    a = "not found";
    document.write("<h2>wrong option</h2>");

    break;
}
console.log(`The value is ${a}`);

// let choice = value;
// switch (choice) {
//   case 1:
//     // execution  code
//     break;
//   case 2:
//     // execution  code
//     break;
//   default:
//     // execution  code
//     break;
// }
// // console.log(`The value is ${a}`);
