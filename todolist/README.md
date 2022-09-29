Davina Fardya Zulfa Izzati - 2106702005 - A<br/>
https://katalog-vina.herokuapp.com/todolist/
<br/>
<br/>
**Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**<br/>
CSRF (Cross Site Request Forgery) adalah serangan yang membuat user melakukan tindakan berbahaya pada situs web yang sedang diautentikasi. CSRF token merupakan token yang dihasilkan server untuk mencegah serangan tersebut. CSRF token digunakan sebagai perbandingan antara dua token yang ditemukan dari user dan request. Jika token tidak sama, request ditolak dan dicatat sebagai potensi CSRF. Sebaliknya, jika token sesuai, request akan diproses.<br/>
Tanpa potongan kode tersebut pada elemen form, orang lain bisa dengan mudah mengakses situs web yang sedang kita akses dan melakukan perubahan yang tidak diinginkan.
<br/>
<br/>
**Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.**<br/>
Bisa. Caranya adalah dengan menginisiasi pembuatan tabel pada template dengan tags </table> dan method POST, kemudian meletakkan data dari user dalam tabel tersebut.
<br/>
<br/>
**Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**<br/>
Data yang di-input user akan diterima dengan tag input. Kemudian, klien mengirim request POST ke server. Request yang diterima server akan diproses sesuai fungsi pada views.py. Data tersebut akan dimasukkan ke dalam form berdasarkan model yang ada serta disimpan ke database.
<br/>
<br/>
<b>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.</b><br/>
- Membuat dan mendaftarkan aplikasi todolist pada proyek yang sudah dibuat
- Membuat class Task pada models.py todolist dengan atribut user, date, title, dan description
- Membuat fungsi yang bersesuai dengan atribut pada views.py todolist sekaligus menambahkan kode untuk restriksi akses agar isi todolist/cretae-task hanya dapat diakses oleh user yang login
- Menambahkan routing pada urls.py todolist
- Membuat template untuk halaman situs yaitu todolist, login, register, dan create-task
- Memasukkan kode ke github
- Melakukan deployment ke Heroku
- Membuat dua akun pengguna dan tiga dummy data