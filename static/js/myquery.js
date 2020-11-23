var flashInterval;

$('#contact').hover(
    function () {
        flashInterval = setInterval(function () {
            $('#contact').toggleClass('red-border');
        }, 1000);
    }, function () {
        clearInterval(flashInterval);
        $('#contact').removeClass('red-border');
    });