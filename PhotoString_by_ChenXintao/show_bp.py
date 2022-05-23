from flask import Blueprint
from UseSqlite import RiskQuery
from upload_bp import make_html_paragraph


show_bp = Blueprint('show_bp' , __name__)


@show_bp.route ('/show')
def get_database_photos():
    rq=RiskQuery('./static/RiskDB.db')
    rq.instructions("SELECT * FROM photo ORDER By time desc")
    rq.do()
    record='<p>My past photo</p>'
    for r in rq.format_results().split('\n\n'):
        record+='%s'%(make_html_paragraph(r))
    return record+'</table>\n'

