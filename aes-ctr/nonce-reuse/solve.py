# Paste C1, C2, and KNOWN_P1 here
C1 = "9c28f6b827b205e610e0eb17aff9afafe9b78a17644ea97dcefb19589ecc8a9d982fb420f9d2c3cfe7957775df3a9bfae8fa2d35ea6fcee75d6d599adf63fb1d3da4e23a687377b44e0ed625f8ba1380158fb00bf6fb61319efe91c331a39d1a1d204aac0caf38659b5028e64297888eed0dc6fc099e4b38e9a4cf897e7e03151633bb"
C2 = "8b39f6be72955aa71ca0a743b4e5fcaaf9bb8b436f53a86d80e81006d1f892dc9666b431e4c5cdefdbb6683b8d3194a6c0a8782feb7ce8b95b401adcce21e10c38bab202357549a34e4fc022fcbb5594"
KNOWN_P1 = "Dear Team, the quarterly report is attached below for your review. Please read it carefully and let us know if you have questions."

c1, c2 = bytes.fromhex(C1), bytes.fromhex(C2)
keystream = bytes(a ^ b for a, b in zip(c1, KNOWN_P1.encode()))
flag = bytes(a ^ b for a, b in zip(c2, keystream))
print(flag.decode(errors="replace"))

# picoCTF{n0nc3_r3us3_1s_c4t4str0ph1c_deadbeef}
