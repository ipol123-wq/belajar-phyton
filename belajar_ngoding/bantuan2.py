import os
import json
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key='rahasia123'
pin_benar = '654321'
def baca_saldo():
    if os.path.exists('saldo.txt'):
        with open('saldo.txt', 'r') as file:
            return int(file.read())
    return 0
def simpan_saldo(saldo_user):
    with open ('saldo.txt', 'w') as file:
        file.write(str(saldo_user))
def baca_riwayat():
    if os.path.exists('riwayat.json'):
        with open('riwayat.json', 'r') as file:
            riwayat = json.load(file)
            return riwayat
    return []
def simpan_riwayat(riwayat):
    with open ('riwayat.json', 'w') as file:
        json.dump (riwayat, file)
def wajib_login():
    return not session.get('login')

@app.route('/', methods=['GET', 'POST'])
def home():
    pesan = ''
    if request.method=='POST':
        pin = request.form.get('pin')
        if pin == pin_benar:
            session['login']=True
            return redirect(url_for('menu'))
        else:
            pesan = 'pin salah'
    return render_template('login.html', pesan = pesan)
@app.route('/menu')
def menu():
    if wajib_login():
        return redirect(url_for('login'))
    return render_template('menu.html')
@app.route('/saldo')
def saldo():
    if wajib_login():
        return redirect(url_for('menu'))
    return render_template('saldo.html', saldo=baca_saldo())
@app.route('/setor', methods=['GET', 'POST'])
def setor():
    if wajib_login():
        return redirect(url_for('login'))
    pesan = ''
    if request.method=='POST':
        try:
            jumlah = int(request.form.get('jumlah'))
        except:
            pesan = 'masukan anga woilah'
            return render_template('setor.html', pesan=pesan)
        saldo_user=baca_saldo()
        saldo_user += jumlah
        simpan_saldo(saldo_user)
        riwayat = baca_riwayat()
        riwayat.append({
            'jenis': 'pemasukan',
            'jumlah': jumlah
        })
        simpan_riwayat(riwayat)
        pesan = f'{jumlah} berhasil di setor'
        return render_template('setor.html', pesan=pesan)
    return render_template('setor.html', pesan=pesan)
@app.route('/tarik', methods=['GET', 'POST'])
def tarik():
    pesan=''
    if wajib_login():
        return redirect(url_for('login'))
    if request.method=='POST':
        try:
            jumlah = int(request.form.get('jumlah'))
        except:
            pesan = 'masukin angak woi'
            return render_template('tarik.html', pesan=pesan)
        saldo_user = baca_saldo()
        if jumlah <= saldo_user:
            saldo_user -= jumlah
            simpan_saldo(saldo_user)
            riwayat = baca_riwayat()
            riwayat.append({
                'jenis': 'pengeluaran',
                'jumlah': jumlah
            })
            simpan_riwayat(riwayat)
            pesan = f'{jumlah} berhasil di tarik'
        else:
            pesan = 'mohon maaf saldo anda tidak mencukupi'
        return render_template('tarik.html', pesan=pesan)
    return render_template('tarik.html', pesan=pesan)
@app.route('/riwayat')
def riwayat():
    if wajib_login():
        return redirect(url_for('login'))
    return render_template('riwayat.html', riwayat=baca_riwayat())
@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)


