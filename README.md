# Weird Text Format-8

## Usage

```bash
usage: WeirdTextFormat8.py [-h] [-e | -d] [-i [INFILE]] [-o [OUTFILE]]

optional arguments:
  -h, --help            show this help message and exit
  -e, --encode          Encode a string into the corresponding list of integer values usingWeird Text Format-8
  -d, --decode          Decode a list of integer values encoded with Weird Text Format-8back into its original string
  -i [INFILE], --infile [INFILE]
                        Specify a file to read input from (default: stdin)
  -o [OUTFILE], --outfile [OUTFILE]
                        Specify a file to write output to (default: stdout)
```

- You can choose the either of the -e or -d options, but not both, to indicate if you are encoding a string, or decoding a list of integers. If you don't specify either, you will be prompted in the terminal to choose one.
- You can specify an input file with the -i option. If you don't specify a file, you will be prompted to enter the input manually in the terminal.
- You can specify an output file with the -o option. If you don't specify a file, the output will be printed to the terminal.

## Tests

```bash
usage: TestWeirdTextFormat8.py
```

Simply run the test file to run all the tests.
