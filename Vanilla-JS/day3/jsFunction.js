function sayHello(name) {
  console.log("Hello!", name, "!");
}

function sayHi(name) {
  return `Hi, ${name}!`
}

sayHello("Wonpyo")
const hiJeon = sayHi("Jeon")
console.log(hiJeon)

const calculator = {
  plus: function(a, b) {
      return a + b;
  }
}

const plus = calculator.plus(5, 5)
console.log(plus)
