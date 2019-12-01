var xhr = new XMLHttpRequest();
xhr.open('GET', '/data', false);
xhr.send();

if (xhr.status != 200) {
    alert("Ошибка запроса маркеров.")
} else {
    // вывести результат
    coords = JSON.parse(xhr.responseText) // responseText -- текст ответа.
}

// Функция ymaps.ready() будет вызвана, когда
// загрузятся все компоненты API, а также когда будет готово DOM-дерево.
ymaps.ready(init);

function getMarkerColor(id) {
    if (id == "00") {
        return 'islands#redIcon'
    } else if (id == "01") {
        return 'islands#blueIcon'
    } else if (id == "10") {
        return 'islands#greenIcon'
    } else if (id == "11") {
        return 'islands#yellowIcon'
    }
}

function init() {
    let myMap = new ymaps.Map("map", {
        center: [51.5, 36],
        zoom: 7
    });

    for (var i = 0; i < coords.length; i++) {
        var myPlacemark = new ymaps.Placemark(coords[i], {}, {
            preset: getMarkerColor(coords[i][2])
        });
    
        myMap.geoObjects.add(myPlacemark)
    }
}