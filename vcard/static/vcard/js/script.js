class Handler {
    run() {
        this.cache_dom();
        this.bind_events();
    }

    cache_dom() {
        this.$projects_nav = $('a#projects_nav');
        this.$contacts_nav = $('a#contacts_nav');
        this.$about_me_nav = $('a#about_me_nav');
        this.$content = $('#content');
        this.template = this.$content.find('[type="text/mustache_template"]').html();
    }

    bind_events() {
        this.$projects_nav.click(this.get_and_view_projects_tags.bind(this));
        this.$contacts_nav.click(this.get_and_view_contacts_info.bind(this));
        this.$about_me_nav.click(this.get_and_view_about_me_text.bind(this));
        this.$content.on('click', '#projects_tags a', this.get_and_view_projects.bind(this));
        this.$content.magnificPopup({delegate: '.photo a', type: 'image'});
    }

    render() {
        const rendered = Mustache.render(this.template, this.data);
        this.$content.html(rendered);
    }

    get_and_view_projects_tags(event) {
        $.get("/get_tags/").done((tags) => {
            this.data = {
                tags,
                has_tags: true,
            };

            this.render();
        });

        event.preventDefault();
    }

    get_and_view_contacts_info(event) {
        $.get("/get_contacts/").done((contacts) => {
            this.data = {contacts};
            this.render();
        });

        event.preventDefault();
    }

    get_and_view_about_me_text(event) {
        $.get("/get_about_me_text/").done((about_me) => {
            this.data = {about_me};
            this.render();
        });

        event.preventDefault();
    }

    get_and_view_projects(event) {
        const project_id = event.currentTarget.id;
        const link = "/get_projects/" + project_id + "/";

        $.get(link).done((projects) => {
            const tags = this.data.tags;
            const has_tags = true;
            this.data = {
                has_tags,
                tags,
                projects,
            };

            this.render();
        });

        event.preventDefault();
    }
}

$(document).ready(function() {
    const handler = new Handler();
    handler.run();
});
