
function toggleMenu() {
  const menu = document.getElementById("dropdownMenu");
  menu.style.display = (menu.style.display === "block") ? "none" : "block";
}
document.addEventListener('click', function(event) {
  const menu = document.getElementById("dropdownMenu");
  const profilePic = document.querySelector('.profile-pic');
  if (!profilePic.contains(event.target) && !menu.contains(event.target)) {
    menu.style.display = 'none';
  }
});
