Davina Fardya Zulfa Izzati - 2106702005 - A<br/><br/>

**Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**<br/>
* Inline CSS hanya menata elemen HTML tertentu, caranya dengan menambahkan atribut style ke setiap tag HTML yang diinginkan tanpa menggunakan selector.<br/>
Kelebihan: lebih mudah jika ingin menata satu halaman saja, prioritasnya paling tinggi sehingga dapat digunakan untuk langsung mengubah sesuatu.<br/>
Kekurangan: menggunakan style akan memakan waktu karena setiap style ditulis untuk satu tag saja dan lebih sulit dibaca karena panjang.<br/>
* Internal CSS merupakan style yang digunakan dengan mendefinisikan kode CSS dalam tag <style> di bagian `<head>` dokumen HTML.<br/>
Kelebihan: lebih cepat dan efektif untuk menata satu halaman, tidak memerlukan dokumen CSS yang berbeda.<br/>
Kekurangan: kurang efektif untuk menata banyak halaman, meningkatkan waktu memuat halaman tersebut.<br/>
* External CSS memuat kode CSS untuk menata berkas-dokumen HTML secara terpisah dengan format dokumen .css.<br/>
Kelebihan: efektif untuk menata situs yang besar, bisa digunakan ke banyak dokumen HTML, struktur pada dokumen HTML lebih rapi karena hanya perlu import style-nya.<br/>
Kekurangan: membutuhkan waktu akses styling dari dokumen .css, tidak efektif jika situs hanya memiliki satu halaman saja.<br/>

**Jelaskan tag HTML5 yang kamu ketahui.**<br/>
- `<button>` membuat tombol yang dapat diklik
- `<div>` menentukan bagian styling dalam dokumen
- `<head>` mendefinisikan bagian atas dokumen yang berisi informasi awal seperti judul
- `<h1> ... <h6>` mendefinisikan heading HTML
- `<html>` mendefinisikan root dokumen HTML
- `<table>` mendefinisikan tabel
- `<title>` mendefinisikan judul dokumen

**Jelaskan tipe-tipe CSS selector yang kamu ketahui**<br/>
* ID Selectors menggunakan ID sebagai selector pada tag, diawali dengan #
* Classes selectors menggunakan class sebagai selector, selector diawali dengan .
* Element selectors menggunakan tag HTML sebagai selector untuk mengubah properti dalam tag tersebut<br/>
Prioritas selector tertinggi dimulai dari yang paling atas.<br/>

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**<br/>
* Menambahkan kode untuk menggunakan Bootstrap ke base.html
* Mendefinisikan class yang ingin dipakai untuk styling
* Mendesain card untuk task pada todolist.html
* Mendesain button dengan Bootstrap
* Mendesain halaman login melalui dokumen login.html
* Mendesain halaman add task melalui dokumen create-task.