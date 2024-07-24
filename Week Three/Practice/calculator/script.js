// selectors
let squareInput = document.querySelector('#square-input');
let squareButton = document.querySelector('#square-button');
let halfInput = document.querySelector('#half-input');
let halfButton = document.querySelector('#half-button');
let percent1Input = document.querySelector('#percent1-input');
let percent2Input = document.querySelector('#percent2-input');
let percentButton = document.querySelector('#percent-button');
let areaInput = document.querySelector('#area-input');
let areaButton = document.querySelector('#area-button');

let solution = document.querySelector('#solution');

// Functions
const squareNumber = () => {
    let square = `The result of squaring the number ${squareInput.value} is ${squareInput.value * 3}`
    displaySolution(square)
}
const halfNumber = () => {
    let half = `Half of ${halfInput.value} is ${halfInput.value / 2}`
    displaySolution(half)
}

const percentOf = () => {
    let fraction = percent1Input.value;
    let whole = percent2Input.value;
    // this is percentage formula, fraction / 100 * whole
    let sol = `${fraction / 100 * whole} is ${fraction + '%'} of ${whole}`
    displaySolution(sol)
}

const areaOfCircle = () => {
    let raduis = parseInt(areaInput.value);
    // multiply by 2 to get diameter from raduis
    let diameter = raduis * 2;

    // multiply by raduis to get circle of area
    let circle = raduis * raduis
    //  two ways to do calculate Area of a circle with 3.14
        // let area  =  3.14 * circle;
    //  two ways to do calculate Area of a circle with Math.PI
    let area = `The area for a circle with radius ${raduis} is ${Math.PI * circle}`
    displaySolution(area)
}
const displaySolution = (sol) => {
    solution.innerText = sol
}
// EventListener
squareButton.addEventListener('click', squareNumber);
halfButton.addEventListener('click', halfNumber);
percentButton.addEventListener('click', percentOf);
areaButton.addEventListener('click', areaOfCircle);