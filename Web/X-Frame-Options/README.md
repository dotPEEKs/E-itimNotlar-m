# Bu Yazımızda X-Frame-Options başlığından bahsedeceğiz
***
> Peki Nedir Bu X-Frame-Options başlığı
* X-Frame-Options başlığı siteninin/sitenizin html tag'lerinden biri olan iframe'i kontrol etmek içindir.
* 3 Tane X-Frame-Options ayarımız bulunmaktarı bunlar sırasıyla: DENY,SAME-ORIGIN,ALLOW-FROM URI'dir(Not)(**NOT ALLOW-URI** bazı tarayıcılarda desteklenmeyebilir
***
***
> **SAME-ORIGIN**: Bu sadece aynı domainden gelen sayfaları kabul eder diğer domainden gelen sayfaları kabul etmez
> **DENY**: Bu hiçbir şekilde iframe kabul etmez
> **ALLOW-FROM URI**:Bu sadece belirtilen domainlerdeki iframe'leri kabul edicektir
***
>***NOT***:Sadece sunucu cevap başlığına **DENY** eklemek yeterli olmayabilir bu yüzden CSP ayarlamalarıda gerekebilir  [Buraya](https://www.mshowto.org/content-security-policy-csp-nedir.html) bakabilirsiniz ayrıca bu sefer fotoğraf ile örneklendirmedim direkt kendiniz sunucuyu çalıştırıp bakabilirsiniz.
# Peki bu açığın önlemi alınmazsa nelere sebebiyet verir
> Clickjacking (Sitenizi başka bir siteye gömüp clickjacking yapabilirler)
