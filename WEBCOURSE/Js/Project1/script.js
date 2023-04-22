const form = document.getElementById("login-form");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (email === "user@gmail.com" && password === "user@123") {
    window.location.href = "Home.html";
  } else {
    alert("invalid email and password");
  }
});
