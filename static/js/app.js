$(document).ready(function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $(document).on('click', 'a.edit-button', function(e) {
        var updateUrl = $(this).data("updateurl");
        $.get(updateUrl, function(data) {
            $('#updateTaskModalBody').html(data);
            console.log($('#updateTaskModalBody').find("form"));
            $('#updateTaskModalBody').find("form").attr('action', updateUrl);
        });
    });

    $(document).on('click', 'a.delete-button', function(e) {
        var deleteUrl = $(this).data("deleteurl");
        $.get(deleteUrl, function(data) {
            $('#deleteTaskConfirmModalBody').html(data);
            $('#deleteTaskConfirmModalBody').find("form").attr('action', deleteUrl);
        });
    });

    $(document).on('click', 'a.finish-button', function(e) {
        var deleteUrl = $(this).data("finishurl");
        $.post(deleteUrl, function(data) {
            location.reload();
        });
    });
})