const ctx = document.getElementById('account_recieveable_chart').getContext('2d');
const account_recieveable_chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['0-30', '31-60', '61-90', '91-120', '121+', 'ALL'],
        datasets: [{
            label: 'Patient',
            data: [1, 2, 3, 4, 5, 6],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 1
        },
        {
            label: 'Insurance Company',
            data: [7,8,9, 10,11,12],
            backgroundColor: [
                'rgba(54, 162, 235, 1)',
            ],
            borderColor: [
            'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});