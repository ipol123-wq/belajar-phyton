from flask import Flask, render_template, request
app = Flask(__name__)

PIN_BENAR= '123456'
@app.route('/', methods=['GET', 'POST'])
def home():
    pesan =''

    if request.method == 'POST':
        pin = request.form.get('pin')
        if pin == PIN_BENAR:
            pesan = 'PIN benar, selamat datang'
        else:
            pesan = 'PIN salah'
    return render_template('login.html', pesan=pesan)

if __name__=='__main__':
    app.run(debug=True)