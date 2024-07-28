Bir cihaz, ağa ilk bağlandığında ve bir IP adresine ihtiyaç duyduğunda, DHCP protokolü kullanılarak IP adresi ve diğer ağ yapılandırma bilgilerini almak için belirli adımları izler. Bu adımlar genellikle dört aşamalı bir süreç olan DORA (Discover, Offer, Request, Acknowledge) süreci olarak bilinir.

DHCP DORA Süreci
#
Discover (Keşfetme)

* İstemci: Ağa bağlanmak isteyen cihaz (istemci), bir DHCP Discover yayını gönderir. Bu yayın, ağdaki tüm DHCP sunucularına yöneliktir ve istemcinin bir IP adresi ve yapılandırma bilgileri aradığını bildirir.
* Paket İçeriği: Yayın (broadcast) adresine gönderilen DHCP Discover paketi, istemcinin MAC adresini ve diğer kimlik bilgilerini içerir.
# Offer (Teklif)
* Sunucu: DHCP sunucuları, DHCP Discover yayınını alır ve istemciye bir DHCP Offer paketi gönderir. Bu paket, istemciye tahsis edilmek üzere bir IP adresi ve diğer yapılandırma bilgilerini içerir.
* Paket İçeriği: DHCP Offer paketi, sunucunun önerdiği IP adresini, alt ağ maskesini, geçerli IP adresi kira süresini, varsayılan ağ geçidini, DNS sunucularını ve diğer ağ yapılandırma bilgilerini içerir.
# Request (Talep)

* İstemci: İstemci, DHCP sunucusunun teklif ettiği IP adresini kabul etmeye karar verdiğinde, bu adresi talep eden bir DHCP Request paketi gönderir. Bu paket, istemcinin kabul ettiği IP adresini ve yapılandırma bilgilerini içerir.
* Paket İçeriği: DHCP Request paketi, istemcinin talep ettiği IP adresini ve hangi DHCP sunucusundan bu adresi talep ettiğini belirtir. Bu, istemcinin özellikle belirli bir sunucunun teklifini kabul ettiğini belirtir.
# NOT BURADA İstemci ARP Probe yapar ve IP adresi başkası tarafından alındıysa DHCP Sunucusuna NACK(Negative Acknowledgement) paketi atar ve DHCP bir üstteki maddede olan OFFER paketini tekrar atar ve hatayı düzeltir
# DHCP-ACK (Onaylama)
* Sunucu: DHCP sunucusu, istemcinin DHCP Request paketini alır ve bu talebi onaylayan bir DHCP Acknowledge (ACK) paketi gönderir. Bu paket, istemcinin belirtilen IP adresini ve yapılandırma bilgilerini kullanabileceğini onaylar.
* Paket İçeriği: DHCP ACK paketi, istemcinin kullanacağı IP adresini, alt ağ maskesini, varsayılan ağ geçidini, DNS sunucularını ve kira süresini içerir.
# Özet
* İstemci: İlk bağlandığında, bir IP adresi almak için DHCP Discover yayını gönderir.*
* Sunucu: DHCP sunucuları, DHCP Discover yayınını alır ve bir DHCP Offer paketi ile yanıt verir.
* İstemci: Sunucunun teklif ettiği IP adresini kabul ederse, DHCP Request paketi gönderir.*
* Sunucu: DHCP Request paketini alır ve DHCP ACK paketi ile istemcinin IP adresini ve yapılandırma bilgilerini onaylar.*
* Bu süreç, istemcinin rastgele bir IP adresi seçmeden, DHCP sunucusundan yapılandırma bilgilerini güvenli ve doğru bir şekilde almasını sağlar.
