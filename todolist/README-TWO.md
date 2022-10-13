Davina Fardya Zulfa Izzati - 2106702005 - A<br/><br/>

**Perbedaan antara ***asynchronous programming*** dengan ***synchronous programming*****<br/>
***Asynchronous programming*** memungkinkan pengguna mengirim ***request*** lain saat ***request*** sebelumnya masih diproses, sedangkan pada ***synchronous programming*** pengguna harus menunggu ***request*** sebelumnya selesai diproses baru bisa mengirim ***request*** baru.<br/>

**Paradigma ***Event-Driven Programming*** dalam JavaScript dan AJAX**<br/>
***Event-driven programming*** merupakan sebuah paradigma di mana eksekusi program berfokus pada aksi atau event yang dilakukan oleh pengguna. Contohnya ketika pengguna mengklik suatu ***button***, akan terjadi sesuatu yang spesifik.<br/>


**Penerapan ***asynchronous programming*** pada AJAX**<br/>
Asynchronous programming pada AJAX dapat dilakukan melalui ***method*** jQuery $.ajax() yang mengirimkan ***request*** di ***background*** sehingga pengguna dapat melakukan hal lain tanpa perlu menunggu ***request*** tersebut selesai diproses.<br/>

**Implementasi ***checklist*****<br/>
* Membuat fungsi show_json pada views.py untuk mengembalikan seluruh data task dalam bentuk JSON
* Membuat path json/ yang mengarah ke fungsi show_json
* Membuat fungsi add_task pada views.py untuk menambahkan task
* Membuat path add/ yang mengarah ke fungsi add_task
* Melakukan pengembalikan data task dengan $.get pada todolist.html
* Membuat modal dengan form untuk menambahkan task dengan $.post pada todolist.html