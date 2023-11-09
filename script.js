$(document).ready(function() {
    $('#piDigitsForm').submit(function(e) {
        e.preventDefault();
        var digits = $('#digits').val();
        var pi = math.pi(digits);
        $('#piDigitsResult').text(pi);
    });
});
