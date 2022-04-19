
$(window).on('load', function() {
    $('.ring').css('visibility', 'visible');
    $('.ring').delay(1000).fadeOut(500);
    $('#starting-win img').delay(1000).fadeOut(1000);
    $('#starting-win').delay(2000).fadeOut(1000);
    $('#main').css("background-image", "url(http://www.zrmin.top:8000/static/images/webos/1.jpg)");

    $('.ring').css('visibility', 'visible');
    $('.ring').fadeOut();
    $('#starting-win img').fadeOut();
    $('#starting-win').fadeOut();
    $('#main').css('background-image', 'url(http://www.zrmin.top:8000/static/images/webos/1.jpg)');

    if (
        localStorage.getItem('name') == null ||
        localStorage.getItem('name') == '' ||
        localStorage.getItem('name') == 'undefined'
    ) {

        name = prompt('Enter Your Nick Name(Maximum limit 8)') || 'My PC';
        while(name.length > 8){
            alert("Keep the Name length to 8 chars or less")
            name = prompt('输入你的昵称（不超过8位）');
        }



        if (typeof Storage !== 'undefined') {

            localStorage.setItem('name', name);

            document.getElementById('name').innerHTML = localStorage.getItem('name');
        } else {
            document.getElementById('name').innerHTML = 'This PC';
        }
    } else {
        document.getElementById('name').innerHTML = localStorage.getItem('name');
        $('#main').css(
            'background-image',
            'url(http://www.zrmin.top:8000/static/images/webos/1.jpg))'
        );
    }
});


var mouse_is_inside = true;
$(document).ready(function() {
    $('body').mouseup(function() {
        if (!mouse_is_inside)
            $('.desktop-item').css('background-color', 'transparent');
        hovered = false;
        selected = false;
    });
});


var selected;
function selectedItem(a) {
    a.style.background = 'rgba(255, 255, 255, .4)';
    mouse_is_inside = false;
    selected = true;
}


var hovered;
function hoveredItem(a) {
    if (!selected) {
        a.style.background = 'rgba(255, 255, 255, .2)';
    }
    mouse_is_inside = false;
    hovered = true;
}


function hoveredOut(a) {
    if (hovered && !selected) {
        a.style.background = 'rgba(255, 255, 255, 0)';
        mouse_is_inside = false;
        hovered = false;
    }
}


dragElement(
    document.getElementById('tab'),
    document.getElementById('tab-header')
);
dragElement(
    document.getElementById('tab-calc'),
    document.getElementById('tab-calc-header')
);
dragElement(
    document.getElementById('tab-todo'),
    document.getElementById('tab-todo-header')
);

function dragElement(elmnt, eH) {
    var pos1 = 0,
        pos2 = 0,
        pos3 = 0,
        pos4 = 0;
    eH.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
        e = e || window.event;

        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;

        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e = e || window.event;

        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;

        elmnt.style.top = elmnt.offsetTop - pos2 + 'px';
        elmnt.style.left = elmnt.offsetLeft - pos1 + 'px';
    }

    function closeDragElement() {

        document.onmouseup = null;
        document.onmousemove = null;
    }
}


setTimeout(function() {
    setInterval(function() {
        var hours = new Date().getHours();
        var merid;
        if (hours > 12) {
            hours = hours - 12;
            merid = 'PM';
        } else {
            merid = 'AM';
        }

        var minutes = new Date().getMinutes();

        minutes = (minutes < 10 ? '0' : '') + minutes;

        var today = new Date();
        var dd = today.getDate();
        var mm = today.getMonth() + 1;

        var yyyy = today.getFullYear();
        var today = mm + '/' + dd + '/' + yyyy;

        $('#clock').html(hours + ':' + minutes + ' ' + merid + '<br>' + today);
    }, 1000);
}, 1000);

var tab = document.getElementById('main');
var starting = document.getElementById('starting-win');

if (starting.addEventListener) {
    starting.addEventListener(
        'contextmenu',
        function(e) {
            e.preventDefault();
        },
        false
    );
}

if (tab.addEventListener) {
    tab.addEventListener(
        'contextmenu',
        function(e) {
            $('#body-rmenu').toggleClass('hide');
            $('#body-rmenu').css({
                position: 'absolute',
                top: e.pageY,
                left: e.pageX
            });

            e.preventDefault();
        },
        false
    );
}


$(document).bind('click', function(event) {
    document.getElementById('body-rmenu').className = 'hide';
});



function changeBg(number) {

    if (typeof Storage !== 'undefined') {

        localStorage.setItem('wp', number);
        $('#main').css(
            'background-image',
            'url(http://www.zrmin.top:8000/static/images/webos/' + number + '.jpg)'
        );
    } else {
        $('#main').css(
            'background-image',
            'url(http://www.zrmin.top:8000/static/images/webos/1.jpg)'
        );
    }
}






function toggleFullScreen() {
    if ((document.fullScreenElement && document.fullScreenElement !== null) ||
        (!document.mozFullScreen && !document.webkitIsFullScreen)) {
        if (document.documentElement.requestFullScreen) {
            document.documentElement.requestFullScreen();
        } else if (document.documentElement.mozRequestFullScreen) {
            document.documentElement.mozRequestFullScreen();
        } else if (document.documentElement.webkitRequestFullScreen) {
            document.documentElement.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
        }
    } else {
        if (document.cancelFullScreen) {
            document.cancelFullScreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.webkitCancelFullScreen) {
            document.webkitCancelFullScreen();
        }
    }
}
