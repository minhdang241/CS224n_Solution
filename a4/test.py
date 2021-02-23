from utils import read_corpus, batch_iter

def main():
    #train_data_src = read_corpus('./chr_en_data/train.chr', source='src', vocab_size=21000) 
    train_data_tgt = read_corpus('./chr_en_data/train.en', source='tgt', vocab_size=8000)
    print(len(train_data_tgt))
    print(train_data_tgt[2])


if __name__ == '__main__':
    main()
