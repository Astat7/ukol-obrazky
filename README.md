# Ukázka Python knihovny Pillow

Knihovna nabízí velké množství funkcí. V souboru pictures.py je ukázka několikia z nich.

# Kód

## Rozostření pomocí BoxBlur

- Toto je filter který pomocí dvou hodnot rozostří obrázek.
- Hodnoty se zadávají v array
- Také se dá zadat int místo array, tato hodnota bude použita pro obě hodnoty

## Změna velikosti

- Image.resize() má na vstupu array s dvěma hodnoty šířka a výška. Tyto hodnoty zadávají počet pixelů výsledného obrázku

## Oříznutí

- Metoda Image.crop() má na vstupu array se čtyrmy hodnoty. Tyto hodnoty určují oblast pro vyříznutí

## Kontrast a světlost

- ImageEnhance může upravit kontrast a jas obrázku
- Kontrast má na vstupu hodnotu od 0.0 do 1.0
- Čím menší hodnota, tím větší kontrast

## Monochrom

- ImageOps.grayscale() odstraní z obrázku barvy

# Zdroje

- [Dokumentace knihovny](https://pypi.org/project/pillow/)
- [Geeksforgeeks](https://www.geeksforgeeks.org/python-pillow-a-fork-of-pil/)
- [Obrázek](https://www.dudleyzoo.org.uk/wp-content/uploads/00120.jpg)
