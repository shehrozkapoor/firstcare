const data = [
    [1, 'Raj', 'IT', 8, 'Xyz@email.com'],
    [2, 'Timir', 'CSE', 4, 'Xyz@email.com'],
    [4, 'Arjesh', 'IT', 2, 'Xyz@email.com'],
    [5, 'Haris ali', 'IT', 6, 'Xyz@email.com'],
    [6, 'Deepak', 'CSE', 4, 'Xyz@email.com'],
    [7, 'Dibyendu', 'ECE', 4, 'Xyz@email.com'],
    [8, 'Aman', 'IT', 4, 'Xyz@email.com'],
    [9, 'Binayak', 'CSE', 6, 'Xyz@email.com'],
    [10, 'Harshad', 'ECE', 6, 'Xyz@email.com'],
    [11, 'Abhra', 'IT', 4, 'Xyz@email.com'],
]

let container = document.querySelector('.handsontable-container');

let hot = new Handsontable(container, {
    data: data,
    colHeaders: ['roll', 'name', 'stream', 'semester', 'email'],
    rowHeaders: true,
    dropdownMenu: true,
    filters: true,
})