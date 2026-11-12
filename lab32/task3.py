import qrcode

# Дані студента — латиницею
text = "Vlad Radchuk, IT-32, vladradcuk5@gmail.com"

image = qrcode.make(text)
image.save("contact.png")

print("saved: contact.png")