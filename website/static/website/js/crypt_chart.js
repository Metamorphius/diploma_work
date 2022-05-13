function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

window.onload = function () {
    var jsonData = loadJson('#jsonData');

    var data = jsonData.map((item) => item.cost);
    var labels = jsonData.map((item) => item.date);

    var config = {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Основной график',
                backgroundColor: 'blue',
                borderColor: 'blue',
                data: data,
                fill: false,
            }]
        },
        options: {
            responsive: false,
            elements: {
                point: {
                    radius: 0
                }
            }
        }
    };

    var ctx = document.getElementById('cryptChart').getContext('2d');
    window.myLine = new Chart(ctx, config);

    var jsonPredictData = loadJson('#jsonPredictData');

    var pdata = jsonPredictData.map((item) => item.cost);
    var plabels = jsonPredictData.map((item) => item.date);

    var config2 = {
        type: 'line',
        data: {
            labels: plabels,
            datasets: [{
                label: 'Прогноз',
                backgroundColor: 'blue',
                borderColor: 'orange',
                data: pdata,
                fill: false,
            }]
        },
        options: {
            responsive: false,
            elements: {
                point: {
                    radius: 0
                }
            }
        }
        };

        var ctx2 = document.getElementById('secondChart').getContext('2d');
        window.myLine2 = new Chart(ctx2, config2);
};
