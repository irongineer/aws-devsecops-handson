import ftplib
from flask import (
    Blueprint,
    render_template
)

bp = Blueprint(
    "a3", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/A3")
def a3():
    ### Is this really necessary? FTP is a cleartext protocol
    try:
        connection = ftplib.FTP("ftp.example.com")
    except:
        pass
    return render_template("a3.html")