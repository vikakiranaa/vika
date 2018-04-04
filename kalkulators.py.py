TAMBAH, KURANG, BAGI, KALI = range(4)

def hitung(a, b, operator=TAMBAH, format_output=float):
    hasil = 0
    if operator == TAMBAH:
        hasil = a + b
    elif operator == KURANG:
        hasil = a - b
    elif operator == BAGI:
        hasil = a / b
    elif operator == KALI:
        hasil = a * b
    else:
        ValueError("Operator yang diijinkan TAMBAH, KURANG, BAGI, KALI")

    if format_output == float:
        hasil=float(hasil)
    elif format_output == int:
        hasil=round(hasil)
    else:
        ValueError("format output harus int atau float")
    return hasil
    
