
$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $(this).toggleClass('active');
    });
});


// Sample data for the pie chart
var pieData = {
labels: ['Label 1', 'Label 2', 'Label 3'],
datasets: [{
data: [30, 40, 30], // Sample data percentages (e.g., 30%, 40%, 30%)
backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'], // Colors for each segment
}]
};

// Options for the pie chart
var pieOptions = {
responsive: true,
maintainAspectRatio: true,
legend: {
position: 'bottom',
}
};

// Get the canvas element
var ctx = document.getElementById('myPieChart').getContext('2d');

// Create the pie chart
var myPieChart = new Chart(ctx, {
type: 'pie',
data: pieData,
options: pieOptions
});
