
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});
let container = document.getElementById("container");

toggle = () => {
    container.classList.toggle("sign-in");
    container.classList.toggle("sign-up");
};

setTimeout(() => {
    container.classList.add("sign-in");
}, 200);
// passwoerd
const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password");
togglePassword.addEventListener("click", function (e) {
    // toggle the type attribute
    const type =
        password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);
    // toggle the eye / eye slash icon
    this.classList.toggle("bi-eye");
});
const togglePasswords = document.querySelector("#togglePasswords");
const passwords = document.querySelector("#passwords");
togglePasswords.addEventListener("click", function (e) {
    // toggle the type attribute
    const type =
        passwords.getAttribute("type") === "password" ? "text" : "password";
    passwords.setAttribute("type", type);
    // toggle the eye / eye slash icon
    this.classList.toggle("bi-eye");
});
// confirm
const toggleCPassword = document.querySelector("#toggleCPassword");
const cpassword = document.querySelector("#cpassword");
toggleCPassword.addEventListener("click", function (e) {
    // toggle the type attribute
    const type =
       cpassword.getAttribute("type") === "password" ? "text" : "password";
    cpassword.setAttribute("type", type);
    // toggle the eye / eye slash icon
    this.classList.toggle("bi-eye");
});
// LOGIN
const toggleLPassword = document.querySelector("#toggleLPassword");
const Lpassword = document.querySelector("#Lpassword");
toggleLPassword.addEventListener("click", function (e) {
    // toggle the type attribute
    const type =
        Lpassword.getAttribute("type") === "password" ? "text" : "password";
    Lpassword.setAttribute("type", type);
    // toggle the eye / eye slash icon
    this.classList.toggle("bi-eye");
});
