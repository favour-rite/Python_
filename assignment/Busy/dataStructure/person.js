const Human = require("./Human");

class Person extends Human{
    #money
    #gender
   
    constructor(name,age,money,gender){
        super(money,name,age);
        this.#money = money;
        this.#gender = gender;
    }

    
}
let personOne = new Person("Skye","old enough","All Currency","Female");
console.log(personOne);