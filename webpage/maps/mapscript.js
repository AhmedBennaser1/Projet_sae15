
function displayInIframe(hour) {
   
    
    var path = "/webpage/maps/maps/"
    var pages = {
        0: path + 'map_h'+hour+'.html',
        1: path + 'map_h'+ hour+ '.html',
        2: path + 'map_h'+ hour+ '.html',
        3: path + 'map_h'+ hour+ '.html',
        4: path + 'map_h'+ hour+ '.html',
        5: path + 'map_h'+ hour+ '.html',
        6: path + 'map_h'+ hour+ '.html',
        7: path + 'map_h'+ hour+ '.html',
        8: path + 'map_h'+ hour+ '.html',
        9: path + 'map_h'+ hour+ '.html',
        10: path + 'map_h'+ hour+ '.html',
        11: path + 'map_h'+ hour+ '.html',
        12: path + 'map_h'+ hour+ '.html',
        13: path + 'map_h'+ hour+ '.html',
        14: path + 'map_h'+ hour+ '.html',
        15: path + 'map_h'+ hour+ '.html',
        16: path + 'map_h'+ hour+ '.html',
        17: path + 'map_h'+ hour+ '.html',
        18: path + 'map_h'+ hour+ '.html',
        19: path + 'map_h'+ hour+ '.html',
        20: path + 'map_h'+ hour+ '.html',
        21: path + 'map_h'+ hour+ '.html',
        22: path + 'map_h'+ hour+ '.html',
        23: path + 'map_h'+ hour+ '.html',
        24: path + 'map_h'+ hour+ '.html',
    };
    
    var href = pages[hour];
    if (!href) {
        console.log("Aucune page n'est assignée pour " + hour + "h.");
    }

    console.log("Affichage de la page " + href + " pour l'heure " + hour + "h.");

    var iframe = document.getElementById('content-frame');
    iframe.src = href;
}
window.onload = function() {
    
    displayInIframe(0);

    var slider = document.getElementById("hour-slider");
    var output = document.getElementById("slider-value");
    slider.value = 0;
    output.innerHTML = "0h";

    slider.oninput = function() {
        output.innerHTML = this.value + "h";
        displayInIframe(this.value); 
    }
}