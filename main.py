#import packeges and modules
from flask import Flask, render_template, request, redirect
import parse


#create flask app
app = Flask(__name__)

#main page generate
@app.route('/<id_>', methods = ['POST', 'GET'])
def index(id_):
    try:
        photo = parse.parse_photo(id_)
        songs = parse.parse_songs(id_)
        artists = parse.parse_artist(id_)
        song_names = parse.parse_songs_names(id_)
        if request.method == 'POST':
            if 'prev' in request.form:
                return redirect(f'/{int(id_)-1}')
            elif 'next' in request.form:
                return redirect(f'/{int(id_)+1}')
    except IndexError:
        return redirect('/1')
    return render_template('index.html', url = 'https://mp3push.com' + songs[int(id_)-1].attrs['data-mp3'], artist = artists[int(id_)-1].text, song_name = song_names[int(id_)-1].text, image = photo[1].attrs['src'], id_ = id_)

#start app
if __name__ == '__main__':
    app.run(debug = True)