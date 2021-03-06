import json
import logging
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #template_path=os.path.join(os.getcwd(), "templates"),
    #static_path=os.path.join(os.getcwd(), "static")
    return render_template('index.html', title='scheduling calendar')
"""    
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
"""

"""
class GetCalendar(RequestHandler):
    #getting calendar

    def initialize(self):
        logging.info("GetCalendar [initialize]")

    def get(self):
        logging.info("GetCalendar [get]")

        ###TODO getting japananese holiday from https://holidays-jp.github.io/api/v1/date.csv
        data = [
            {
                "title": "All Day Event",
                "start": "2020-06-05"
            },
            {
                "title": "Long Event",
                "start": "2020-06-06",
                "end": "2020-06-22"
            },
            {
                "id":  "999",
                "title": "Repeating Event",
                "start": "2020-06-09T16:00:00-05:00"
            },
            {
                "id":  "999",
                "title": "Repeating Event",
                "start": "2020-06-16T16:00:00-05:00"
            },
            {
                "id": "1000",
                "title": "Meeting",
                "start": "2020-06-20T10:30:00-05:00",
                "end": "2020-06-20T12:30:00-05:00"
            }
        ]

        self.write(json.dumps(data))

app = tornado.web.Application([
    (r"/", MainHandler),
    (r"/getCalendar", GetCalendar),
],
    template_path=os.path.join(os.getcwd(), "templates"),
    static_path=os.path.join(os.getcwd(), "static"),
)
"""

if __name__ == "__main__":
    """
    ## it's to delete
    options.parse_command_line()
    app.listen(8080)
    logging.info("server started")
    tornado.ioloop.IOLoop.instance().start()
    """
    app.run(debug=True)