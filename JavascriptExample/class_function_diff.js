// class Person {
//   constructor(name){
//     this.name = name
//   }
// }

// class Student extends Person {
//   constructor(name, school) {
//     super(name)
//     this.school = school;
//   }
// }

// const student = new Student('홍길동', '동국')
// console.log(student);

function Person(name) {
  this.name = name;
}

function Student(name, school) {
  Person.call(this, name);
  this.school = school;
}

Student.prototype = Object.create(Person)
Student.prototype.constructor = Student 

console.dir(Student)

const student = new Student('홍길동', '동국')
console.log(student);