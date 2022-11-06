<template>
    <div>
        <div class="card">
            <h5>Basic</h5>
            <Chart type="line" :data="basicData" :options="basicOptions" />
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            basicData: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                datasets: [
                    {
                        label: 'First Dataset',
                        data: [65, 59, 80, 81, 56, 55, 40],
                        fill: false,
                        borderColor: '#42A5F5',
                        tension: .4
                    },
                    {
                        label: 'Second Dataset',
                        data: [28, 48, 40, 19, 86, 27, 90],
                        fill: false,
                        borderColor: '#FFA726',
                        tension: .4
                    },
                    {
                        label: 'Third Dataset',
                        data: [1,10,20,40,60],
                        fill: false,
                        borderColor: 'green',
                        tension: .4
                    }
                ]
            },
            lineStylesData: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                datasets: [
                    {
                        label: 'First Dataset',
                        data: [65, 59, 80, 81, 56, 55, 40],
                        fill: false,
                        tension: .4,
                        borderColor: '#42A5F5'
                    },
                    {
                        label: 'Second Dataset',
                        data: [28, 48, 40, 19, 86, 27, 90],
                        fill: false,
                        borderDash: [5, 5],
                        tension: .4,
                        borderColor: '#66BB6A'
                    },
                    {
                        label: 'Third Dataset',
                        data: [12, 51, 62, 33, 21, 62, 45],
                        fill: true,
                        borderColor: '#FFA726',
                        tension: .4,
                        backgroundColor: 'rgba(255,167,38,0.2)'
                    }
                ]
            },
            basicOptions: {
                plugins: {
                    legend: {
                        labels: {
                            color: '#495057'
                        }
                    }
                },
                scales: {
                    x: {
                        ticks: {
                            color: '#495057'
                        },
                        grid: {
                            color: '#ebedef'
                        }
                    },
                    y: {
                        ticks: {
                            color: '#495057'
                        },
                        grid: {
                            color: '#ebedef'
                        }
                    }
                }
            },
        }
    }
}
</script>