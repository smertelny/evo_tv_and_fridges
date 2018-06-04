function getCSRFToken() {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i];
            if (cookie.substring(0, 10) == ('csrftoken' + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(10));
                break;
            }
        }
    }
    return cookieValue;
    }
    function increase(elem) {
    fetch(`/inc-click/${elem.dataset.id}`, {
        method: "POST",
        headers: {"X-CSRFToken": getCSRFToken()},
        credentials: 'include'
    }).then(data => data.json()).then(data => document.getElementById(elem.dataset.id).innerHTML=data.clicks).catch(() => console.error("Error!"));
}