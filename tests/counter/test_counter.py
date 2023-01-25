from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word1 = "python"
    word2 = "javascript"

    with open(path) as file:
        result = file.read()

        count = {
            word1: result.lower().count("python"),
            word2: result.lower().count("javascript")
        }
        # A contagem de palavras deve ser case insentitive - lower()
        # param1 = path uma string com o caminho do arquivo (data/jobs.csv);
        # param2 = word uma string com a palavra a ser contabilizada
        assert count["python"] == count_ocurrences(path, word1)
        assert count["javascript"] == count_ocurrences(path, word2)
