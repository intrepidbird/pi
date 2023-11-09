$(document).ready(function() {
    $('#digitsForm').submit(function(e) {
        e.preventDefault();
        let digits = $('#digits').val();
        if (digits > 0) {
            let pi = calculatePi(digits);
            $('#piResult').text(`The first ${digits} digits of Pi are: ${pi}`);
        } else {
            $('#piResult').text('Please enter a valid number of digits.');
        }
    });

    function calculatePi(digits) {
        let pi = Math.PI.toFixed(digits);
        return pi;
    }
});
