#method generateIC takes a list of cosets as an inputs and returns the IC for these cosets
def generateIC(coset):
    cosetIC = 0
    for c in coset:
        c = c.lower()
        count = [0]*26
        n = 0
        for i in range(0, len(c)):
            val = ord(c[i]) - ord('a')
            if(val >= 0 and val <= 25):
                count[val] = count[val] + 1
                n += 1
        total = 0.0
        for i in range(0, len(count)):
            total += count[i] * (count[i]-1)
        total = total/(n*(n-1))
        cosetIC += total
    cosetIC = cosetIC/len(coset)
    return cosetIC

def crack(cipher):
    mkl = 10
    aic = []

    for i in range(1, mkl + 1):
        cosets = [''] * i
        for j, c in enumerate(cipher):
            cosets[j % i] += c

        aic.append((i, generateIC(cosets)))

    maxaic = max(aic, key=lambda x: x[1])
    keylen = maxaic[0]

    return keylen

s0 = "RSTCSJLSLRSLFELGWLFIISIKRMGL"
s1 = "OICPWZXZEVLGCLNFSYPGALPXWZJTEGALPCSIIWDHOIECCBFWPAHOPCGALPCCBROASNWTYHOIDBIHVPSCSIDEVLSYPGDLZDSLXSTBNWOTTMICPBAPJEVLCLCSUSEQCUHZQFBPPDOUHESSFLLGSUSCPGWINETVVESSZXLEIZUFZMVYNLBXYZESALPXRPWLRFLIHTHOXSPANPZCWMCZCJPPTQMALPXOISFEHOIZYZFXSTBNCZFQHRYZHKSTDWNRZCSALPXPLGLFGLXSPMJLLYULXSTBNWESSFTFDVALPSITEYCOJIQZFDECOOUHHSWSIDZALQLJGLIESSTEDEVLGCLNFSYPGDIDPSNIYTIZFPNOBWPEVLTPZDSIHSCHVPNFHDJPBVYRSHVXSTBRXSPMJEYNVHRRPHOIHZFSHLCSALPZBLWHSCKS"
s2 = "VVVXSQWPSNJMUMJOKKLGFQAVEXAHWRVTMFXVVRKAJTVMFLOPHYWJDSTXKAGFVVTPHKYEPPJOKPSWACJVSIGGVOLXLVMQPVCMGOGMFLAKENVRMIUAKTKVHIXCFJZRAHWFHLIUMHCIRFWGFOETIUNEQVJWEHOSJWVQFYWKYMPGQHWISOPKHYFYV"
key_length = crack(s0)
print(key_length)

key_length = crack(s1)
print(key_length)

key_length = crack(s2)
print(key_length)