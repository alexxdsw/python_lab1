name = input("Introdu numele tău: ")
print("Salut, " + name + "! Bine ai venit la laboratorul nr.1")

numar_intreg = 42
numar_real = 3.14
text_scurt = "Python"
text_lung = """Acesta este un text lung
care ocupa mai multe randuri
si serveste ca exemplu."""

tip1 = type(numar_intreg)
tip2 = type(numar_real)
print("Tipul variabilei numar_intreg:", tip1)
print("Tipul variabilei numar_real:", tip2)

lungime_text = len(text_scurt)
print("Lungimea textului scurt este:", lungime_text)

text_mare = text_scurt.upper()
print("Textul in litere mari:", text_mare)

subsir = text_scurt[1:4] 
print("Subsir extras:", subsir)

mesaj_formatat = "Numarul intreg este {} si numarul real este {:.2f}".format(numar_intreg, numar_real)
print(mesaj_formatat)

print(f"Textul lung este:\n{text_lung}")


print("\n" * 3)


#ex a)
txt = "More results from text..."
substr = txt[4:12]
print(substr)
print(substr.strip())
#txt[4:12] extrage subsirul " results" (include spatiul de la inceput).
#strip() elimina spatiile de la margini

print("\n" * 3)

#ex b)
txt = "More results from text..."
print(txt.split())
#split() imparte sirul in cuvinte, separand dupa spatii
print("\n" * 3)


#ex c)
age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))
#format(age) inlocuieste {} cu valoarea 36