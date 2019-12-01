var myMap;

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
    } else if (id == "01" || id == "10" || id == "11") {
        return 'islands#yellowIcon'
    } else if (id == "20") {
        return 'islands#greenIcon'
    } else if (id == "02") {
        return 'islands#blueIcon'
    }
}

// Возвращает лейбл для точки
function getMarkerInfo(id) {
    if (id == "00") {
        return 'Нет постамата и нет выдачи на кассе'
    } else if (id == "01") {
        return 'Нет постамата и есть выдача на кассе'
    } else if (id == "10") {
        return 'Есть постамат и нет выдачи на кассе'
    } else if (id == "11") {
        return 'Есть постамат и есть выдача на кассе'
    } else if (id == "20") {
        return "Здесь выгодно поставить постамат"
    } else if (id == "02") {
        return "Здесь выгодно поставить выдачу на кассе"
    }
}

function init() {
    myMap = new ymaps.Map("map", {
        zoom: 7,
        bounds: ymaps.util.bounds.fromPoints(coords)
    });

    for (var i = 0; i < coords.length; i++) {
        if (coords[i].length > 3) {
            var myPlacemark = new ymaps.Placemark(coords[i], {
                hintContent: getMarkerInfo(coords[i][2]),
                balloonContentHeader: getMarkerInfo(coords[i][2]),
                balloonContent: coords[i][3]
            }, {
                preset: getMarkerColor(coords[i][2])
            });
        } else {
            var myPlacemark = new ymaps.Placemark(coords[i], {
                hintContent: getMarkerInfo(coords[i][2]),
                balloonContentHeader: getMarkerInfo(coords[i][2])
            }, {
                preset: getMarkerColor(coords[i][2])
            });
        }

        myMap.geoObjects.add(myPlacemark)

        if (coords[i][2] == "00") {
            myPlacemark.options.set("visible", false)
        }
    }
}

document.addEventListener("click", e => {
    if (e.target && e.target.closest(".map")) {
        // Получаем все точки, цвет которых совпадает с чек боксом
        var result = ymaps.geoQuery(myMap.geoObjects)
            .search('options.preset = "islands#' + e.target.id + '"')

        // Прячем или показываем точки
        result.setOptions('visible', e.target.checked);
    }
})