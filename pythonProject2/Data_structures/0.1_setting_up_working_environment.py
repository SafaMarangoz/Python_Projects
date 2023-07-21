print("Hello AI ERA")
## SAYILAR (NUMBERS) AND STRINGS (KARAKTER DİZİNLERİ)
## FLOAT 9.1 INTEGER 9
## TYPE FONKSIYONU
type(9.1)
type("MRB")
type(9)
## ATAMALAR VE DEGISKENLER (ASSIGNMENTS VE VARIABLES)

A=9
A
B="HELLO AI ERA"
B
C=10
A*C
###############################################################################################################################################
## VIRTUAL ENVIRONMENT (SANAL ORTAM)
#AYNI ANDA BİRDEN FAZLA FARKLI SÜRÜMÜN,FARKLI KÜTÜPHANELERİN BİRBİRİYLE ÇALIŞMASINI SAĞLAR.BİRİBİRİNİ ETKILEMEZLER (CONDA,VENV,VİRTUALV,PİPENV)
###############################################################################################################################################
## PACKAGE MANAGEMENT (PAKET YÖNETİMİ)
# pi(requirements.txt),pipenv(pipfile),conda(enviorenment.yaml)
#işlevleri 1.paket yönetimi 2.bağımlılık yönetimi
###############################################################################################################################################
## SANAL ORTAMLAR VE PAKET YÖNETİM ARAÇLARI İLİŞKİSİ UYGULAMA
## Sanallaştırma
# conda env list

##SANAL ORTAM OLUŞTURMA
# conda create -n msafa

##SANAL ORTAM AKTİF ETME
#conda activate msafa

## YÜKLÜ PAKETLERİN İNCELENMESİ
# conda list

##PAKET YÜKLEME
## conda install numpy

##AYNI ANDA PAKET YÜKLEME ( BOŞLUK BIRARAK DİĞER PAKETİ YAZARIZ)
## conda install scipy pandas

## paket silme
#CONDA REMOVE PACKAGE_NAME

## BELİRLİ BİR VERSİYONA GÖRE PAKET YÜKLEME
#conda install numpy=1.20.1

## PAKET YÜKSELTME
# conda upgrade numpy

## Tüm paketlerin yükseltilmesi
# conda upgrade -all

##pip:pypi (python package index) paket yönetim aracı

##Paket yükleme
# pip install pandas
### Paket yükleme(versiyona göre)
# pip install pandas ==1.2.1

##CONDA LISTDEKİ KÜTÜPHANLERİ PAKETLERİ BASKASINA AKTARMA
##conda env export>environment.yaml
## wındowsta dir ıos da ls yazıyoruz.
## sonunda oluştu

##başka yerden aldığımız çalışma ortamını kendi çalıştırma ortamına aktarma,oluşturma
# conda deactivate (ortamdan çıkış yapmak) (base env giriyoruz)
# conda env remove -n msafa (siliyoruz)
# conda list ()
## conda enc create -f environment.yaml
#coonda activate msafa
#conda list



