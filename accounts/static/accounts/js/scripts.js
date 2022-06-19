function ShowPass() {
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

function isValid() {
    var username = document.getElementById('id_username');
    var password = document.getElementById('id_password');
    var userIsPass = document.getElementById('user_pass')
    var lengthPass = document.getElementById('length');
    var numberCase = document.getElementById('all_number');
    var fieldCase = document.getElementById('uppercase');
    var firstNumber = document.getElementById('number');

    // Validate capital letters
    if (password.value.match(/[A-Z]\w/g)) {
        fieldCase.classList.remove('text-muted');
        fieldCase.classList.remove('text-danger');
        fieldCase.classList.add('text-success');
    } else {
        fieldCase.classList.remove('text-muted');
        fieldCase.classList.remove('text-success');
        fieldCase.classList.add('text-danger');
    }

    //Validate is all numbers
    if (!password.value.match(/[a-zA-Z._@&]/g)) {
        numberCase.classList.remove('text-muted');
        numberCase.classList.remove('text-success');
        numberCase.classList.add('text-danger');

    } else {
        numberCase.classList.remove('text-muted');
        numberCase.classList.remove('text-danger');
        numberCase.classList.add('text-success');

        button.removeEventListener('click', (event) => {
            event.preventDefault();
        });
    }
    
    // Validate length
    if (password.value.length < 6) {
        lengthPass.classList.remove('text-muted');
        lengthPass.classList.remove('text-success');
        lengthPass.classList.add('text-danger');
    } else {
        lengthPass.classList.remove('text-muted');
        lengthPass.classList.remove('text-danger');
        lengthPass.classList.add('text-success');
    }

    // Validate username is password
    if (username.value == password.value) {
        userIsPass.classList.remove('text-muted');
        userIsPass.classList.remove('text-success');
        userIsPass.classList.add('text-danger');
    } else {
        userIsPass.classList.remove('text-muted');
        userIsPass.classList.remove('text-danger');
        userIsPass.classList.add('text-success');
    }

    // Valide first number
    if (password.value.match(/[0-9]/g)) {
        firstNumber.classList.remove('text-muted');
        firstNumber.classList.remove('text-danger');
        firstNumber.classList.add('text-success');
    } else {
        firstNumber.classList.remove('text-muted');
        firstNumber.classList.remove('text-success');
        firstNumber.classList.add('text-danger');
    }

}


// const button = document.getElementById('btn_submit')

// button.addEventListener('click', (event) => {
//     const fname = document.getElementById('first_name')
//     const lname = document.getElementById('last_name')
//     const user = document.getElementById('username')
//     const email = document.getElementById('email')
//     const password = document.getElementById('password')
//     const password_confirm = document.getElementById('password_confirm')

//     if (fname.value == '' || fname.value.length > 20) {
//         fname.classList.add('is-invalid');
//         
//     }
//     if (lname.value == '') {
//         lname.classList.add('is-invalid')
//     }
//     if (user.value == '') {
//         user.classList.add('is-invalid')
//     }
//     if (email.value == '') {
//        email.classList.add('is-invalid')
//     }else {
//         password_confirm.classList.add('is-valid')
//     }
//     if (password.value == '') {
//         password.classList.add('is-invalid')
//     }else {
//         password_confirm.classList.add('is-valid')
//     }
//     if (password_confirm.value == '') {
//         password_confirm.classList.add('is-invalid')
//     } 
    
// })