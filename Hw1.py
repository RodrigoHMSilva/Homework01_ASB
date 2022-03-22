from Bio import Entrez
import sys

#Usage: in terminal - python3 filename.py "email" "database" "term"


def procura():
    Entrez.email = sys.argv[1]
    userdatabase = sys.argv[2]
    useterm = sys.argv[3]
    searchHandle = Entrez.esearch(db = userdatabase, usehistory="y", term = useterm, idtype = "acc")
    searchResult = Entrez.read(searchHandle)
    webEnv = searchResult["WebEnv"]
    queryKey = searchResult["QueryKey"]
    searchHandle.close()
    results = [queryKey, webEnv]
    return results

def resultados(rslt):
    fetchHandle = Entrez.efetch(db = "nucleotide", rettype = "fasta", retmode = "text", query_key = rslt[0], webenv = rslt[1],idtype = "acc")
    print(fetchHandle.read())
    fetchHandle.close()

rslt = procura()
resultados(rslt)