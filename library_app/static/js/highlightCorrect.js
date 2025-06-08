const inputs = document.querySelectorAll('.correct-answer');
const labels = document.querySelectorAll('.correct-label');

console.log(inputs, labels);

for (let count = 0; count < inputs.length; count++) {
    const input = inputs[count];
    const label = labels[count];

    input.addEventListener('focus', () => {
        label.classList.add('focus');
        // alert('fff')
    });
}
