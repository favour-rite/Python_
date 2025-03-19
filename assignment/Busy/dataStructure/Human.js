class Human{
    #name;
    #age;

    constructor(name,age){
        this.#name = name;
        this.#age = age;
    }
    setname(name){
        this.name = name;
    }
    getname(){
        return this.name;
    }
    moneyHurting(){ 
        moneyChaseValue = true;
    }
    
}
let personOne = new Human("chinedu", 12);
console.log(personOne.firstName)

module.exports = Human;
