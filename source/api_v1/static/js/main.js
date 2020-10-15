
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method='GET', data=undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {  // нормальный ответ
        return await response.json();
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function onClick(event) {
    event.preventDefault();
    let likeBtn = event.target;
    let url = likeBtn.href;

    try {
        a = document.getElementById("a").value
        b = document.getElementById("b").value
        let response = await makeRequest(url,"POST", {"A":a,"B":b});
        console.log(response);
        const counter = document.getElementById("container")
         counter.style.color = "green"
        counter.innerText = response['answer'];
    }
    catch (error) {
        console.log(error);
        error = await error.response
        response = await error.json()

        console.log(response)
        const counter = document.getElementById("container")
        counter.style.color = "red"
        counter.innerText = response['error'];
    }
}

window.addEventListener('load', function() {
    const add= document.getElementById('add');
    const subtract = document.getElementById("subtract");
    const multiply = document.getElementById("multiply");
    const divide = document.getElementById("divide");

    add.onclick = onClick
    subtract.onclick = onClick
    multiply.onclick = onClick
    divide.onclick = onClick
});
