from flask import Blueprint
from PIL import Image

upload_bp = Blueprint('upload_bp', __name__)

@upload_bp.route('/upload')
def make_html_paragraph(s):
    if s.strip()=='':
        return ''
    lst=s.split(',')
    picture_path=lst[2].strip()
    picture_name=lst[3].strip()
    im = Image.open(picture_path)
    im.thumbnail((400, 300))
    im.save('./static/figure/'+picture_name, 'jpeg')
    result='<p>'
    result+='<i>%s</i><br/>'%(lst[0])
    result+='<i>%s</i><br/>'%(lst[1])
    result+='<a href="%s"><img src="./static/figure/%s"alt="风景图"></a>'%(picture_path,picture_name)
    return result+'</p>'