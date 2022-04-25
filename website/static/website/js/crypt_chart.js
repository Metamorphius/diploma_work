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
            borderColor: 'red',
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
};