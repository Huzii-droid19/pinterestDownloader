from io import BytesIO
import os
from pickle import TRUE
from flask import Flask, send_file
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from api.pypin import downloadPinterestMedia

parser = reqparse.RequestParser()
parser.add_argument('url', type=str, required=True,
                    help="URL cannot be empty and must be valid")

app = Flask(__name__)
api = Api(app)
CORS(app)


class PinterestDownloader(Resource):
    def post(self):
        args = parser.parse_args()
        url = args['url']
        file_name = downloadPinterestMedia(url)
        output = BytesIO()
        with open(file_name, 'rb') as f:
            output.write(f.read())
            output.seek(0)
        os.remove(file_name)
        return send_file(output, as_attachment=True, download_name=file_name)


api.add_resource(PinterestDownloader, '/api/v1/download/media')
