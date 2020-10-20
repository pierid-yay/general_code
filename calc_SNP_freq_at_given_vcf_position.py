fh = open('/mnt/griffin/handor/python_course/python_course/genotypes_small.vcf','r', encoding = 'utf-8')

wt = 0
het = 0
hom = 0

for line in fh:
    if not line.startswith('#'):
        cols = line.strip().split('\t')
        chrom = cols[0]
        pos = cols[1]
        if chrom == '2' and pos == '136608646':
            for geno in cols[9:]:
                alleles = geno.split(':')[0]
                if alleles == '0/0':
                    wt += 1
                elif alleles == '0/1':
                    het += 1
                elif alleles == '1/1':
                    hom += 1

freq = (2*hom + het)/((wt+hom+het)*2)

print('The frequency of the rs4988235 SNP, which is associated with lactose tolerance, is:' +str(freq))

fh.close()
