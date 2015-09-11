$(document).ready(function() {
    $('#projects_nav').click(function (e) {
        $.ajax("/get_projects/", {
            success: function(projects_list) {
                var html = '<div class="projects">';

                for (var i = 0; i < projects_list.length; i++) {
                    html +=
                        '<div class="project">\
                            <div class="photo">\
                                <img src="/media/' + projects_list[i].fields.picture + '" alt="" />\
                            </div>\
                            <span class="caption">' + projects_list[i].fields.caption + '</span>\
                        </div>';
                }

                html += '</div>';

                $('#content').html(html);
            },
            error: function(data) {

            },
        });
        e.preventDefault();
    });

    $('#contacts_nav').click(function (e) {
        $.ajax("/get_contacts/", {
            success: function(contacts_list) {
                var html = '<div class="contacts"><ul>';

                for (var i = 0; i < contacts_list.length; i++) {
                    html += '<li>' + contacts_list[i].fields.text + '</li>';
                }

                html += '</div></ul>';

                $('#content').html(html);
            },
            error: function(data) {

            },
        });
        e.preventDefault();
    });

    $('#about_me_nav').click(function (e) {
        $.ajax('/get_about_me_text/', {
            success: function(about_me) {
                about_me = about_me[0];
                var html = '<div class="about_me">' + about_me.fields.text + '</div>';
                
                $('#content').html(html);
            },
            error: function(data) {

            },
        });
        e.preventDefault();
    });
});
