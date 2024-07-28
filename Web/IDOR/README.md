# IDOR(Insecure direct object references) zaafiyet nedir ?
* IDOR zaafiyeti hedef web sunucusunda yetkisiz erişim sağlamaya ve eylemler gerçekleştirmesine sebebiyet veren bir zaafiyettir
* Verilere erişme,değiştirme olanağı
* Aynı şekilde hesap devralma
* ve diğer her türlü veriye erişme
* örnek
* ID=10256 Kurban ID'si
* ID=40555 ise Saldırgan ID'si
* saldırgan hemen url kısmına http://ornekweburl.com/credentials?id=10256
* yazarak kurbanın verilerine erişim sağlayabilir ya da değiştirebilir
* bu idor zaafiyetidir
# Peki IDOR zaafiyetinden nasıl korunabiliriz
* İlgili web sitesini geliştirenler anahtarlar dosya adları gibi önemli verileri görüntülemekten kaçınmalıdır
* Parametrelerin kontrolünün sağlanması gereklidir
* Başvurulan parametrelerin hepsinin doğrulanması gereklidir
* Belirteçler, yalnızca kullanıcıyla eşleştirilecek ve herkese açık olmayacak şekilde oluşturulmalıdır.
