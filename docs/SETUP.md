<h1 align="center">Setup Your Bot Config</h1>
Sangat disarankan untuk mengatur botmu terlebih dahulu menggunakan 
environment variables, ini adalah cara untuk mengatur bot dengan .env file
<br>
<br>

<details>
<summary><code>API_ID</code> dan <code>API_HASH</code></summary>
Kamu bisa mendapatkan API_ID dan API_HASH 
<a href="https://my.telegram.org/apps">di sini</a>
<br>
<li>Login dahulu menggunakan nomor Telegram kamu</li>
<li>Jika sudah tekan next atau selanjutnya</li>
<li>Kamu akan menerima kode verifikasi dari Telegram service</li>
<li>Setelah sudah login kamu buat app atau aplikasi</li>
<li>Isi form seperti nama, url, dan platform terserah kalian
<li>Jika berhasil dibuat maka akan ada field API ID dan API Hash</li>
<li>Copy API ID dan API Hash tersebut ke dalam <a href="../example.env">example.env</a>
</details>

<details>
<summary><code>Bot Token</code></summary>
Kamu bisa mendapatkan Bot Token 
<a href="https://t.me/botfather">di BotFather</a>
<br>
<li>Buat bot terlebih dahulu jika belum punya dengan mengetik /newbot</li>
<li>Isi nama dan username untuk bot kamu</li>
<li>Jika sudah maka ada tulisan seperti ini
<br>
<pre>Use this token to access the HTTP API:
13131:adjwad-cWAdaiw
Keep your token secure and store it safely, it can be used by anyone to control your bot</pre>
</li>
<li>Copy token yang sudah diberikan ke dalam <a href="../example.env">example.env</a></li>
</details>

<details>
<summary><code>Terakhir</code></summary>
<li>Rename <a href="../example.env">example.env</a> menjadi <a href="../example.env">.env</a></li>
<li>Jalankan bot dengan <code>python3 main.py</code></li>
</details>