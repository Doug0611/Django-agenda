function ShowPass1() {
    var psw = document.getElementById('id_password')
    var btn = document.querySelector('.btn')

    if (psw.type === "password") {
      psw.type = "text";
    } else {
        psw.type = "password";
    }

    psw.type = psw.type

    if (btn.classList.contains("fa-eye")) {
        btn.classList.remove("fa-eye");
        btn.classList.add("fa-eye-slash");
    } else {
        btn.classList.remove("fa-eye-slash");
        btn.classList.add("fa-eye");
    }
}

function ShowPass2() {
    var psw = document.getElementById('id_password_confirm')
    var btn = document.querySelector('.btn2')

    if (psw.type === "password") {
      psw.type = "text";
    } else {
        psw.type = "password";
    }

    psw.type = psw.type

    if (btn.classList.contains("fa-eye")) {
        btn.classList.remove("fa-eye");
        btn.classList.add("fa-eye-slash");
    } else {
        btn.classList.remove("fa-eye-slash");
        btn.classList.add("fa-eye");
    }
}
