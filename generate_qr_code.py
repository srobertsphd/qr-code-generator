import segno

qr = segno.make_qr("https://docs.google.com/forms/d/e/1FAIpQLSe9hoqMgicYI6GAi6aloQASHUqo82_21Gk6RjqM8_nCc0LjJg/viewform", error='L')
qr.save(
    "ASRC_Lesker_Workshop_QR_L.png",
    scale=10,
    border=5,
    # quiet_zone="#000000"#01579B",#0D47A1",#1976D2"
    # light="#ADD8E6",
    # dark="darkblue",
    # data_dark="green",
    # data_light="lightgreen",
    )

