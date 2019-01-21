import datetime

from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return getHTMLtemplate(getTime())


def getTime():
    dateTime = str(datetime.datetime.now())
    
    return dateTime

def getHTMLtemplate(theTime):
    text = """
    <html>
    <body>

    <h1>UniqueIdentifier</h1>
    <script>
    
    document.write(new Date())
    console.log(new Date())
    
    </script>
    </body>
    </html>
    """
    
    return text.replace("UniqueIdentifier",theTime)
if __name__ == "__main__":
    app.run(debug=True)




