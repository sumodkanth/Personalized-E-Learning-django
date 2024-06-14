// Main JavaScript file

// Function to toggle sidebar
function toggleSidebar() {
    document.getElementById("sidebar").classList.toggle("active");
}

// Event listener for sidebar toggle button
document.getElementById("sidebarCollapse").addEventListener("click", function() {
    toggleSidebar();
});

// Function to close sidebar when clicking outside
window.addEventListener("mouseup", function(event) {
    var sidebar = document.getElementById("sidebar");
    if (event.target != sidebar && !sidebar.contains(event.target)) {
        sidebar.classList.remove("active");
    }
});
