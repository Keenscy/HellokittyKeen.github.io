$(document).ready(function() {
    $.ajax({
        url: 'http://tu-servicio-web/kitten',
        type: 'GET',
        success: function(data) {
            var canvas = document.getElementById('kittenCanvas');
            var ctx = canvas.getContext('2d');
            var img = new Image();
            img.onload = function() {
                ctx.drawImage(img, 0, 0);
            };
            img.src = 'data:image/png;base64,' + data;
        }
    });
});