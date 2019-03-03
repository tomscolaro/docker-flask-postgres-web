var something = document.getElementById('something');

something.style.cursor = 'pointer';
something.onclick = function() {
    // do something...
};


something.onmouseover = function() {
    this.style.backgroundColor = 'green';
};
something.onmouseout = function() {
    this.style.backgroundColor = '';
};
