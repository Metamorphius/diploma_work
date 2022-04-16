function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

window.onload = function () {
var jsonData = loadJson('#jsonData');

var data = jsonData.map((item) => item.cost);
var labels = jsonData.map((item) => item.date);

var config = {
    type: 'bar',
    data: {
        labels: labels,
        datasets: [{
            label: 'A random dataset',
            backgroundColor: 'blue',
            borderColor: 'lightblue',
            data: data,
            fill: false
        }]
    },
    options: {
      responsive: true
    }
    };

    var ctx = document.getElementById('cryptChart').getContext('2d');
    window.myLine = new Chart(ctx, config);
};