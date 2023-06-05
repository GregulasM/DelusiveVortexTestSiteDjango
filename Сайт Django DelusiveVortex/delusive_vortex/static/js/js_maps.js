

var granimInstance = new Granim({
    element: '#canvas-image-blending',
    direction: 'top-bottom',
    isPausedWhenNotInView: false,
    image: {
        source: '../../static/images/background2.png',
        position: ['center', 'top'],
        stretchMode: ['stretch', 'stretch-if-bigger'],
        blendingMode: 'multiply'
    },
    states: {
        "default-state": {
            gradients: [
                ['#29323c', '#485563'],
                ['#FF6B6B', '#556270'],
                ['#80d3fe', '#7ea0c4'],
                ['#625876', '#5c7173']
            ],
            transitionSpeed: 7000
        }
    }
});



function switchTab(tabName, event) {
    event.preventDefault();
    var tabs = document.getElementsByClassName('tab-content');
    for (var i = 0; i < tabs.length; i++) {
        tabs[i].style.display = 'none';
    }


    
    // Показываем выбранную вкладку
    var tab = document.getElementById(tabName);
    if (tab) {
        tab.style.display = 'block';
    }
}


$('.multiple-items').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1500,
    dots: true,
    TouchMove: true
});