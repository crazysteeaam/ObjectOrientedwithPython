def isPotentialGene(dna):
    #基因长度为3的倍数, 否则返回Fasle
    if len(line) % 3 != 0:
        return False

    # 基因以ATG开始, 否则返回Fasle
    if not dna.startswith('ATG'):
        return False

    #基因以TAG、TAA或TGA结束, 否则返回Fasle
    if dna[-3:] not in ('TAG', 'TAA', 'TGA'):
        return False

    #基因中间部分不包括密码子TAG、TAA或TGA，否则返回False
    for i in range(3,len(dna)-3,3):
        if dna[i:i+3] in ('TAG', 'TAA', 'TGA'):
            return False
    return True

if __name__ == "__main__":
    filename = "gene.txt"
    for lineno, line in enumerate(open(filename,"r")):
        if isPotentialGene(line.strip()):
            print("{0}:{1}".format(lineno+1, line.strip()))

