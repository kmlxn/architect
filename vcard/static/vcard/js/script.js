$(document).ready(function() {
    $('#projects_nav').click(get_and_view_projects_tags);
    $('#contacts_nav').click(get_and_view_contacts_info);
    $('#about_me_nav').click(get_and_view_about_me_text);
});


var get_and_view_projects_tags = function(e) {
    $.ajax("/get_tags/", {
        success: function(tags) {
            // console.log(tags[0]);
            var html = '<ul class="projects_tags" id="projects_tags">';

            for (var i = 0; i < tags.length; i++) {
                html +=
                    '<li>\
                        <a href="#" id="' + tags[i].fields.alias + '">\
                            ' + tags[i].fields.caption + '\
                        </a>\
                    </li>';
            }

            html += '</ul>';

            $('#content').html(html);
            $('#projects_tags a').click(get_and_view_projects);
        },
        error: function(data) {

        },
    });
    e.preventDefault();
};


var get_and_view_contacts_info = function(e) {
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
};


var get_and_view_about_me_text = function(e) {
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
};


var get_and_view_projects = function(e) {
    var link = "/get_projects/" + $(this).attr('id') + "/";
    $.ajax(link, {
        success: function(projects) {
            console.log(projects[0]);
            var html = '<div class="projects">';

            for (var i = 0; i < projects.length; i++) {
                html +=
                    '<div class="project">\
                        <div class="photo">\
                            <img src="/media/' + projects[i].fields.picture + '" alt="" />\
                        </div>\
                        <span class="caption">' + projects[i].fields.caption + '</span>\
                    </div>';
            }

            html += '</div>';

            $('#content').html(html);
        },
        error: function(data) {

        },
    });
    e.preventDefault();
};
