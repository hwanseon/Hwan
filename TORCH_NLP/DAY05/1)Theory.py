# p 313
# 1개의 문장을 구성하는 토큰의 수 6 ==> squence_len = 6

# 뭔 말인지 모루겠네

##
# >>> # example with padding_idx
# >>> embedding = nn.Embedding(10, 3, padding_idx=0)    -> 단어사전의 수가 10
# >>> input = torch.LongTensor([[0, 2, 0, 5]])          -> 4행
# >>> embedding(input)
# tensor([[[ 0.0000,  0.0000,  0.0000],
#          [ 0.1535, -2.0309,  0.9315],
#          [ 0.0000,  0.0000,  0.0000],
#          [-0.1655,  0.9897,  0.0635]]])

# >>> embedding = nn.Embedding(10, 3, padding_idx=0)   
# >>> input = torch.LongTensor([[0, 2, 0, 5]]) 

## 0번 0000 ...0 (10개)
## 2번 0100 ...0 (10개)
## 0번 0000 ...0 (10개)
## 5번 00001...0 (10개) 
## 리스트의 원소가 4개라서 4행, 단어 사전의 수가 10개라서 10행 => (4, 10)인데 피쳐의 수를 10 -> 3으로 줄여야함
