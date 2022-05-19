text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(':')
val=text[pos+5:]
dec=float(val)
print(dec)