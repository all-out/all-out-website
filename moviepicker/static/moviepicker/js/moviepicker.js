loadPoll()

/**
 * Calls 'get-results/'. If a non-zero length result is returned by django,
 * replaces the current contents of #results with the result.  If the result
 * IS length zero, this is announced with a message.
 */
function loadPoll() {
    $.ajax({
        url: '/movies/get-results/',
        success: function(result) {
            if (result.length > 0) {
                $('#results').html(result)
            } else {
                $('#results').html('<p class="text-center">No movies have been suggested yet.</p>')
            }
        },
    })
}


/**
 * Toggle a vote on a poll choice.
 */
$('#results').on('click', '.vote-toggle', function() {
    var movie_id = $(this).attr('data-movie-id')
    var voted = $(this).hasClass('success')

    $.ajax({
        url: '/movies/vote-toggle/',
        method: 'POST',
        data: {
            movie_id: movie_id
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
        },
        success: function() {
            if (voted) {
                $(this).removeClass('success')
            } else {
                $(this).addClass('success')
            }
            loadPoll()
        },
    })
})


/**
 * Get the cookie containing the CSRF token (needed for POSTing with ajax)
 */
function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}