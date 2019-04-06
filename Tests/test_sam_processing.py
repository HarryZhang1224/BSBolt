import unittest
import os
from BSB.BSB_Align.ProcessSamReads import ProcessSamAlignment

test_directory = os.path.dirname(os.path.realpath(__file__))

# properly paired reads
test_read_1 = {'read_sequence': 'CTTTTCTTTTCTTTCATTTCTTTCTCTTAAATAAACTTTCCCCTATTTTATTCTCCCTACCCTTCATTACCTATTCCCTACAAACCTACTTAAACTAAAACACTAATAAAAAAAATCAATATCAT', 'W_C2T': {'QNAME': 'chr10-55354', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTTTTTTTTTTTTTTATTTTTTTTTTTTAAATAAATTTTTTTTTATTTTATTTTTTTTATTTTTTATTATTTATTTTTTATAAATTTATTTAAATTAAAATATTAATAAAAAAAATTAATATTAT', 'QUAL': 'CBAB@GG11BGGGGGGGDF>GGGGGGGGGGGDFDGGGGGGGGGGGGGG@GGGGGGGGGG:GGEGGGGCGFGFGGEGGGGGGGFGGGGGGGGGFGGGGGG>GGGGDGEGGDG1GGGGDDGGDCGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'C_C2T': {'QNAME': 'chr10-55354', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTTTTTTTTTTTTTTATTTTTTTTTTTTAAATAAATTTTTTTTTATTTTATTTTTTTTATTTTTTATTATTTATTTTTTATAAATTTATTTAAATTAAAATATTAATAAAAAAAATTAATATTAT', 'QUAL': 'CBAB@GG11BGGGGGGGDF>GGGGGGGGGGGDFDGGGGGGGGGGGGGG@GGGGGGGGGG:GGEGGGGCGFGFGGEGGGGGGGFGGGGGGGGGFGGGGGG>GGGGDGEGGDG1GGGGDDGGDCGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'W_G2A': {'QNAME': 'chr10-55354', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '221597', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '221789', 'TLEN': '317', 'SEQ': 'CTTTTCTTTTCTTTCATTTCTTTCTCTTAAATAAACTTTCCCCTATTTTATTCTCCCTACCCTTCATTACCTATTCCCTACAAACCTACTTAAACTAAAACACTAATAAAAAAAATCAATATCAT', 'QUAL': 'CBAB@GG11BGGGGGGGDF>GGGGGGGGGGGDFDGGGGGGGGGGGGGG@GGGGGGGGGG:GGEGGGGCGFGFGGEGGGGGGGFGGGGGGGGGFGGGGGG>GGGGDGEGGDG1GGGGDDGGDCGGG', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:0', 'YT:Z:CP']}, 'C_G2A': {'QNAME': 'chr10-55354', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'CTTTTCTTTTCTTTCATTTCTTTCTCTTAAATAAACTTTCCCCTATTTTATTCTCCCTACCCTTCATTACCTATTCCCTACAAACCTACTTAAACTAAAACACTAATAAAAAAAATCAATATCAT', 'QUAL': 'CBAB@GG11BGGGGGGGDF>GGGGGGGGGGGDFDGGGGGGGGGGGGGG@GGGGGGGGGG:GGEGGGGCGFGFGGEGGGGGGGFGGGGGGGGGFGGGGGG>GGGGDGEGGDG1GGGGDDGGDCGGG', 'SAM_TAGS': ['YT:Z:UP']}}
test_read_2 = {'read_sequence': 'GGAGGTTGTAGTGTGGGTTGTATAGATGAGTTAGATGTAGGTTTTGCTTTTTTTTTATTGTATAATAGGGTTTTAGGATTATATTTTTATTATTATGATGGTTTTAGATTAAGAATTAAATTATT', 'W_C2T': {'QNAME': 'chr10-55354', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'AAAAATTATAATATAAATTATATAAATAAATTAAATATAAATTTTACTTTTTTTTTATTATATAATAAAATTTTAAAATTATATTTTTATTATTATAATAATTTTAAATTAAAAATTAAATTATT', 'QUAL': 'CCBBCGG<GGG1FGGGGG1;GGG1GGGG1GGGGGG@EGEGGGGGGCEGGFGGE=GGGGGGGGGGGCGGG@GGGGDGGGGGGGGGGGFGGG0GGGGGGGGGGG.GGCG0GGGGGEGEGGGDDGGGE', 'SAM_TAGS': ['YT:Z:UP']}, 'C_C2T': {'QNAME': 'chr10-55354', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'AAAAATTATAATATAAATTATATAAATAAATTAAATATAAATTTTACTTTTTTTTTATTATATAATAAAATTTTAAAATTATATTTTTATTATTATAATAATTTTAAATTAAAAATTAAATTATT', 'QUAL': 'CCBBCGG<GGG1FGGGGG1;GGG1GGGG1GGGGGG@EGEGGGGGGCEGGFGGE=GGGGGGGGGGGCGGG@GGGGDGGGGGGGGGGGFGGG0GGGGGGGGGGG.GGCG0GGGGGEGEGGGDDGGGE', 'SAM_TAGS': ['YT:Z:UP']}, 'W_G2A': {'QNAME': 'chr10-55354', 'FLAG': '147', 'RNAME': 'chr10', 'POS': '221789', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '221597', 'TLEN': '-317', 'SEQ': 'AATAATTTAATTCTTAATCTAAAACCATCATAATAATAAAAATATAATCCTAAAACCCTATTATACAATAAAAAAAAAACAAAACCTACATCTAACTCATCTATACAACCCACACTACAACCTCC', 'QUAL': 'EGGGDDGGGEGEGGGGG0GCGG.GGGGGGGGGGG0GGGFGGGGGGGGGGGDGGGG@GGGCGGGGGGGGGGG=EGGFGGECGGGGGGEGE@GGGGGG1GGGG1GGG;1GGGGGF1GGG<GGCBBCC', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:0', 'YT:Z:CP']}, 'C_G2A': {'QNAME': 'chr10-55354', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'GGAGGTTGTAGTGTGGGTTGTATAGATGAGTTAGATGTAGGTTTTGTTTTTTTTTTATTGTATAATAGGGTTTTAGGATTATATTTTTATTATTATGATGGTTTTAGATTAAGAATTAAATTATT', 'QUAL': 'CCBBCGG<GGG1FGGGGG1;GGG1GGGG1GGGGGG@EGEGGGGGGCEGGFGGE=GGGGGGGGGGGCGGG@GGGGDGGGGGGGGGGGFGGG0GGGGGGGGGGG.GGCG0GGGGGEGEGGGDDGGGE', 'SAM_TAGS': ['YT:Z:UP']}}

# c_g2a read
test_read_3 = {'read_sequence': 'ATCTTTTAATTAAAAACCTAACATACTACTAATAAAAATATAAATAATTTAACTACTAAAAAAAATCTAACTTCTTATATAATCAATCAATTTAAAATATTCTCTCCCTAACACTTTCTCAAATC', 'W_C2T': {'QNAME': 'chr10-55902', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'ATTTTTTAATTAAAAATTTAATATATTATTAATAAAAATATAAATAATTTAATTATTAAAAAAAATTTAATTTTTTATATAATTAATTAATTTAAAATATTTTTTTTTTAATATTTTTTTAAATT', 'QUAL': 'CCCBCGGGGG=GGGGFGGGGG0GGCGGGGGGFGGGBGGGGGGGE1GGCGGGGGGFGGGGGGGG1GGG?FG>GGG00FGGGDGG/G0G<GECGGGEGGGEGGGGGGGG9GGGGBGEDGGGGGGGF0', 'SAM_TAGS': ['YT:Z:UP']}, 'C_C2T': {'QNAME': 'chr10-55902', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'ATTTTTTAATTAAAAATTTAATATATTATTAATAAAAATATAAATAATTTAATTATTAAAAAAAATTTAATTTTTTATATAATTAATTAATTTAAAATATTTTTTTTTTAATATTTTTTTAAATT', 'QUAL': 'CCCBCGGGGG=GGGGFGGGGG0GGCGGGGGGFGGGBGGGGGGGE1GGCGGGGGGFGGGGGGGG1GGG?FG>GGG00FGGGDGG/G0G<GECGGGEGGGEGGGGGGGG9GGGGBGEDGGGGGGGF0', 'SAM_TAGS': ['YT:Z:UP']}, 'W_G2A': {'QNAME': 'chr10-55902', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'ATCTTTTAATTAAAAACCTAACATACTACTAATAAAAATATAAATAATTTAACTACTAAAAAAAATCTAACTTCTTATATAATCAATCAATTTAAAATATTCTCTCCCTAACACTTTCTCAAATC', 'QUAL': 'CCCBCGGGGG=GGGGFGGGGG0GGCGGGGGGFGGGBGGGGGGGE1GGCGGGGGGFGGGGGGGG1GGG?FG>GGG00FGGGDGG/G0G<GECGGGEGGGEGGGGGGGG9GGGGBGEDGGGGGGGF0', 'SAM_TAGS': ['YT:Z:UP']}, 'C_G2A': {'QNAME': 'chr10-55902', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '275543', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '275829', 'TLEN': '411', 'SEQ': 'ATCTTTTAATTAAAAACCTAACATACTACTAATAAAAATATAAATAATTTAACTACTAAAAAAAATCTAACTTCTTATATAATCAATCAATTTAAAATATTCTCTCCCTAACACTTTCTCAAATC', 'QUAL': 'CCCBCGGGGG=GGGGFGGGGG0GGCGGGGGGFGGGBGGGGGGGE1GGCGGGGGGFGGGGGGGG1GGG?FG>GGG00FGGGDGG/G0G<GECGGGEGGGEGGGGGGGG9GGGGBGEDGGGGGGGF0', 'SAM_TAGS': ['AS:i:-3', 'XN:i:0', 'XM:i:1', 'XO:i:0', 'XG:i:0', 'NM:i:1', 'MD:Z:21T103', 'YS:i:0', 'YT:Z:CP']}}

test_read_4 = {'read_sequence': 'TGGGTTTATATTTGTTTATTTTTGGCTAAATGTAATTTTTTGTATTTTTAGTTTTGTGGATTTCTTTTTGGTGGATTTGTGTATAGTTTTTGTTTAGGATTTTGTTTTGGATTAGGTTTTGGTTTA', 'W_C2T': {'QNAME': 'chr10-55904', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TGGGTTTATATTTGTTTATTTTTGGTTAAATGTAATTTTTTGTATTTTTAGTTTTGTGGATTTTTTTTGGTGGATTTGTGTATAGTTTTTGTTTAGGATTTTGTTTTGGATTAGGTTTTGGTTTA', 'QUAL': 'CBACCGG=GGGGGGGGGGGGGGFGGGGG<GGGGGGGGGFG=GGGG1GCGGGGGGGGGGG1GEGGEGGGGG/GGGBGG0GGGGGGGGGGGGBGGGGGGGGGGGCGGGGGGGGGGGGGBGDGGGGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'C_C2T': {'QNAME': 'chr10-55904', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '313008', 'MAPQ': '255', 'CIGAR': '63M1I62M', 'RNEXT': '=', 'PNEXT': '313310', 'TLEN': '427', 'SEQ': 'TGGGTTTATATTTGTTTATTTTTGGTTAAATGTAATTTTTTGTATTTTTAGTTTTGTGGATTTTTTTTGGTGGATTTGTGTATAGTTTTTGTTTAGGATTTTGTTTTGGATTAGGTTTTGGTTTA', 'QUAL': 'CBACCGG=GGGGGGGGGGGGGGFGGGGG<GGGGGGGGGFG=GGGG1GCGGGGGGGGGGG1GEGGEGGGGG/GGGBGG0GGGGGGGGGGGGBGGGGGGGGGGGCGGGGGGGGGGGGGBGDGGGGGG', 'SAM_TAGS': ['AS:i:-3', 'XN:i:0', 'XM:i:1', 'XO:i:0', 'XG:i:0', 'NM:i:1', 'MD:Z:77T47', 'YS:i:-5', 'YT:Z:CP']}, 'W_G2A': {'QNAME': 'chr10-55904', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TAAATTTATATTTATTTATTTTTAACTAAATATAATTTTTTATATTTTTAATTTTATAAATTTTTTTTAATAAATTTATATATAATTTTTATTTAAAATTTTATTTTAAATTAAATTTTAATTTA', 'QUAL': 'CBACCGG=GGGGGGGGGGGGGGFGGGGG<GGGGGGGGGFG=GGGG1GCGGGGGGGGGGG1GEGGEGGGGG/GGGBGG0GGGGGGGGGGGGBGGGGGGGGGGGCGGGGGGGGGGGGGBGDGGGGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'C_G2A': {'QNAME': 'chr10-55904', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TAAATTTATATTTATTTATTTTTAACTAAATATAATTTTTTATATTTTTAATTTTATAAATTTTTTTTAATAAATTTATATATAATTTTTATTTAAAATTTTATTTTAAATTAAATTTTAATTTA', 'QUAL': 'CBACCGG=GGGGGGGGGGGGGGFGGGGG<GGGGGGGGGFG=GGGG1GCGGGGGGGGGGG1GEGGEGGGGG/GGGBGG0GGGGGGGGGGGGBGGGGGGGGGGGCGGGGGGGGGGGGGBGDGGGGGG', 'SAM_TAGS': ['YT:Z:UP']}}
test_read_5 = {'read_sequence': 'CTTGATAGCCTCTTAAGGAAAATTTGCTTCCAAATTTTAGCCCCCATCCTGTGCCCATGTAAACCCGAGAGACCCTAGCAGGAACACACTCCCCAACTGAGTATGGGGCTGATAAAAATGGCGCCTA', 'W_C2T': {'QNAME': 'chr10-55944', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTAATAATTTTTTAAAAAAAATTTATTTTTAAATTTTAATTTTTATTTTATATTTATATAAATTTAAAAAATTTTAATAAAAATATATTTTTTAATTAAATATAAAATTAATAAAAATAATATTT', 'QUAL': 'CBBCCGFGBGG1GGGGGGGGGGGGGGGEGGGG1EBGGGG1GGG11GGGDGGGEGGGGBFGGGGGGGFGGGGG<GGGGGGGGGGGGGGGGGGGGGGGGGG;GG>GGDGGFGFGGDG0GGGGGCGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'C_C2T': {'QNAME': 'chr10-55944', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTAATAATTTTTTAAAAAAAATTTATTTTTAAATTTTAATTTTTATTTTATATTTATATAAATTTAAAAAATTTTAATAAAAATATATTTTTTAATTAAATATAAAATTAATAAAAATAATATTT', 'QUAL': 'CBBCCGFGBGG1GGGGGGGGGGGGGGGEGGGG1EBGGGG1GGG11GGGDGGGEGGGGBFGGGGGGGFGGGGG<GGGGGGGGGGGGGGGGGGGGGGGGGG;GG>GGDGGFGFGGDG0GGGGGCGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'W_G2A': {'QNAME': 'chr10-55944', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTGATAGTTTTTTAAGGAAAATTTGTTTTTAAATTTTAGTTTTTATTTTGTGTTTATGTAAATTTGAGAGATTTTAGTAGGAATATATTTTTTAATTGAGTATGGGGTTGATAAAAATGGTGTTT', 'QUAL': 'CBBCCGFGBGG1GGGGGGGGGGGGGGGEGGGG1EBGGGG1GGG11GGGDGGGEGGGGBFGGGGGGGFGGGGG<GGGGGGGGGGGGGGGGGGGGGGGGGG;GG>GGDGGFGFGGDG0GGGGGCGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'C_G2A': {'QNAME': 'chr10-55944', 'FLAG': '147', 'RNAME': 'chr10', 'POS': '194964', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '194655', 'TLEN': '-434', 'SEQ': 'AAACACCATTTTTATCAACCCCATACTCAATTAAAAAATATATTCCTACTAAAATCTCTCAAATTTACATAAACACAAAATAAAAACTAAAATTTAAAAACAAATTTTCCTTAAAAAACTATCAA', 'QUAL': 'GGGCGGGGG0GDGGFGFGGDGG>GG;GGGGGGGGGGGGGGGGGGGGGGGGGG<GGGGGFGGGGGGGFBGGGGEGGGDGGG11GGG1GGGGBE1GGGGEGGGGGGGGGGGGGGG1GGBGFGCCBBC', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:0', 'YT:Z:CP']}}

test_read_6 = {'read_sequence': 'CTTGATAGCCTCTTAAGGAAAATTTGCTTCCAAATTTTAGCCCCCATCCTGTGCCCATGTAAACCCGAGAGACCCTAGCAGGAACACACTCCCCAACTGAGTATGGGGCTGATAAAAATGGCGCCTA', 'W_C2T': {'QNAME': 'chr10-55944', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTAATAATTTTTTAAAAAAAATTTATTTTTAAATTTTAATTTTTATTTTATATTTATATAAATTTAAAAAATTTTAATAAAAATATATTTTTTAATTAAATATAAAATTAATAAAAATAATATTT', 'QUAL': 'CBBCCGFGBGG1GGGGGGGGGGGGGGGEGGGG1EBGGGG1GGG11GGGDGGGEGGGGBFGGGGGGGFGGGGG<GGGGGGGGGGGGGGGGGGGGGGGGGG;GG>GGDGGFGFGGDG0GGGGGCGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'C_C2T': {'QNAME': 'chr10-55944', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTAATAATTTTTTAAAAAAAATTTATTTTTAAATTTTAATTTTTATTTTATATTTATATAAATTTAAAAAATTTTAATAAAAATATATTTTTTAATTAAATATAAAATTAATAAAAATAATATTT', 'QUAL': 'CBBCCGFGBGG1GGGGGGGGGGGGGGGEGGGG1EBGGGG1GGG11GGGDGGGEGGGGBFGGGGGGGFGGGGG<GGGGGGGGGGGGGGGGGGGGGGGGGG;GG>GGDGGFGFGGDG0GGGGGCGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'W_G2A': {'QNAME': 'chr10-55944', 'FLAG': '141', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TTGATAGTTTTTTAAGGAAAATTTGTTTTTAAATTTTAGTTTTTATTTTGTGTTTATGTAAATTTGAGAGATTTTAGTAGGAATATATTTTTTAATTGAGTATGGGGTTGATAAAAATGGTGTTT', 'QUAL': 'CBBCCGFGBGG1GGGGGGGGGGGGGGGEGGGG1EBGGGG1GGG11GGGDGGGEGGGGBFGGGGGGGFGGGGG<GGGGGGGGGGGGGGGGGGGGGGGGGG;GG>GGDGGFGFGGDG0GGGGGCGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'C_G2A': {'QNAME': 'chr10-55944', 'FLAG': '147', 'RNAME': 'chr10', 'POS': '194964', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '194655', 'TLEN': '-434', 'SEQ': 'AAACACCATTTTTATCAACCCCATACTCAATTAAAAAATATATTCCTACTAAAATCTCTCAAATTTACATAAACACAAAATAAAAACTAAAATTTAAAAACAAATTTTCCTTAAAAAACTATCAA', 'QUAL': 'GGGCGGGGG0GDGGFGFGGDGG>GG;GGGGGGGGGGGGGGGGGGGGGGGGGG<GGGGGFGGGGGGGFBGGGGEGGGDGGG11GGG1GGGGBE1GGGGEGGGGGGGGGGGGGGG1GGBGFGCCBBC', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:5', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:0', 'YT:Z:CP']}}

test_read_7 = {'read_sequence': 'TGGGTTTATATTTGTTTATTTTTGGCTAAATGTAATTTTTTGTATTTTTAGTTTTGGATTTCTTTTTGGTGGATTTGTGTATAGTTTTTGTTTAGGATTTTGTTTTGGATTAGGTTTTGGTTTA', 'W_C2T': {'QNAME': 'chr10-55904', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TGGGTTTATATTTGTTTATTTTTGGTTAAATGTAATTTTTTGTATTTTTAGTTTTGTGGATTTTTTTTGGTGGATTTGTGTATAGTTTTTGTTTAGGATTTTGTTTTGGATTAGGTTTTGGTTTA', 'QUAL': 'CBACCGG=GGGGGGGGGGGGGGFGGGGG<GGGGGGGGGFG=GGGG1GCGGGGGGGGGGG1GEGGEGGGGG/GGGBGG0GGGGGGGGGGGGBGGGGGGGGGGGCGGGGGGGGGGGGGBGDGGGGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'C_C2T': {'QNAME': 'chr10-55904', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '313008', 'MAPQ': '255', 'CIGAR': '62M1D62M', 'RNEXT': '=', 'PNEXT': '313310', 'TLEN': '427', 'SEQ': 'TGGGTTTATATTTGTTTATTTTTGGTTAAATGTAATTTTTTGTATTTTTAGTTTTGTGGATTTTTTTTGGTGGATTTGTGTATAGTTTTTGTTTAGGATTTTGTTTTGGATTAGGTTTTGGTTTA', 'QUAL': 'CBACCGG=GGGGGGGGGGGGGGFGGGGG<GGGGGGGGGFG=GGGG1GCGGGGGGGGGGG1GEGGEGGGGG/GGGBGG0GGGGGGGGGGGGBGGGGGGGGGGGCGGGGGGGGGGGGGBGDGGGGGG', 'SAM_TAGS': ['AS:i:-3', 'XN:i:0', 'XM:i:1', 'XO:i:0', 'XG:i:0', 'NM:i:1', 'MD:Z:77T47', 'YS:i:-5', 'YT:Z:CP']}, 'W_G2A': {'QNAME': 'chr10-55904', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TAAATTTATATTTATTTATTTTTAACTAAATATAATTTTTTATATTTTTAATTTTATAAATTTTTTTTAATAAATTTATATATAATTTTTATTTAAAATTTTATTTTAAATTAAATTTTAATTTA', 'QUAL': 'CBACCGG=GGGGGGGGGGGGGGFGGGGG<GGGGGGGGGFG=GGGG1GCGGGGGGGGGGG1GEGGEGGGGG/GGGBGG0GGGGGGGGGGGGBGGGGGGGGGGGCGGGGGGGGGGGGGBGDGGGGGG', 'SAM_TAGS': ['YT:Z:UP']}, 'C_G2A': {'QNAME': 'chr10-55904', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'TAAATTTATATTTATTTATTTTTAACTAAATATAATTTTTTATATTTTTAATTTTATAAATTTTTTTTAATAAATTTATATATAATTTTTATTTAAAATTTTATTTTAAATTAAATTTTAATTTA', 'QUAL': 'CBACCGG=GGGGGGGGGGGGGGFGGGGG<GGGGGGGGGFG=GGGG1GCGGGGGGGGGGG1GEGGEGGGGG/GGGBGG0GGGGGGGGGGGGBGGGGGGGGGGGCGGGGGGGGGGGGGBGDGGGGGG', 'SAM_TAGS': ['YT:Z:UP']}}

test_read_8 = {'read_sequence': 'CTTTTCTTTTCTTTCATTTCTTTCTCTTAAATAAACTTTCCCCTATTTTATTCTCCCTACCCTTCATTACCTATTCCCTACAAACCTACTTAAACTAAAACACTAATAAAAAAAATCAATATCAT','W_C2T': {'QNAME': 'chr10-55354', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '221597', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '221789', 'TLEN': '317','SEQ': 'CTTTTCTTTTCTTTCATTTCTTTCTCTTAAATAAACTTTCCCCTATTTTATTCTCCCTACCCTTCATTACCTATTCCCTACAAACCTACTTAAACTAAAACACTAATAAAAAAAATCAATATCAT', 'QUAL':'CBAB@GG11BGGGGGGGDF>GGGGGGGGGGGDFDGGGGGGGGGGGGGG@GGGGGGGGGG:GGEGGGGCGFGFGGEGGGGGGGFGGGGGGGGGFGGGGGG>GGGGDGEGGDG1GGGGDDGGDCGGG','SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:0', 'YT:Z:CP']},'C_C2T': {'QNAME': 'chr10-55354', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ':'TTTTTTTTTTTTTTTATTTTTTTTTTTTAAATAAATTTTTTTTTATTTTATTTTTTTTATTTTTTATTATTTATTTTTTATAAATTTATTTAAATTAAAATATTAATAAAAAAAATTAATATTAT', 'QUAL': 'CBAB@GG11BGGGGGGGDF>GGGGGGGGGGGDFDGGGGGGGGGGGGGG@GGGGGGGGGG:GGEGGGGCGFGFGGEGGGGGGGFGGGGGGGGGFGGGGGG>GGGGDGEGGDG1GGGGDDGGDCGGG', 'SAM_TAGS': ['YT:Z:UP']},'W_G2A': {'QNAME': 'chr10-55354', 'FLAG': '99', 'RNAME': 'chr10', 'POS': '221597', 'MAPQ': '255', 'CIGAR': '125M', 'RNEXT': '=', 'PNEXT': '221789', 'TLEN': '317','SEQ': 'CTTTTCTTTTCTTTCATTTCTTTCTCTTAAATAAACTTTCCCCTATTTTATTCTCCCTACCCTTCATTACCTATTCCCTACAAACCTACTTAAACTAAAACACTAATAAAAAAAATCAATATCAT', 'QUAL':'CBAB@GG11BGGGGGGGDF>GGGGGGGGGGGDFDGGGGGGGGGGGGGG@GGGGGGGGGG:GGEGGGGCGFGFGGEGGGGGGGFGGGGGGGGGFGGGGGG>GGGGDGEGGDG1GGGGDDGGDCGGG', 'SAM_TAGS': ['AS:i:0', 'XN:i:0', 'XM:i:0', 'XO:i:0', 'XG:i:0', 'NM:i:0', 'MD:Z:125', 'YS:i:0', 'YT:Z:CP']}, 'C_G2A': {'QNAME': 'chr10-55354', 'FLAG': '77', 'RNAME': '*', 'POS': '0', 'MAPQ': '0', 'CIGAR': '*', 'RNEXT': '*', 'PNEXT': '0', 'TLEN': '0', 'SEQ': 'CTTTTCTTTTCTTTCATTTCTTTCTCTTAAATAAACTTTCCCCTATTTTATTCTCCCTACCCTTCATTACCTATTCCCTACAAACCTACTTAAACTAAAACACTAATAAAAAAAATCAATATCAT', 'QUAL': 'CBAB@GG11BGGGGGGGDF>GGGGGGGGGGGDFDGGGGGGGGGGGGGG@GGGGGGGGGG:GGEGGGGCGFGFGGEGGGGGGGFGGGGGGGGGFGGGGGG>GGGGDGEGGDG1GGGGDDGGDCGGG', 'SAM_TAGS': ['YT:Z:UP']}}

test_reads = [test_read_1, test_read_2, test_read_3, test_read_4, test_read_5, test_read_6, test_read_7, test_read_8]

processed_sam_reads = {}

bsb_db = f'{test_directory}/TestData/BSB_Test_DB/'

for count, read in enumerate(test_reads):
    processed_sam_reads[f'Read_{count + 1}'] = ProcessSamAlignment(sam_line_dict=read,
                                                                   bsb_database=bsb_db,
                                                                   contig_dict={},
                                                                   conversion_threshold=(.5, 5),
                                                                   mismatch_threshold=4)


class TestSamReadProcessing(unittest.TestCase):

    def setUp(self):
        pass

    def test_read_1_output(self):
        # read one reporting zero mismatches between reference and sequence, so alignment sequences should be identical
        processed_read = processed_sam_reads['Read_1'].output_read
        read_input = test_reads[0]
        self.assertEqual(processed_read[1]['SEQ'], read_input[processed_read[2]]['SEQ'])

    def test_read_2_output(self):
        # paired read to read 1, flag should be reverse complement
        processed_read = processed_sam_reads['Read_2'].output_read
        read_input = test_reads[1]
        self.assertEqual(processed_read[1]['SEQ'], read_input[processed_read[2]]['SEQ'])

    def test_read_3_output(self):
        # test read 3 contains one mismatch, so it should pass quality filters but not evaluate equal
        processed_read = processed_sam_reads['Read_3'].output_read
        # get mismatch number
        mismatch_number = int(processed_sam_reads['Read_3'].output_read[1]['SAM_TAGS'][2].split(':')[-1])
        mapping_reference_sequence = 'GATTTGAGAAAGTGTTAGGGAGAGAATATTTTAAATTGATTGATTATATAAGAAGT' \
                                     'TAGATTTTTTTTAGTAGTTAAATTATTTATATTTTTATTAGTAGTATATTAGGTTTTTAATTAAAAGAT'
        self.assertNotEqual(processed_read[1]['SEQ'], mapping_reference_sequence)
        # check mismatched base not equal
        self.assertNotEqual(processed_read[1]['SEQ'][103], mapping_reference_sequence[103])
        # check mismatch number
        self.assertEqual(mismatch_number, 1)

    def test_read_4_output(self):
        # test read 4 has an insertion so mapping location should be adjusted by one
        processed_read = processed_sam_reads['Read_4'].output_read
        self.assertEqual(processed_read[1]['POS'], '110369')
        # check cigar has been properly flipped
        self.assertEqual(processed_read[1]['CIGAR'], '62M1I63M')

    def test_read_5_output(self):
        # read modified to fail bisulfite filter
        processed_read = processed_sam_reads['Read_5'].output_read
        conversion_flag = processed_read[1]['SAM_TAGS'][-2].split(':')[-1]
        self.assertEqual(conversion_flag, '1')

    def test_read_6_output(self):
        # read modified to fail bisulfite filter
        processed_read = processed_sam_reads['Read_6'].output_read
        bs_strand = processed_read[2]
        self.assertIsNone(bs_strand)

    def test_read_7_output(self):
        # test read 4 has an insertion so mapping location should be adjusted by one
        processed_read = processed_sam_reads['Read_7'].output_read
        self.assertEqual(processed_read[1]['POS'], '110369')
        # check cigar has been properly flipped
        self.assertEqual(processed_read[1]['CIGAR'], '62M1D62M')

    def test_multimapping(self):
        processed_read = processed_sam_reads['Read_8'].output_read
        # check if mapped read count equal to 2
        self.assertEqual(processed_read[0], 2)
        # check mapped read strand correct
        self.assertEqual(processed_read[1][3][0], 'W_C2T')
        self.assertEqual(processed_read[1][3][1], 'W_G2A')

    def test_mapping_length(self):
        # the mapping length for a reads with the cigar structure below should be identical is regards to the reference
        test_deletion_cigar = [(0, 20), (1, 1), (0, 26)]
        test_insertion_cigar = [(0, 20), (2, 1), (0, 25)]
        deletion_mapping_length = processed_sam_reads['Read_7'].get_mapping_length(test_deletion_cigar)
        insertion_mapping_length = processed_sam_reads['Read_7'].get_mapping_length(test_insertion_cigar)
        self.assertEqual(deletion_mapping_length, insertion_mapping_length)

    def test_bisulfite_conversion_check(self):
        # test bisulfite conversion check
        reference_sequence = 'CCTAAACAGAGGCTGTGCAGAGATCCACCAAGGGGAGTCCACAAGGCTGAAG'
        deletion_sequence = 'CTAAACAAAAACTATACACAAATCCACCAAAAA-GAAATCCAAAACTAAA'
        mapping_strand = '-FW'
        # check converted strand return False
        good_conversion_check = processed_sam_reads['Read_7'].check_bisulfite_conversion(deletion_sequence,
                                                                                         reference_sequence,
                                                                                         mapping_strand)
        # check unconverted returns True
        unconverted_sequence = 'CTAAACAGAGGCTGTGCAGAGATCCACCAAGGGGAGTCCACAAGGCTGAA'
        bad_conversion_check = processed_sam_reads['Read_7'].check_bisulfite_conversion(unconverted_sequence,
                                                                                         reference_sequence,
                                                                                         mapping_strand)
        self.assertFalse(good_conversion_check)
        self.assertTrue(bad_conversion_check)


if __name__ == '__main__':
    unittest.main()
