class musica:
    nome = ''
    artista = ''
    duracao =  ''

in_da_club = musica()
in_da_club.nome = 'In da Club'
in_da_club.artista = '50 cent'
in_da_club.duracao = '3:13'

lose_yourself = musica()
lose_yourself.nome = 'Lose yourself'
lose_yourself.artista = 'Eminem'
lose_yourself.duracao = '5:26'

gold_digger = musica()
gold_digger.nome = 'Gold Digger'
gold_digger.artista = 'Kayne West'
gold_digger.duracao = '3:27'

print(vars(lose_yourself))
