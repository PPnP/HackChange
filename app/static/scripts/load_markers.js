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
        return {
            preset: 'islands#redIcon' 
        }
    } else if (id == "01") {
        return {
            preset: 'islands#blueIcon'
        }
    } else if (id == "10") {
        return {
            preset: 'islands#yellowIcon'
        }
    } else if (id == "11") {
        return {
            preset: 'islands#greenIcon'
        }
    } else if (id == "20") {
        return {
            iconLayout: 'default#image',
            iconImageHref: "/static/images/postamat.png",
        }
    } else if (id == "02") {
        return {
            iconLayout: 'default#image',
            iconImageHref: "/static/images/cashbox.png",
        }
    }
}

function getMarkerInfo(id) {
    if (id == "00") {
        return 'Нет постамата и нет выдачи на кассе'
    } else if (id == "01") {
        return 'Нет постамата и есть выдача на кассе'
    } else if (id == "10") {
        return 'Есть постамат и нет выдачи на кассе'
    } else if (id == "11") {
        return 'Есть постамат и есть выдача на кассе'
    } 
}

function init() {
    let myMap = new ymaps.Map("map", {
        center: [51.5, 36],
        zoom: 7
    });

    for (var i = 0; i < coords.length; i++) {
        var myPlacemark = new ymaps.Placemark(coords[i], {
            hintContent: getMarkerInfo(coords[i][2]),
            balloonContentHeader: getMarkerInfo(coords[i][2])
        }, getMarkerColor(coords[i][2]));
    
        myMap.geoObjects.add(myPlacemark)
    }
}