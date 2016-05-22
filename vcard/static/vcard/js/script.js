$(document).ready(function() {
    $('#projects_nav').click(get_and_view_projects_tags);
    $('#contacts_nav').click(get_and_view_contacts_info);
    $('#about_me_nav').click(get_and_view_about_me_text);
});


var get_and_view_projects_tags = function(e) {
    $.ajax("/get_tags/", {
        success: function(tags) {
            var template = $('#content [type="text/mustache_template"]').html();
            var rendered = Mustache.render(template, {tags: tags});
            $('#content').html(rendered);
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

            $('#projects').html(html);
        },
        error: function(data) {

        },
    });
    e.preventDefault();
};
