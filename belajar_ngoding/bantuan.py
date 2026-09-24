import os
import json
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key='rahasia123'
pin_benar='654321'
@app.route('/', methods=['GET', 'POST'])
def home():
    pesan=''
    if request.method=='POST':
        pin = request.form.get('pin')
        if pin==pin_benar:
            session['login']=True
            return redirect(url_for('menu'))
        else:
            pesan = 'pin salah'
    return render_template('login.html', pesan=pesan)
@app.route('/menu')
def menu():
    if not session.get('login'):
        return redirect(url_for('menu'))
    return render_template('menu.html')
@app.route('/saldo')
def saldo():
    if not session.get('login'):
        return redirect(url_for('home'))
    if os.path.exists('saldo.txt'):
        with open ('saldo.txt', 'r') as file:
            saldo_user=int(file.read())
    else:
        saldo_user=0
    return render_template('saldo.html', saldo=saldo_user)

@app.route('/setor', methods=['GET', 'POST'])
def setor():
    if not session.get('login'):
        return redirect(url_for('home'))
    pesan = ''
    if request.method=='POST':
        try:
            jumlah = int(request.form.get('jumlah'))
        except:
            pesan=f'masukkan nominal woi'
            return render_template('setor.html', pesan=pesan)
        if os.path.exists('saldo.txt'):
            with open ('saldo.txt', 'r') as file:
                saldo_user=int(file.read())
        else:
            saldo_user=0
        saldo_user+=jumlah
        with open('saldo.txt', 'w') as file:
            file.write(str(saldo_user))
        pesan = f'{jumlah} berhasil di setor'
        if os.path.exists('riwayat.json'):
            with open('riwayat.json', 'r') as file:
                riwayat = json.load(file)
        else:
            riwayat = []
        riwayat.append({
            'jenis': 'pemasukan',
            'jumlah': jumlah
        })
        with open ('riwayat.json', 'w') as file:
            json.dump(riwayat, file)
            pesan=f'{jumlah} berhasil di setor'
        return render_template('setor.html', pesan=pesan)
    return render_template ('setor.html', pesan=pesan)

@app.route('/tarik', methods=['GET', 'POST'])
def tarik():
    if not session.get('login'):
        return redirect(url_for('home'))
    pesan =''
    if request.method=='POST':
        try:
            jumlah=int(request.form.get('jumlah'))
        except:
            pesan=f'masukin angka woilah cik'
            return render_template('tarik.html', pesan=pesan)
        if os.path.exists('saldo.txt'):
            with open ('saldo.txt', 'r') as file:
                saldo_user=int(file.read())
        else:
            saldo_user=0
        if os.path.exists('riwayat.json'):
            with open('riwayat.json', 'r') as file:
                riwayat = json.load(file)
        else:
            riwayat = []
        if jumlah <= saldo_user:
            saldo_user -= jumlah
            with open('saldo.txt', 'w') as file:
                file.write(str(saldo_user))
            pesan = f'{jumlah} berhasil di tarik'
            riwayat.append({
                'jenis': 'pengeluaran',
                'jumlah': jumlah
            })
            with open ('riwayat.json', 'w') as file:
                json.dump(riwayat, file)
        else:
            pesan = 'saldo anda tidak mencukupi'
        return render_template('tarik.html', pesan=pesan)
    return render_template('tarik.html', pesan=pesan)
@app.route('/riwayat')
def riwayat():
    if not session.get('login'):
        return redirect(url_for('home'))
    if os.path.exists('riwayat.json'):
        with open ('riwayat.json', 'r') as file:
            data = json.load(file)
    else:
        data = []
    return render_template('riwayat.html', riwayat=data)
@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('home'))
if __name__=='__main__':
    app.run(debug=True)

