import subprocess
from BSB.BSB_Align.StreamTabFormat import StreamTab


class Bowtie2Align:
    """Launch external bowtie2 mapping commands using streamed tab format. Alignment works by performing base
     substitutions of the original fastq reads and piping them into the bowtie2 instance. The stdout generate by
     bowtie2 is then yielded and processes by the BS_align.AlignmentHelpers.launch_bowtie2_mapping function.

     Keyword Arguments:
            fastq1 (str): path to fastq file
            fastq2 (str): path to fastq1 mate pair
            bowtie2_commands (list of str): commands to use for bowtie2 alignment
            replacement_base1 (str): base to replace for fastq1 read
            replacement_base2 (str): base to replace for fastq2 read
            bsb_database(str): path to bsb 2 directory with specific mapping reference suffix
            bowtie2_path(str): path to bowtie2 executable
        Attributes:
            self.fastq1 (str): path to fastq file
            self.fastq2 (str): path to fastq1 mate pair
            self.bowtie2_commands (list of str): commands to use for bowtie2 alignment
            self.bsb_database(str): path to bsb 2 directory
            self.tab_commands (dict): dict of str, listing paths and replacement bases to stream fastq(s) for alignment
            self.paired_end (bool): paired end fastq files
            self.replacement_base2 = Base to replace for fastq2 read
            self.bowtie2_alignment (subprocess): subprocess instance of bowtie2 alignment

    """

    def __init__(self, fastq1=None, fastq2=None, bowtie2_commands=None, replacement_base1=None, replacement_base2=None,
                 bowtie2_path=None, bowtie2_database=None):
        if bowtie2_commands:
            assert isinstance(bowtie2_commands, list)
        self.bowtie2_commands = bowtie2_commands
        assert isinstance(bowtie2_path, str)
        self.bowtie2_path = bowtie2_path
        assert isinstance(bowtie2_database, str)
        self.bowtie2_database = bowtie2_database
        assert isinstance(fastq1, str)
        self.tab_commands = dict(fastq1=fastq1, fastq2=fastq2,
                                 replacement_base1=replacement_base1, replacement_base2=replacement_base2)
        self.paired_end = False
        if fastq2:
            self.paired_end = True
        self.replacement_base2 = replacement_base2
        self.bowtie2_alignment = None
        self.launch_bowtie2_alignment()

    def launch_bowtie2_alignment(self):
        """Initialize tab conversion object and launch bowtie2 with StreamTab yielding to stdin"""
        # initialize tab conversion stream
        tab_conversion = StreamTab(**self.tab_commands).tab_conversion
        # format the bowtie2 command and stream tab5 for single end and tab6 for paired end
        bowtie2_command = self.format_bowtie2_command
        # launch bowtie2 alignment as external subprocess command
        self.bowtie2_alignment = subprocess.Popen(bowtie2_command,
                                                  stdin=tab_conversion.stdout,
                                                  stdout=subprocess.PIPE,
                                                  universal_newlines=True)

    def __iter__(self):
        """ Yield dictionary of mapped reads from self.bowtie2_alignmentstdout"""
        # iterate through stdout
        for sam_line in iter(self.bowtie2_alignment.stdout.readline, ''):
            # yield processing line
            yield self.process_sam_line(sam_line)
        # close stdout when iteration completes
        self.bowtie2_alignment.stdout.close()
        # wait for return code
        return_code = self.bowtie2_alignment.wait()
        # if non-zero return code raise error
        if return_code:
            raise subprocess.CalledProcessError(return_code, 'Pipe error')

    @property
    def format_bowtie2_command(self):
        """Add bowtie2 database and specific streaming format"""
        bowtie2_command = [self.bowtie2_path]
        bowtie2_command.extend(self.bowtie2_commands)
        # add path for correct bowtie2 database
        bowtie2_command.extend(['-x', self.bowtie2_database])
        input_file_style = '--tab5'
        # if paired end stream tab6
        if self.paired_end:
            input_file_style = '--tab6'
        bowtie2_command.extend([input_file_style, '-'])
        return bowtie2_command

    @staticmethod
    def process_sam_line(sam_line):
        # yield parsed sam line as dict
        if sam_line:
            processed_sam_line: list = sam_line.replace('\n', '').split('\t')
            QNAME, FLAG, RNAME, POS, MAPQ, CIGAR, RNEXT, PNEXT, TLEN, SEQ, QUAL, *SAM_TAGS = processed_sam_line
            return dict(QNAME=QNAME, FLAG=FLAG, RNAME=RNAME, POS=POS, MAPQ=MAPQ, CIGAR=CIGAR, RNEXT=RNEXT, PNEXT=PNEXT,
                        TLEN=TLEN, SEQ=SEQ, QUAL=QUAL, SAM_TAGS=SAM_TAGS)
