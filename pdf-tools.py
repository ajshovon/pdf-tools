from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse


def oddNumbers(l, r):
    return list(range(l | 1, r + 1, 2))


def evenNumbers(l, r):
    return list(range(l | 2, r + 1, 2))


def deletePages(inputFileName, outputFileName, EorO):
    inputFile = PdfFileReader(inputFileName, "rb")
    output = PdfFileWriter()
    totalPages = inputFile.getNumPages()
    if EorO == "even":
        pageNumbers = evenNumbers(2, totalPages)
    elif EorO == "odd":
        pageNumbers = oddNumbers(1, totalPages)
    # print(pageNumbers)
    # print(totalPages)
    for i in range(1,totalPages+1):
        # print(i)
        if i not in pageNumbers:
            p = inputFile.getPage(i-1)
            output.addPage(p)
    with open(outputFileName, "wb") as f:
        output.write(f)


parser = argparse.ArgumentParser(
    description="PDF tools written in python with PyPDF2..."
)
parser.add_argument(
    "-d",
    "--delete",
    choices=["even", "odd"],
    help="Delete every even or odd  number pages",
)
parser.add_argument("-i", "--input", type=str, help="Enter tharget pdf name")
parser.add_argument("-o", "--output", type=str, help="Enter new pdf name")
args = parser.parse_args()
inputFile = args.input
outputFile = args.output
EvenOrOdd = args.delete


if __name__ == "__main__":
    if EvenOrOdd:
        try:
            deletePages(inputFile, outputFile, EvenOrOdd)
        except:
            print("error")
        else:
            print(
                "\nSuccessfully deleted",
                EvenOrOdd,
                "pages from",
                inputFile,
                "and saved as",
                outputFile,
            )

    else:
        parser.print_help()
