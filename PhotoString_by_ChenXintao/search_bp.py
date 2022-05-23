from flask import Blueprint, request
from UseSqlite import InsertQuery
from datetime import datetime
from show_bp import get_database_photos


search_bp = Blueprint('search_bp',__name__)


@search_bp.route('/',methods=['POST','GET'])
def main():
    if request.method=='POST':
        uploaded_file=request.files['file']
        time_str=datetime.now().strftime('%Y%m%d%H%M%S')
        new_filename=time_str+'.jpg'
        uploaded_file.save('./static/upload/'+new_filename)
        time_info=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        description=request.form['description']
        path='./static/upload/'+new_filename
        iq=InsertQuery('./static/RiskDB.db')
        iq.instructions("INSERT INTO photo Values('%s','%s','%s','%s')"%(time_info,description,path,new_filename))
        iq.do()
        return '<p>You have uploaded %s.<br/> <a href="/">Return</a>.'%(uploaded_file.filename)
    else:
        page='''<form action="/"method="post"enctype="multipart/form-data">
        <input type="file"name="file"><input name="description"><input type="submit"value="Upload"></form>'''
        page+=get_database_photos()
        return page