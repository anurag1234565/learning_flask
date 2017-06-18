from flask import Flask, render_template

app = Flask(__name__)  # creating a Flask object


# Home Page
@app.route("/")
def index():
    videos = [{'code': '5CQZiHonkcw', 'title': 'New Season'},
              {'code': 'BCwKEUWcJME', 'title': 'Infantino Street'},
              {'code': 'PGBhvCJdJX4', 'title': 'Finish Line Scene'},
              {'code': '6j8A-N_KigM', 'title': 'Season 3 Finale | Sizzle'},
              {'code': 'OL94MGoBS3w', 'title': ' I Know Who You Are Scene'}
              ]
    return render_template("main.html",videos=videos)


# Galary
@app.route("/gallery/")
def gallery():
    images = [{'link': 'http://fanaru.com/the-flash/image/190033-the-flash-the-flash.jpg',
               'description': 'The Flash'},
              {'link': 'https://fsmedia.imgix.net/b7/3a/b5/c9/084e/4533/8903/edcdcee5bb61/the-speed-force.png?dpr=1.5&auto=format,compress&q=75',
               'description': 'Barry Allen in the Speedforce'},
              {'link': 'http://www.etonline.com/tv/2015/05/24149447/640_flash_barry_iris.jpg',
               'description': 'Barry and Iris'},
              {'link': 'http://2paragraphs.com/wp-content/uploads/2016/10/Jesse-The-Flash-CW.jpg',
               'description': 'Jessy Quick'},
              {'link': 'http://static.srcdn.com/wp-content/uploads/2017/01/Cisco-as-Vibe-in-The-Flash.jpg',
               'description': 'Cisco AKA Vibe'},
              {'link':'http://static.srcdn.com/wp-content/uploads/2017/04/The-Flash-Once-and-Future-Flash-Savitar-Poster.jpg',
               'description': 'The Flash Vs Savatar'},
              {'link': 'http://legionofleia.com/wp-content/uploads/2016/01/Flash-Reverse-Flash.png',
               'description': 'Reverse Flash( Eobard Thawn )'},
              {'link': 'http://www.cbr.com/wp-content/uploads/2017/03/The-Flash-Into-the-Speed-Force-feature.jpg',
               'description': 'Jay Garrik(Flash) and Barry Allen(Flash)'},
              {'link': 'http://heroichollywood.b-cdn.net/wp-content/uploads/2016/09/The-CW-DC-TV-Superhero-Fight-Club.jpg',
               'description':'Arrow verse'},
              {'link': 'http://images.parentherald.com/data/images/full/79395/the-cw-crossover.jpg',
               'description': 'Arrow, Flash and Supergirl'},
              {'link':'http://www.gamingilluminaughty.com/wp-content/uploads/2016/02/The-Flash-Killer-Frost.jpg',
              'description': 'Killer Frost'},
              {'link':'http://cdn.entertainmentfuse.com/media/2016/07/The-Flash-TV-Show-Wally-West-Costume.jpg',
               'description': 'Wally West (Kid Flash)'}
              ]
    return render_template("gallery.html", images=images)


if __name__ == "__main__":
    app.run()
