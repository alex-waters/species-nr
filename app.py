import os
from flask import Flask, render_template, send_from_directory, request

# instantiate app with static path to help PA distributed filesystem
app = Flask(
    __name__,
    static_url_path='/home/anw/mysite/species-nr/static/'
)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route('/', methods=['GET', 'POST'])
def region_choice():

    page = render_template('layout.html')
    if request.method == 'GET':
        page = render_template('layout.html')

    return page


if __name__ == '__main__':
    port = app.config.get("PORT", 5000)
    app.run(port=port)
