let a = 1;
switch (a) {
  case 1:
    a = "one";
    document.write("<h2>one</h2>");
    break;
  case 2:
    a = "two";
    break;
  default:
    a = "not found";
    break;
}
console.log(`The value is ${a}`);
