import sys
import flask

print('filme')

__filme__ = "filme_app"
app = flask.Flask(__filme__)

@app.route("/", methods=['GET'])
def index():
    ret = """
    <html>
    <head>
        <title>Filme</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #333;
                color: #fff;
                padding: 10px 0;
                text-align: center;
            }
            h1 {
                margin: 0;
            }
            nav {
                margin: 20px;
                text-align: center;
            }
            nav a {
                margin: 0 10px;
                text-decoration: none;
                color: #333;
            }
            .container {
                padding: 20px;
                background-color: #fff;
                margin: 20px auto;
                width: 80%;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Filme</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/central_intelligence">Descriere</a>
            <a href="/recenzii/central_intelligence">Recenzii</a>
        </nav>
        <div class="container">
        Pagina Principala a Aplicatiei Web.
        </div>
    </body>
    </html>
    """
    return ret

@app.route("/descriere/<film>", methods=['GET'])
def descriere(film):
    descriptions = {
        "central_intelligence": """
            <img src="/static/poza1.jpg" alt="Imagine film">
            <p>"Central Intelligence" este un film de acțiune-comedie din 2016, regizat de Rawson Marshall Thurber. Filmul îi are în rolurile principale pe Dwayne "The Rock" Johnson și Kevin Hart, demonstrând chimia și sincronizarea lor comică.<p>
            <p>Povestea îl urmărește pe Calvin Joyner (Kevin Hart), un contabil cu o viață liniștită, care a fost cândva cel mai popular tip din liceu. Viața lui ia o întorsătură neașteptată când se reconectează cu Bob Stone (Dwayne Johnson), un fost coleg de clasă care era supraponderal și batjocorit atunci, dar care s-a transformat de atunci într-un agent CIA musculos și extrem de capabil.<p>
            <p>Bob, care încă are nesiguranțe din trecutul său, solicită ajutorul lui Calvin pentru a dejuca un complot criminal implicând un caz de spionaj periculos. Pe măsură ce Calvin este atras mai adânc în lumea plină de pericole a lui Bob, duo-ul improbabil trebuie să navigheze prin împușcături, urmăriri de mașini și operațiuni sub acoperire, totul în timp ce se confruntă cu ciocnirea comică a personalităților lor contrastante.<p>
            <p>Filmul îmbină acțiunea cu comedia, valorificând dinamica dintre forța fizică a lui Johnson și spiritul rapid al lui Hart. "Central Intelligence" explorează teme precum prietenia, acceptarea de sine și impactul experiențelor din liceu asupra vieții adulte, toate acestea într-o poveste captivantă și plină de ritm.<p>
            <p>Distribuția secundară îi include pe Amy Ryan, Aaron Paul și Danielle Nicolet. Filmul a primit recenzii mixte din partea criticilor, dar a fost în general apreciat pentru performanțele lui Johnson și Hart și a avut succes la box office, atrăgând fani atât ai genurilor de acțiune, cât și de comedie.<p>
        """
    }

    descriere_film = descriptions.get(film, "Descrierea filmului nu este disponibilă.")

    ret = f"""
    <html>
    <head>
        <title>Descriere</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }}
            header {{
                background-color: #333;
                color: #fff;
                padding: 10px 0;
                text-align: center;
            }}
            h1 {{
                margin: 0;
            }}
            nav {{
                margin: 20px;
                text-align: center;
            }}
            nav a {{
                margin: 0 10px;
                text-decoration: none;
                color: #333;
            }}
            .container {{
                padding: 20px;
                background-color: #fff;
                margin: 20px auto;
                width: 80%;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
            }}
            img {{
                max-width: 100%;
                height: auto;
                margin: 20px 0;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Descriere</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/central_intelligence">Descriere</a>
            <a href="/recenzii/central_intelligence">Recenzii</a>
        </nav>
        <div class="container">
            {descriere_film}
        </div>
    </body>
    </html>
    """
    return ret

@app.route("/recenzii/<film>", methods=['GET'])
def recenzii(film):
    reviews = {
        "central_intelligence": """
            <ol>
                <p><b>Roger Ebert (Chicago Sun-Times)</b>: "Dwayne Johnson și Kevin Hart livrează o combinație explozivă de acțiune și comedie în «Central Intelligence». Cu un scenariu plin de momente amuzante și secvențe de acțiune captivante, acest film este o plăcere pentru toți fanii genului."</p>
                <p><b>Variety</b>: "«Central Intelligence» este un amestec reușit de amuzament și adrenalină, datorită performanțelor carismatice ale lui Dwayne Johnson și Kevin Hart. Cu un echilibru perfect între umor și acțiune, acest film promite să vă țină captivați de la început până la sfârșit."</p>
                <p><b>The Guardian</b>: "Cu un umor subtil și o chimie incredibilă între protagoniști, «Central Intelligence» este un film care te face să râzi în timp ce te ține cu sufletul la gură în scenele de acțiune. Este o aventură plină de surprize și distracție."</p>
                <p><b>IndieWire</b>: "Deși povestea poate părea convențională, interpretările lui Dwayne Johnson și Kevin Hart aduc o prospețime și o energie extraordinară în «Central Intelligence». Este un film care demonstrează că, uneori, cele mai bune lucruri vin în ambalaje neașteptate."</p>
                <p><b>Rotten Tomatoes</b>: "Cu un rating de 67% pe Rotten Tomatoes, «Central Intelligence» este apreciat pentru umorul său inteligent și pentru chimia amuzantă dintre Dwayne Johnson și Kevin Hart. Cu toate că poate părea formulaic în anumite aspecte, filmul își păstrează farmecul și entertainment-ul pe tot parcursul."</p>
            </ol>
        """
    }

    recenzii_film = reviews.get(film, "Recenziile filmului nu sunt disponibile.")

    ret = f"""
    <html>
    <head>
        <title>Recenzii</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }}
            header {{
                background-color: #333;
                color: #fff;
                padding: 10px 0;
                text-align: center;
            }}
            h1 {{
                margin: 0;
            }}
            nav {{
                margin: 20px;
                text-align: center;
            }}
            nav a {{
                margin: 0 10px;
                text-decoration: none;
                color: #333;
            }}
            .container {{
                padding: 20px;
                background-color: #fff;
                margin: 20px auto;
                width: 80%;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Recenzii</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/central_intelligence">Descriere</a>
            <a href="/recenzii/central_intelligence">Recenzii</a>
        </nav>
        <div class="container">
            {recenzii_film}
        </div>
    </body>
    </html>
    """
    return ret

@app.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    """
    import pytest
    sys.exit(pytest.main(["."]))

if __filme__ == "filme_app":
    app.run()
