# ebookpoint-promocja
Skrypt tworzy **plik CSV** (wartości przedzielone są średnikami) z kolumnami o nazwach:

1. Autor
2. Tytuł
3. Cena
4. Cena detaliczna
5. Zniżka 
6. Oszczędzasz

zawierający **tylko ebooki** (epub,pdf,mobi) będące w **promocji** na www.ebookpoint.pl

Po wygenerowaniu pliku ebookpoint_ebooks.csv najlepiej zaimportować go do Excela poprzez:

Dane -> Z tekstu -> ebookpoint_ebooks.csv -> Importuj -> Pochodzenie pliku: Windows (ANSI) -> Dalej -> Średnik -> Dalej -> Zakończ

i wstawienie tabeli z filtrami poprzez:

Ctrl + Shift + lewa strzałka + prawa strzałka -> Wstawianie -> Tabela

![alt tag](https://raw.githubusercontent.com/maciejszewczyk/ebookpoint-promocja/master/ebookpoint_promocja.png)
