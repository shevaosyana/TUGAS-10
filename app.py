from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Fungsi untuk menghitung probabilitas distribusi binomial
def binomial_distribution(n, p, k):
    coefficient = math.comb(n, k)  # Menghitung C(n, k)
    probability = coefficient * (p ** k) * ((1 - p) ** (n - k))  # Menghitung probabilitas
    return probability

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    n, p, k = None, None, None  # Default None untuk GET request

    if request.method == 'POST':
        try:
            # Ambil input dari form
            n = int(request.form['n'])
            p = float(request.form['p'])
            k = int(request.form['k'])
            
            # Validasi input
            if n <= 0:
                result = "Jumlah pelanggan (n) harus lebih besar dari 0."
            elif p < 0 or p > 1:
                result = "Probabilitas (p) harus berada antara 0 dan 1."
            elif k < 0 or k > n:
                result = "Jumlah pelanggan yang membeli produk (k) harus antara 0 dan n."
            else:
                # Hitung distribusi binomial
                result = binomial_distribution(n, p, k)
        
        except KeyError as e:
            result = f"KeyError: {str(e)} - Pastikan semua form input diisi dengan benar."
        except ValueError:
            result = "Harap masukkan angka yang valid untuk n, p, dan k!"
    
    return render_template('index.html', result=result, n=n, p=p, k=k)

if __name__ == '__main__':
    app.run(debug=True)
