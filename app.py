import time, os, pickle
from flask import Flask, render_template, send_from_directory, request, jsonify

# instantiate app with static path to help PA distributed filesystem
app = Flask(
    __name__,
#    static_url_path='/home/anw/mysite/species-nr/static/'
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


@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('submit.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        receive_time = round(time.time())
        received = request.form.to_dict(flat=False)
        pickle.dump(received, file=open('{}.p'.format(receive_time), 'wb'))
    # with open('{}_form.json'.format(str(round(receive_time)), 'wb')) as f:
    #     json.dump(request.form, f)

    return render_template(
        'thank_submit.html',
    )


if __name__ == '__main__':
    port = app.config.get("PORT", 5000)
    app.run(port=port)
