import pafy

url = input('Cole a url do video: ')
aov = ''
video = pafy.new(url)
print('A url escolhida foi: {}'.format(url))

while aov not in ['audio', 'video']:
    aov = input('Àudio ou video? ').strip().replace('à', 'a').replace('í', 'i').lower()
print('Você baixar um {}'.format(aov))
caminho = input('Caminho do arquivo: ')
print('O caminho do arquivo eh {}'.format(caminho))
o = input('Você quer a melhor configuração? ')

if o.strip().lower() == 'sim':
    print('Entendi \'{}\''.format('sim'))
    if aov == 'audio':
        print('Baixando melhor o áudio.')
        video.getbestaudio().download(filepath=caminho)
    else:
        print('Baixando melhor o video...')
        video.getbest().download(filepath=caminho)
else:
    print('Entendi \'não\'')
    print(', então você escolherá dentre as opções disponíveis.')
    if aov == 'audio':
        print('Listarei as opções de áudio.')
        auds = video.audiostreams
        for i in range(len(auds)):
            s = auds[i]
            print(i+1, s.bitrate, s.extension, s.get_filesize())
        a = int(input('Escolha uma das opções disponíveis: '))
        auds[a-1].download()
    elif aov == 'video':
        print('Listarei todas as opções de vídeo.')
        s = video.streams
        for i in range(len(s)):
            a = s[i]
            print(i+1, a.resolution, a.extension, a.get_filesize())
        o = int(input('Escolha uma das opções disponíveis: '))
        s[o-1].download()

